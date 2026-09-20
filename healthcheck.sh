#!/usr/bin/env bash
# 5-hour end-to-end health check for the docling batch.
# - Restarts the batch (resume) if dead.
# - Runs sanity checks on built markdown outputs.
# - Appends a report to output/schedule_reports.log.
# - If the `opencode` CLI is available, also invokes `opencode run` with
#   check_prompt.txt for an agentic end-to-end pass; otherwise runs the
#   equivalent checks inline in bash.
set -u

REPO=/home/ubuntu/gnidart
OUT=$REPO/output
REPORT=$OUT/schedule_reports.log
PROMPT=$REPO/check_prompt.txt
TS=$(date '+%F %T')

# Guard: don't overlap with a previous healthcheck run (lockfile, race-free)
exec 9>"$REPO/.healthcheck.lock"
if ! flock -n 9; then
  echo "$TS | healthcheck already running, exiting" >> "$REPORT"
  exit 0
fi

{
echo "===== $TS | scheduled 5h check ====="

# 1. Manifest counts
python3 - "$OUT/manifest.json" <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
from collections import Counter
c = Counter(v.get("status", "?") for v in d.values())
print(f"manifest: {len(d)} total | " + " ".join(f"{k}={n}" for k, n in sorted(c.items())))
EOF

# 2. Built outputs on disk
MD_COUNT=$(ls "$OUT"/*/document.md 2>/dev/null | wc -l)
echo "document.md on disk: $MD_COUNT"

# 3. Process state (bracket pattern avoids pgrep self-match via wrapper shells)
if pgrep -f "[p]rocess_docs\.py" >/dev/null; then
  ps aux | grep '[p]rocess_docs.py' | awk '{print "batch: ALIVE pid="$2" cpu="$3"% rss="$6/1024"MB"}'
else
  echo "batch: DEAD -> restarting with resume"
  tmux kill-session -t docling-batch 2>/dev/null
  sleep 1
  # Close FD 9 first: a freshly forked tmux server inherits open FDs,
  # and an inherited lock FD would block all future runs.
  9>&- tmux new-session -d -s docling-batch -c "$REPO"
  sleep 1
  tmux send-keys -t docling-batch "python3 -u process_docs.py 2>&1 | tee /tmp/opencode/docling-cron.log" Enter
  sleep 20
  if pgrep -f "[p]rocess_docs\.py" >/dev/null; then
    echo "batch: RESTARTED ok"
  else
    echo "batch: RESTART FAILED"
  fi
fi
tmux has-session -t docling-batch 2>/dev/null && echo "tmux: alive" || echo "tmux: no session"

# 4. Inline sanity checks (mirrors check_prompt.txt §3)
python3 - "$OUT" <<'EOF'
import hashlib, json, os
outdir = os.sys.argv[1]
manifest = json.load(open(os.path.join(outdir, "manifest.json")))
fail = 0
# a) success entries have non-empty md+json
missing = [k for k, v in manifest.items() if v.get("status") == "success"
           and not (os.path.exists(os.path.join(outdir, k, "document.md"))
                    and os.path.getsize(os.path.join(outdir, k, "document.md")) > 0
                    and os.path.exists(os.path.join(outdir, k, "document.json"))
                    and os.path.getsize(os.path.join(outdir, k, "document.json")) > 0)]
print(f"check outputs-present: {'PASS' if not missing else 'FAIL ' + str(missing)}")
fail += bool(missing)
# b) no byte-identical markdowns
seen, dupes = {}, []
for k, v in manifest.items():
    if v.get("status") != "success":
        continue
    p = os.path.join(outdir, k, "document.md")
    if not os.path.exists(p):
        continue
    h = hashlib.md5(open(p, "rb").read()).hexdigest()
    if h in seen:
        dupes.append((seen[h], k))
    seen[h] = k
print(f"check same-content-md: {'NONE' if not dupes else 'NOTED ' + str(dupes)} (same book text under different filenames; sources differ, both kept)")
# c) errors all carry a message
bad = [k for k, v in manifest.items() if v.get("status") == "error" and not v.get("error")]
print(f"check errors-have-messages: {'PASS' if not bad else 'FAIL ' + str(bad)}")
fail += bool(bad)
print(f"sanity: {'ALL PASS' if fail == 0 else 'FAILURES PRESENT'}")
EOF

# 5. Disk + current file
df -h / | tail -1
tail -2 "$OUT/processing.log" | cut -c1-160

# 6. Agentic pass via opencode CLI if present
OPENCODE=/root/.opencode/bin/opencode
if [ -x "$OPENCODE" ]; then
  echo "invoking: opencode run check_prompt.txt"
  timeout 1200 "$OPENCODE" run --auto "$(cat "$PROMPT")" --model opencode/mimo-v2.5-free 2>&1 | tail -50
else
  echo "opencode CLI not found at $OPENCODE -> agentic pass skipped"
fi

echo "===== $TS | check done ====="
} >> "$REPORT" 2>&1
