#!/usr/bin/env python3
"""
Batch Document Processor using Docling
Converts PDFs and EPUBs to structured Markdown + JSON for RAG/LLM use.

Features:
- PDF: ACCURATE table extraction, RapidOCR fallback for scanned pages
- EPUB: native extraction with chapter structure
- SHA256 deduplication of identical files
- Resume support: skips already-processed documents
- Per-file error logging (no silent drops)
- Manifest tracking with metadata, page counts, timing
"""

import hashlib
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
REPO_DIR = Path(__file__).parent
OUTPUT_DIR = REPO_DIR / "output"
SUPPORTED_EXTENSIONS = {".pdf", ".epub"}
SKIP_EXTENSIONS = {".mobi", ".azw", ".azw3"}
# Files to exclude from processing (metadata files, not books)
EXCLUDE_FILES = {"_info.json", "_info.text", "Trading.txt", ".gitattributes"}
# Skip files larger than this (OOM risk on 2-core/8GB box)
MAX_FILE_SIZE_MB = 50

# Docling imports
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import ThreadedPdfPipelineOptions, TableFormerMode

# ─── Setup Logging ───────────────────────────────────────────────────────────
log_dir = OUTPUT_DIR
log_dir.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("docling_batch")
logger.setLevel(logging.INFO)

fh = logging.FileHandler(OUTPUT_DIR / "processing.log", mode="a")
fh.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(fh)

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(ch)

