# Number Analyzer — Python CLI Tool

A simple Python command-line tool that reads numbers from a text file, skips invalid lines, computes basic statistics, and writes a summary report.

This project demonstrates clean Python structure, file handling, error handling, and CLI argument usage with `argparse`.

---

## Features
- Read numbers from a `.txt` file (one per line)
- Skip invalid or empty lines safely
- Compute:
- Count
- Sum
- Minimum
- Maximum
- Average
- Write results to an output file
- Command-line interface (CLI)
- Optional quiet mode

---

## Project Structure
week-3/

├─ src/

│  └─ number_analyzer.py

├─ samples/

│  └─ data.txt

├─ output/

├─ learning/

│  └─ (archived practice files)

└─ README.md

---

## Requirements
- Python 3.10+

---

## Usage

-Run from the project root.

### Basic run
```bash
-py src/number_analyzer.py --in samples/data.txt --out output/summary.txt
## Quiet mode
-py src/number_analyzer.py --in samples/data.txt --out output/summary.txt --quiet

## Sample Output
Count: 5
Sum: 150
Min: 10
Max: 50
Average: 30.0
Skipped lines: 0


## Notes
-Non-numeric lines are skipped automatically

-Designed as a clean, beginner-to-intermediate Python CLI project

## Future Improvements
-Support floating-point numbers

-Add unit tests

-Package as an installable CLI tool





