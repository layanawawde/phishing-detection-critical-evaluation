# Critical Reproduction of a Phishing Website Detection Tutorial

**Student:** Layan Awawde  
**Course:** Data Science in Cybersecurity

## Project description

This project critically reproduces and evaluates a phishing-website classification tutorial. It checks the author's 90.5% accuracy claim, audits target semantics and dataset documentation, analyzes duplicates and contradictory labels, performs EDA and feature engineering, compares three classifiers, and studies cybersecurity-relevant false-positive/false-negative trade-offs.

## Selected source

- **Blog post:** Nicolas Papernot, “Detecting phishing websites using a decision tree”  
  https://medium.com/@NicolasPapernot/detecting-phishing-websites-using-a-decision-tree-ed069d073723
- **Original GitHub repository:**  
  https://github.com/npapernot/phishing-detection

## Dataset

- UCI Machine Learning Repository: **Phishing Websites**
- DOI: https://doi.org/10.24432/C51W2X
- License: CC BY 4.0
- Local file: `data/dataset.csv`, copied from the selected source repository.

## Important audit findings

1. The tutorial says the dataset has 2,456 websites, but the current CSV has 11,055 rows.
2. Its code trains on the first 2,000 rows and tests on every remaining row, so the current test set has 9,055 rows, not 456.
3. The tutorial prose reverses the established UCI target meanings. This project uses `Result = -1` as phishing and `Result = 1` as legitimate.
4. The raw file contains 5,206 repeated exact rows and 64 unique feature vectors with contradictory labels.
5. The original repository does not include the raw URL collection or complete feature-extraction pipeline.

## Repository structure

- `data/dataset.csv` - source dataset
- `notebooks/phishing_detection_reproduction.ipynb` - fully executed analysis
- `report/Phishing_Detection_Critical_Evaluation.pdf` - final report
- `report/Phishing_Detection_Critical_Evaluation.docx` - editable report source
- `figures/` - notebook-generated figures
- `results/` - notebook-generated tables and predictions
- `src/` - reusable loading and evaluation helpers
- `ORAL_DEFENSE_NOTES.md` - short preparation notes

## Installation

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

Exact versions verified in GitHub Codespaces are listed in `requirements-verified.txt`.

## Execute the notebook

From the repository root:

```bash
python -m jupyter nbconvert \
  --to notebook \
  --execute notebooks/phishing_detection_reproduction.ipynb \
  --output phishing_detection_reproduction_verified.ipynb \
  --ExecutePreprocessor.timeout=900
```

The notebook also works interactively in Jupyter or VS Code. It automatically locates the repository root whether launched from the root or the `notebooks/` directory.

## Main conclusion

The source's 90.5% claim is approximately reproducible only under the current repository file and its unintended 9,055-row test behavior. The tutorial is a useful educational baseline, but its documentation, target semantics, evaluation design, and missing data-generation pipeline do not support production deployment claims.
