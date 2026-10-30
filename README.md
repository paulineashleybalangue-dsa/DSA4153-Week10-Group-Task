# DSA4153 Week 10 Group Project — Four-Format Data Recovery

## Project Overview
This project demonstrates the recovery, validation, analysis, and export of a historical Gapminder dataset supplied in four different formats: CSV, XLSX, nested JSON, and Parquet.

The system processes each format independently, validates the records, quarantines invalid observations, removes exact duplicates, and detects conflicting (country, year) keys. It then verifies agreement across the four formats before performing pandas and NumPy analyses and exporting the resulting datasets.

The input observations cover 1952–2007. These are historical data, not current conditions. The supplied defects are classroom fixtures and are not errors attributed to the original Gapminder source.

## Project Objectives
- Read and process data from four different file formats.
- Validate records and quarantine invalid observations.
- Identify and remove exact duplicate records.
- Detect conflicting (country, year) keys.
- Verify consistency across all four input formats.
- Perform data analysis using pandas and NumPy.
- Export the canonical dataset into multiple formats and verify the exported results.

## Team Ownership 
| Member | Git identity | Responsibility |
|---|---|---|
| Pauline Ashley Balangue | paulineashley.balangue@ust.edu.ph | Four-format data loading, configuration, reader tests |
| Mary Belle Cubol | bellecubol16@gmail.com | Data validation, quarantine, validation tests |
| Meghan Isabelle Espiritu | meghanisabelle.espiritu@ust.edu.ph | Duplicate removal, conflict detection, recovery tests |
| Mikaela Stefanie Tilo | mikaelastefanie.tilo@ust.edu.ph | pandas analysis, NumPy matrix, calculation tests |
| Coleen Dian Fernandez | coleendian.fernandez@ust.edu.ph | Exports, round-trip verification, auditing, export tests |
| Rolando Banjo Alano | rolandobanjo.alano@ust.edu.ph | Main program integration, documentation, reports, test results, submission coordination |

## Repository Structure
- main.py — Main command-line program and orchestration.
- config.json — Input/output paths, reporting year, and comparison tolerances.
- data/raw/ — Original supplied input files and manifest. Preserve their original contents.
- src/ — Reusable data loading, validation, recovery, analysis, export, and audit modules.
- tests/ — Automated tests for the project's functions and processing steps.
- outputs/ — Generated datasets, analysis results, validation records, and reports.
- notebooks/report.ipynb — Notebook demonstrating the project code.
- notebooks/report.html — HTML export of the notebook.
- contributions.csv — Record of individual member contributions.
- reviews.md — Documentation of code reviews.
- submission_manifest.txt — Final submission information.

## Setup
Use Python 3.10+ (or a version compatible with the installed dependencies).

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Program
From the repository root:

```bash
python main.py --config config.json
```

The default reporting year is 2007. To change it to 1997, edit `"reporting_year": 1997` in `config.json` and rerun. Processing functions do not need to be edited.

The program stages generated files and only promotes them to `outputs/` after recovery, cross-format agreement, and export round-trip checks pass. A failed run returns a nonzero exit code and writes `outputs/validation_failed.csv` without replacing a previously successful output set.

## Run Tests

```bash
python -m pytest -v
```

Tests cover normal format reading, schema failures, missing files, invalid numeric values, non-finite and fractional values, invalid domains, duplicates, conflicting keys, reordered rows, analysis controls, export round trips, and corrupted exports.

## Expected Results
For each normal input format:

1,712 raw records = 6 quarantined records + 2 exact duplicate copies removed + 1,704 canonical records.

Across all four formats, the expected reconciliation is:

| Measure | Expected result |
|---|---:|
| Quarantined records | 24 |
| Duplicate copies removed | 8 |
| Canonical observations | 1,704 |

The four input formats represent the same observations. They must agree and must not be concatenated into 6,816 observations.

For the default 2007 analysis, the expected control values are:
- Asian rows: 33
- Asian population total: 3,811,953,827
- Philippine population: 91,077,287

## Generated Outputs
The `outputs/` directory should contain:

**Canonical datasets**
- canonical.csv
- canonical.xlsx — sheet: observations
- canonical.json — records orientation
- canonical.parquet
**Analysis results**
- asia_selected_year.csv
- country_history.csv
- population_index.csv**
**Validation and audit records**
- quarantine.csv
- duplicate_log.csv
- validation.csv
- audit_log.csv
**Test results**
- test_results.txt
The final ZIP must also include the supplied `data/` folder, source code, tests, notebook and HTML export, contribution/review evidence, and submission manifest.

## Git Collaboration and Submission
The project uses individual member branches to organize contributions. Each member is expected to contribute a processing function or method and an automated test.

The group collaboration process includes:

1. Creating and working on individual member branches.
2. Committing completed code and tests.
3. Submitting pull requests for review.
4. Recording reviewed commits, feedback, and responses in `reviews.md`.
5. Merging reviewed contributions while preserving individual commit history.
6. Performing a fresh-clone verification before submission.

The submitted version should be tagged `week10-v1.0`. Its full commit hash and repository URL must be recorded in `submission_manifest.txt`.

The `outputs/` directory is ignored by Git by default, so generated deliverables must be included separately in the final group ZIP.