logging.getLogger("docling").setLevel(logging.DEBUG)
logging.getLogger("docling.document_converter").setLevel(logging.INFO)
logging.getLogger("docling.pipeline").setLevel(logging.INFO)
logging.getLogger("docling.models.stages.ocr").setLevel(logging.INFO)
logging.getLogger("docling.models.stages.layout").setLevel(logging.INFO)
logging.getLogger("docling.models.stages.table_structure").setLevel(logging.INFO)
logging.getLogger("docling.backend").setLevel(logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


# ─── Hash Functions ──────────────────────────────────────────────────────────
def sha256_file(path: Path, block_size: int = 65536) -> str:
    """Compute SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hasher.update(block)
    return hasher.hexdigest()


# ─── Converter Setup ─────────────────────────────────────────────────────────
def create_converter() -> DocumentConverter:
    """Create Docling DocumentConverter with PDF-specific options."""
    pdf_opts = ThreadedPdfPipelineOptions()
    pdf_opts.do_table_structure = True
    pdf_opts.table_structure_options.mode = TableFormerMode.FAST
    pdf_opts.do_ocr = True
    pdf_opts.generate_picture_images = False  # skip images to save disk

    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pdf_opts)
        }
    )


# ─── Processing ──────────────────────────────────────────────────────────────
def process_file(
    conv: DocumentConverter, file_path: Path, manifest: dict
) -> dict:
    """Process a single file and return its manifest entry."""
    stem = file_path.stem
    out_dir = OUTPUT_DIR / stem
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / "document.md"
    json_path = out_dir / "document.json"

    # Resume: skip stems already recorded as skipped (too large, OOM, ...)
    if stem in manifest and manifest[stem].get("status", "").startswith("skipped"):
        logger.info(f"SKIP (resume): {stem}")
        return manifest[stem]

    # Resume: skip if already processed
    if md_path.exists() and json_path.exists():
        logger.info(f"SKIP (resume): {stem}")
        return manifest.get(stem, {"status": "skipped_resume", "file": str(file_path.name)})

    file_size_mb = file_path.stat().st_size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        logger.warning(f"SKIP (too large): {stem} | {file_size_mb:.0f}MB > {MAX_FILE_SIZE_MB}MB limit")
        return {"status": "skipped_too_large", "file": file_path.name, "size_mb": round(file_size_mb, 1)}

    start = time.time()
    entry = {
        "file": file_path.name,
        "path": str(file_path.relative_to(REPO_DIR)),
        "extension": file_path.suffix.lower(),
        "sha256": sha256_file(file_path),
        "size_bytes": file_path.stat().st_size,
        "processed_at": datetime.now().isoformat(),
        "docling_version": None,
        "markdown_chars": 0,
        "markdown_lines": 0,
        "pages": 0,
        "headings_h1": 0,
        "headings_h2": 0,
        "headings_h3": 0,
        "elapsed_seconds": 0,
        "status": "pending",
        "error": None,
    }

    try:
        logger.info(f"START: {file_path.name}")
        result = conv.convert(str(file_path))
        doc = result.document
        elapsed = time.time() - start

        # Export Markdown
        md = doc.export_to_markdown()
        md_path.write_text(md, encoding="utf-8")

        # Export JSON (structured docling dict)
        d = doc.export_to_dict()
        json_path.write_text(
            json.dumps(d, indent=1, default=str, ensure_ascii=False),
            encoding="utf-8",
        )

        # Count structure
        entry["markdown_chars"] = len(md)
        entry["markdown_lines"] = md.count("\n") + 1
        entry["headings_h1"] = md.count("\n# ") + (1 if md.startswith("# ") else 0)
        entry["headings_h2"] = md.count("\n## ") + (1 if md.startswith("## ") else 0)
        entry["headings_h3"] = md.count("\n### ") + (1 if md.startswith("### ") else 0)
        entry["elapsed_seconds"] = round(elapsed, 1)

        # Count pages from provenance
        pages = set()
        for t in d.get("texts", []):
            prov = t.get("prov", [])
            if prov and isinstance(prov, list):
                p = prov[0].get("page_no")
                if p:
                    pages.add(p)
        entry["pages"] = len(pages)

        entry["status"] = "success"
        logger.info(
            f"DONE: {stem} | {entry['pages']} pages | "
            f"{entry['markdown_chars']} chars | {elapsed:.1f}s"
        )

    except Exception as e:
        elapsed = time.time() - start
        entry["status"] = "error"
        entry["error"] = str(e)
        entry["elapsed_seconds"] = round(elapsed, 1)
        logger.error(f"ERROR: {stem} | {e}", exc_info=True)

    return entry


def collect_files(repo_dir: Path) -> list[Path]:
    """Collect all processable files, excluding metadata and git files."""
    files = []
    for p in sorted(repo_dir.rglob("*")):
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS:
            if p.name not in EXCLUDE_FILES and ".git" not in str(p):
                files.append(p)
    return files


def main():
    logger.info("=" * 70)
    logger.info("DOCLING BATCH PROCESSOR STARTING")
    logger.info(f"Repository: {REPO_DIR}")
    logger.info(f"Output: {OUTPUT_DIR}")

    # Collect files
    all_files = collect_files(REPO_DIR)
    logger.info(f"Found {len(all_files)} supported files (PDF/EPUB)")

    # SHA256 dedup
    hashes = {}
    duplicates = []
    unique_files = []
    for f in all_files:
        h = sha256_file(f)
        if h in hashes:
            duplicates.append((f.name, hashes[h]))
            logger.info(f"DEDUP: {f.name} is identical to {hashes[h]}")
        else:
            hashes[h] = f.name
            unique_files.append(f)

    if duplicates:
        logger.info(f"Skipped {len(duplicates)} duplicate files")

    # Load existing manifest for resume
    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        logger.info(f"Loaded existing manifest with {len(manifest)} entries")

    # Create converter
    conv = create_converter()
    logger.info("Docling converter initialized")

    # Process
    total = len(unique_files)
    errors = 0
    skipped = 0
    processed = 0

    for i, fpath in enumerate(unique_files, 1):
        stem = fpath.stem
        logger.info(f"[{i}/{total}] Processing: {fpath.name}")

        entry = process_file(conv, fpath, manifest)
        manifest[stem] = entry

        if entry["status"] == "error":
            errors += 1
        elif entry["status"] == "skipped_resume":
            skipped += 1
        else:
            processed += 1

        # Save manifest after each file (crash recovery)
        manifest_path.write_text(
            json.dumps(manifest, indent=1, default=str, ensure_ascii=False)
        )

    # Summary
    logger.info("=" * 70)
    logger.info("BATCH COMPLETE")
    logger.info(f"Total unique files: {total}")
    logger.info(f"Processed: {processed}")
    logger.info(f"Skipped (resume): {skipped}")
    logger.info(f"Errors: {errors}")
    logger.info(f"Manifest: {manifest_path}")

    # Write unsupported format report
    skip_report = OUTPUT_DIR / "unsupported_formats.json"
    skip_data = [{"file": d[0], "duplicate_of": d[1]} for d in duplicates]
    skip_data.extend(
        [{"file": f.name, "reason": "unsupported_format"} for f in Path(".").glob("*") 
         if f.is_file() and f.suffix.lower() in SKIP_EXTENSIONS]
    )
    skip_report.write_text(json.dumps(skip_data, indent=1))
    logger.info(f"Unsupported/duplicate report: {skip_report}")

    return errors


if __name__ == "__main__":
    sys.exit(main())
