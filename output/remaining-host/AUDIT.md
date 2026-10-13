# Host-only conversion resumption audit

Observed on 2026-10-03 at 02:29 UTC in /home/ubuntu/gnidart.

## Verified previous progress

Source evidence: README.md, process_docs.py, output/manifest.json, output/processing.log, output/schedule_reports.log and Git commit f042c603a14850a297f1a79793f7e0aa977fac56.

The original pipeline exports Markdown and Docling JSON, not DOCX. The last logged batch completed on 2026-09-29. Original manifest: 141 entries, 139 success, two skipped_oom. All 139 success entries have readable non-empty Markdown and parseable JSON; Markdown character counts match manifest metadata. The original manifest remains byte-identical to HEAD. Source files and existing completed outputs were not edited.

There are 150 supported source files, 149 unique byte hashes. A single identical Algorithmic Trading annotated copy is excluded. Eight unique PDFs were missed because resume/output identity uses filename stem rather than source hash: seven PDF/EPUB pairs and one different annotated PDF in New Folder. These are unconverted source variants, not eight entirely missing book titles.

The Handbook of Technical Analysis 2016.pdf is a Git LFS pointer (134 bytes), not a usable local PDF. Its pointer object hash matches the successful manifest entry; existing converted output is retained. No LFS download was attempted.

Eight MOBI/AZW files remain outside the original supported conversion scope. Some are alternate formats of completed books; The Blind Side and Moneyball have no supported counterpart in this directory. They are not in this run.

README and healthcheck contain old /data/gnidart and /root paths. Actual code has a 150 MB threshold, despite README describing 50 MB. The original batch's 'Processed: 149' summary includes resume skips and is not a count of newly converted sources. No conversion process was active before this task; ubuntu has no crontab. No old monitor or agentic auto-restart was enabled.

## Remaining source queue: ten PDFs

A Complete Guide To Volume Price Analysis 2013.pdf
Day Trading For Dummies 3rd edition 2014.pdf
Evidence-Based Technical Analysis - Applying the Scientific Method and Statistical Inference to Trading Signals 2007.pdf
Fooled by Randomness - The Hidden Role of Chance in Life and in the Markets 2005.pdf
How to Make Money in Stocks - A Winning System in Good Times and Bad 4th edition 2009.pdf
New Folder/Mastering the Trade - Proven Techniques for Profiting from Intraday and Swing Trading Setups 2nd edition 2012 (1) - annotated.pdf
Reminiscences of a Stock Operator 2008.pdf
The Little Book of Common Sense Investing - The Only Way to Guarantee Your Fair Share of Stock Market Returns 2007.pdf
Trade Your Way to Financial Freedom 2nd edition 2006.pdf
When Genius Failed - The Rise and Fall of Long-Term Capital Management 2001.pdf

Evidence-Based Technical Analysis and Trade Your Way to Financial Freedom were previously quarantined after OOM failures on the old host. The original quarantine entries remain unchanged; this is a separately tracked, resource-limited attempt, not a clearing of their historical status.

## New host-only run

Runner: /home/ubuntu/gnidart/resume_remaining.py
Environment: /home/ubuntu/gnidart/.venv-docling (Python 3.12, Docling 2.121.0, CPU-only torch).
Queue: /home/ubuntu/gnidart/output/remaining-host/queue.json
Checkpoint: /home/ubuntu/gnidart/output/remaining-host/manifest.json
Outputs: /home/ubuntu/gnidart/output/remaining-host/<stem>--pdf--<source-hash-prefix>/
Per-source logs: conversion.log inside each output directory.

Unit: gnidart-remaining.service in ubuntu's systemd user manager. It runs directly on the host, independently of this chat, not in a container or remote conversion service. MemoryMax=6G, CPUQuota=150%, Nice=10, OOMPolicy=stop, Restart=no. One converter process at a time. CPU, FAST table extraction, RapidOCR, page batch size one, two threads, image placeholders. HF_HUB_OFFLINE=1; model assets were downloaded during local environment testing, and PDF content is not sent to remote services.

Queue construction uses completed SHA256 hashes rather than shared stems. Original completed files are excluded, exact duplicates are excluded, outputs are collision-safe. Checkpoints are atomic. Completed new outputs resume without reprocessing. Every success requires non-empty Markdown, valid structured JSON, and JSON page count equal to source PDF page count. The batch stops on the first conversion/validation failure; there are no unattended retries. An OOM stops the unit; inspect systemd Result and logs before deciding how to proceed.

Verification: three automated tests pass (hash-based queue/collision handling, local CLI options, failed-conversion checkpointing/original preservation). A real two-page smoke conversion of A Complete Guide To Volume Price Analysis 2013.pdf succeeded, with 3,747-byte Markdown and 16,276-byte JSON covering pages 1 and 2. Smoke files are isolated in output/remaining-host-smoke and are not full-book completion artifacts.

At 02:29 UTC the live unit was active/running with main PID 910549 and converter child PID 910555. The first full PDF was processing, memory approximately 1.9 GB in the unit. Ten files were queued; one running, none yet recorded complete. This report does not claim full-batch completion.

Check live status:

systemctl --user status gnidart-remaining.service
journalctl --user -u gnidart-remaining.service --no-pager

Do not rerun process_docs.py or healthcheck.sh for this queue: their stem-based resume skips the missing variants, and the old monitor starts extra agentic work.
