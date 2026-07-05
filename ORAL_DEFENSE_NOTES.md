# Oral Defense Notes

## One-minute explanation

I evaluated a 2016 tutorial that uses a decision tree to classify phishing websites from 30 engineered indicators. I first reproduced the author's code, then audited the data and evaluation. I found that the current CSV has 11,055 rows although the tutorial says 2,456, so the code tests on 9,055 rows instead of 456. I also found that the tutorial reverses the UCI label meanings; the correct convention is -1 phishing and +1 legitimate. The raw dataset contains many duplicate rows and 64 identical feature vectors with contradictory labels. My primary experiment therefore uses one consistently labeled row per unique feature vector. I compared Logistic Regression, Decision Tree, and Random Forest with stratified holdout testing and five-fold cross-validation. Random Forest was strongest, but I concluded that the tutorial is not ready for real deployment because there are no timestamps, raw URLs, campaign IDs, external validation, or complete feature-extraction code.

## Numbers to remember

- Raw rows: 11,055
- Predictors: 30
- Exact duplicate repetitions: 5,206
- Contradictory feature-vector groups: 64
- Primary cleaned rows: 5,721
- Raw phishing prevalence: about 44.3%
- Clean phishing prevalence: about 51.7%
- Original current-file test size: 9,055
- Random Forest holdout F1: about 0.97
- Random Forest 5-fold CV F1: about 0.96

## Important conceptual answers

**Why Spearman?** The predictors are discrete ordered indicators; Spearman measures monotonic rank association without requiring normal continuous data.

**Why not z-score outliers?** The values are bounded at -1, 0, and 1. Invalid categories, rare values, duplicates, and contradictions are the meaningful quality checks.

**Why is a false negative serious?** A phishing site is treated as legitimate, so a user may disclose credentials or payment information.

**Why use F2?** It weights recall more heavily, reflecting the higher cost of missed phishing pages.

**Why is accuracy insufficient?** It hides which class is missed and can remain high when one class dominates.

**Why no temporal split?** The dataset has no timestamps. This is a limitation, not a choice; future work needs recent time-stamped data.

**Would I deploy it?** No. I would use it only as a baseline for a redesigned, time-aware, externally validated system.
