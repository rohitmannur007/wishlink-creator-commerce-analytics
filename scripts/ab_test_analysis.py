#!/usr/bin/env python3
"""
Simple A/B analysis using counts exported from SQL.
Usage:
  Create data/ab_test_counts.csv with columns: variant, views, purchases
  Then run:
  python3 scripts/ab_test_analysis.py
"""
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from pathlib import Path

FILE = Path(__file__).parents[1] / "data" / "ab_test_counts.csv"

def main():
    if not FILE.exists():
        print("Place ab_test_counts.csv in data/ with columns: variant,views,purchases")
        return
    df = pd.read_csv(FILE)
    counts = df['purchases'].values
    nobs = df['views'].values
    stat, pval = proportions_ztest(counts, nobs)
    conv = counts / nobs
    uplift = (conv[1] - conv[0]) / conv[0] * 100
    print("Variants:", df['variant'].tolist())
    print("Conversions:", conv)
    print("z-stat:", stat, "p-value:", pval)
    print("Relative uplift (A->B) %:", round(uplift,2))

if __name__ == "__main__":
    main()
