#!/usr/bin/env python3
"""
Load cleaned_wishlink.csv into a local SQLite DB and create normalized events table.
Usage:
    python3 scripts/load_to_sqlite.py
"""
import sqlite3
import pandas as pd
from pathlib import Path
import sys

CLEANED = Path(__file__).parents[1] / "data" / "cleaned_wishlink.csv"
DB = Path(__file__).parents[1] / "data" / "wishlink.db"

def main():
    if not CLEANED.exists():
        print("Missing cleaned file at", CLEANED)
        sys.exit(1)
    df = pd.read_csv(CLEANED, low_memory=False)
    # ensure columns exist
    cols = [c.strip().lower().replace(' ', '_') for c in df.columns]
    df.columns = cols
    # canonical columns
    required = ['user_id','product_id','creator_id','event_time','event_type','price','category','followers_clean','is_view','is_click','is_add_to_cart','is_purchase']
    for r in required:
        if r not in df.columns:
            df[r] = pd.NA
    # cast event_time to string for sqlite; we will use ISO format
    df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')
    # safe dtypes
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
    df['followers_clean'] = pd.to_numeric(df['followers_clean'], errors='coerce').fillna(0).astype(int)
    # write to sqlite
    conn = sqlite3.connect(DB)
    df.to_sql('events_raw', conn, if_exists='replace', index=False)
    # create events table with only columns we need (normalized)
    conn.executescript("""
    DROP TABLE IF EXISTS events;
    CREATE TABLE events AS
    SELECT user_id, product_id, creator_id, event_time, event_type, price, category, followers_clean AS followers,
           is_view, is_click, is_add_to_cart, is_purchase
    FROM events_raw;
    """)
    conn.commit()
    conn.close()
    print("Loaded events into", DB)

if __name__ == "__main__":
    main()
