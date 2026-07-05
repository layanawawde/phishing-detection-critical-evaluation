"""Dataset loading and quality-control helpers."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

FEATURE_NAMES = [
    "having_IP_Address", "URL_Length", "Shortining_Service", "having_At_Symbol",
    "double_slash_redirecting", "Prefix_Suffix", "having_Sub_Domain", "SSLfinal_State",
    "Domain_registeration_length", "Favicon", "port", "HTTPS_token", "Request_URL",
    "URL_of_Anchor", "Links_in_tags", "SFH", "Submitting_to_email", "Abnormal_URL",
    "Redirect", "on_mouseover", "RightClick", "popUpWidnow", "Iframe", "age_of_domain",
    "DNSRecord", "web_traffic", "Page_Rank", "Google_Index", "Links_pointing_to_page",
    "Statistical_report",
]


def load_dataset(path: Path) -> pd.DataFrame:
    """Load the headerless source CSV and add a phishing-positive target."""
    data = pd.read_csv(path, header=None, names=FEATURE_NAMES + ["Result"])
    # UCI convention: -1 = phishing, +1 = legitimate.
    data["phishing"] = (data["Result"] == -1).astype(int)
    return data


def unique_consistent_feature_vectors(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Keep one row per feature vector and separate contradictory-label groups."""
    grouped = (
        data.groupby(FEATURE_NAMES, dropna=False)["Result"]
        .agg(label_count="nunique", rows_in_group="size", Result="first")
        .reset_index()
    )
    conflicts = grouped[grouped["label_count"] > 1].copy()
    clean = grouped[grouped["label_count"] == 1].copy()
    clean = clean[FEATURE_NAMES + ["Result"]]
    clean["phishing"] = (clean["Result"] == -1).astype(int)
    return clean.reset_index(drop=True), conflicts.reset_index(drop=True)
