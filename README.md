# Critical Reproduction of a Phishing Website Detection Tutorial

Student: Layan Awawde

## Project description
This project critically reproduces and evaluates Nicolas Papernot's tutorial, "Detecting phishing websites using a decision tree." The original tutorial reports about 90.5% accuracy. This project verifies that claim, audits the data, compares three models, examines duplicates and redundancy, and evaluates cybersecurity-relevant errors.

## Selected source
- Tutorial and original repository: https://github.com/npapernot/phishing-detection
- Dataset source stated by the tutorial: UCI Phishing Websites dataset

## Repository structure
- `data/dataset.csv`: dataset copied from the original repository
- `notebooks/phishing_detection_reproduction.ipynb`: complete analysis notebook
- `report/Phishing_Detection_Critical_Evaluation.pdf`: final report
- `figures/`: generated visualizations
- `src/evaluate.py`: reusable metric helper

## Main reproducibility finding
The README describes 2,456 websites and a 456-row test set, but the current CSV contains 11,055 rows. The original code trains on the first 2,000 rows and therefore tests on 9,055 rows. The reported accuracy is approximately reproducible in magnitude, but not under the stated dataset description.

## Installation and execution
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/phishing_detection_reproduction.ipynb
```

Run the notebook from inside the `notebooks` directory, or adjust the relative data path.

## Requirements
Python 3.10+ is recommended.
