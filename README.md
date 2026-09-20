# gnidart — Trading Books Library + Document Conversion Pipeline

A collection of trading/investing books (PDF, EPUB) plus an automated pipeline
that converts every document into clean, structured **Markdown + JSON** suitable
for RAG / LLM chunking (heading hierarchy, table extraction, OCR fallback).

`Trading.txt` is the original curated reading list. Everything below covers the
conversion operations layer.

## Repo layout

| Path | What it is |
|---|---|
| `*.pdf`, `*.epub` (repo root) | Source books. The only inputs the pipeline reads. Never deleted by automation. |
| `*.mobi`, `*.azw` | Present but **unsupported** — recorded in `output/unsupported_formats.json`, never processed. |
| `process_docs.py` | The batch converter (Docling). See Operations. |
| `healthcheck.sh` | 5-hour monitor: sanity checks, auto-restart, agentic pass. See Operations. |
| `check_prompt.txt` | Checklist prompt for the agentic (`opencode run`) health pass. |
| `output/` | All generated artifacts: per-book dirs, `manifest.json`, logs, reports. |
| `.healthcheck.lock` | flock guard so cron runs never overlap. Do not delete while a check runs. |

## Operations

### 1. Prerequisites

- Python 3.12, Docling 2.121.0, CPU-only torch (no GPU on this box).
- Docling models (RapidOCR PP-OCRv6, TableFormer weights) are cached locally —
  the batch never downloads at runtime.
- Hardware envelope: 2-core CPU, ~7.6 GB RAM, tight disk. Every setting below
  is tuned for that: expect **1–17 h per large PDF**, EPUBs take seconds.

### 2. How the conversion works (`process_docs.py`)

Pipeline per file: Docling PDF pipeline (table structure **FAST** mode, OCR on
for scanned pages, picture images off to save disk) → `output/<Book-Stem>/document.md`
+ `document.json`. EPUBs extract natively with chapter structure.

- **Supported:** `.pdf`, `.epub`. **Skipped:** `> 50 MB` files (`MAX_FILE_SIZE_MB`,
  OOM risk) → manifest status `skipped_too_large`.
- **Dedup:** SHA256 over source files; byte-identical copies processed once.
- **Manifest** (`output/manifest.json`, saved after every file = crash recovery).
  Statuses: `success` · `error` (always carries a message) · `skipped_too_large` ·
  `skipped_oom` (file that OOM-killed the box; quarantined with reason) ·
  `skipped_resume`.
- **Resume is two-layer:** files with finished outputs are skipped, and stems
  already recorded as `skipped_*` are skipped without re-running (so an OOM-killer
  file can never trap a restart in a death loop).
- **Logs:** `output/processing.log` (per-record flush = source of truth).
  Stdout mirrors it; run python with `-u` so piped `tee` captures don't lag hours.

### 3. Running the batch

Always inside the named tmux session, always unbuffered, always resumable:

```bash
tmux new-session -d -s docling-batch -c /data/gnidart
tmux send-keys -t docling-batch "python3 -u process_docs.py 2>&1 | tee /tmp/opencode/docling-cron.log" Enter
```

Just re-run the same commands to resume — finished files are skipped automatically.
Check progress with `tail -3 output/processing.log`.

### 4. Monitoring (`healthcheck.sh` + cron)

```bash
0 */5 * * * /data/gnidart/healthcheck.sh
```

Each run appends to `output/schedule_reports.log` and does, in order:
manifest counts → `document.md` count → process/tmux state → sanity checks
(outputs present, no duplicate-content surprises, errors have messages) →
disk + current file → agentic pass:

```bash
/root/.opencode/bin/opencode run --auto "$(cat check_prompt.txt)" --model opencode/mimo-v2.5-free
```

`--auto` is required: cron has no TTY, so without it every permission prompt
auto-rejects. If the batch is dead, the script restarts it with resume.
Concurrency guard is `flock` on `.healthcheck.lock`.

### 5. Quick status checks

```bash
# manifest counts
python3 -c "import json; from collections import Counter; d=json.load(open('output/manifest.json')); print(len(d), dict(Counter(v['status'] for v in d.values())))"
# process alive — bracket pattern! plain "process_docs.py" self-matches wrapper shells
pgrep -f "[p]rocess_docs\.py" >/dev/null && echo ALIVE || echo DEAD
tmux has-session -t docling-batch 2>/dev/null && echo "tmux: alive"
tail -3 output/processing.log
find output -name "document.md" | wc -l
df -h / | tail -1
```

### 6. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Tmux pane shows `Killed`, log stops mid-file | OOM killer (recurring on this box) | Restart per §3; resume continues. If the **same** file kills twice, mark it `skipped_oom` in `manifest.json` (mirror the existing entry: `status`, `file`, `size_mb`, `reason`) so resume passes over it. |
| Cron logs `healthcheck already running` every slot | Stale `flock`: a forked tmux server inherited lock FD 9 | `tmux kill-server` (releases the lock), verify with `flock -n .healthcheck.lock true`, restart per §3. `healthcheck.sh` already closes FD 9 before spawning tmux, so this should not recur. |
| `tee` capture (`/tmp/opencode/*.log`) hours behind `processing.log` | Block-buffered stdout through the pipe | Always launch with `python3 -u` (§3). |
| Disk ≥ 90% used | Output + model cache growth | Free space before the batch stalls; never delete `output/manifest.json` (keep the `manifest.json.bak-*` copies). |
| Cron monitor replaced / manifest entries vanishing | Only `healthcheck.sh` (this repo) may own the cron slot; never grant unsupervised jobs delete rights on the manifest | Repoint cron at `healthcheck.sh`, quarantine the intruder. |

### 7. Known quirks (not bugs)

- The 2010/2011 "Complete Resource" editions produce byte-identical markdown
  (same book text, different source PDFs) — both outputs are kept deliberately.
- `process_docs.py`'s module docstring still says "ACCURATE table extraction";
  actual mode is `TableFormerMode.FAST` (line ~80) — FAST is what survives OOM.
- A few files show garbled OCR on title pages only; body text is clean.
- `output/schedule_reports.log` and `output/cron.log` both exist from different
  monitoring generations; `schedule_reports.log` is the current one.
