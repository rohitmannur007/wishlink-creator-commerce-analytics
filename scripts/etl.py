#!/usr/bin/env python3
"""
scripts/etl.py
Cleans raw wishlink CSV and writes cleaned_wishlink.csv
Usage:
    python3 scripts/etl.py --input data/wishlink_raw.csv --out data/cleaned_wishlink.csv
"""
import argparse
import pandas as pd
import numpy as np
import re

def parse_followers(x):
    if pd.isna(x):
        return 0
    s = str(x).strip().lower().replace(',', '')
    if s in ['', 'nan', 'none']:
        return 0
    try:
        if s.endswith('k'):
            return int(float(s[:-1]) * 1000)
        if s.endswith('m'):
            return int(float(s[:-1]) * 1_000_000)
        return int(float(s))
    except:
        digits = ''.join(ch for ch in s if ch.isdigit() or ch=='.')
        try:
            return int(float(digits))
        except:
            return 0

def parse_price(x):
    if pd.isna(x):
        return 0.0
    s = str(x).strip().replace(',', '').replace('₹','').replace('$','').replace('INR','')
    allowed = ''.join(ch for ch in s if ch.isdigit() or ch=='.' or ch=='-')
    try:
        return float(allowed) if allowed not in ['', '-', '.', '-.'] else 0.0
    except:
        return 0.0

def normalize(df):
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # ensure common fields exist
    expected = ['user_id','product_id','creator_id','event_time','event_type','price','category','followers']
    for c in expected:
        if c not in df.columns:
            df[c] = pd.NA
    # parse datetimes/fields
    df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')
    df['price'] = df['price'].apply(parse_price)
    # unify followers column name, create followers_clean
    candidate = None
    for col in df.columns:
        if 'follow' in col:
            candidate = col
            break
    if candidate:
        df['followers_raw'] = df[candidate]
    else:
        df['followers_raw'] = df.get('followers', pd.NA)
    df['followers_clean'] = df['followers_raw'].apply(parse_followers)
    # normalize ids and types
    df['creator_id'] = df['creator_id'].fillna('-1').astype(str)
    df['product_id'] = df['product_id'].fillna('-1').astype(str)
    df['user_id'] = df['user_id'].fillna('-1').astype(str)
    df['event_type'] = df['event_type'].astype(str).str.lower().str.strip()
    # create event flags
    df['is_view'] = df['event_type'].isin(['view','impression','page_view','impressions']).astype(int)
    df['is_click'] = df['event_type'].isin(['click','clicked']).astype(int)
    df['is_add_to_cart'] = df['event_type'].isin(['add_to_cart','add','addtocart']).astype(int)
    df['is_purchase'] = df['event_type'].isin(['purchase','order','buy','checkout']).astype(int)
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--out', default='data/cleaned_wishlink.csv')
    args = parser.parse_args()
    df = pd.read_csv(args.input, low_memory=False)
    df = normalize(df)
    df.to_csv(args.out, index=False)
    print(f"Saved cleaned dataset to {args.out}")

if __name__ == '__main__':
    main()
