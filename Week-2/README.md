# Week 2 — Robust Log Analyzer

A beginner-friendly Python script that reads a log file safely and prints a summary of log levels.
It is designed to **not crash** and to handle common user mistakes (missing file, empty file, wrong input).

## What it does
- Asks the user for a log filename (example: `log.txt`)
- If the file is missing:
- Shows a friendly message
- Asks if you want to create the file
- If the file is empty:
- Shows a friendly message and exits safely
- Reads the file and counts lines that contain:
- `ERROR`
- `WARNING`
- `INFO`
- `OTHER` (anything else)
- If `OTHER` is 0, prints a friendly message
- Saves the summary into `summary_report.txt`
- Asks if you want to analyze another file (Y/N validation)

## How to run
From the folder where the script exists:

```bash
python robust_log_analyzer.py
