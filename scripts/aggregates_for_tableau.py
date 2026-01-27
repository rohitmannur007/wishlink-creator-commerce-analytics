#!/usr/bin/env python3
"""
Exports pre-aggregated CSVs ready for Tableau.
Usage:
    python3 scripts/aggregates_for_tableau.py
"""
import sqlite3
import pandas as pd
from pathlib import Path

DB = Path(__file__).parents[1] / "data" / "wishlink.db"
OUT = Path(__file__).parents[1] / "data"

conn = sqlite3.connect(DB)

# 1) Creator leaderboard
sql_leaderboard = """
SELECT
  creator_id,
  SUM(is_view) AS views,
  SUM(is_click) AS clicks,
  SUM(is_add_to_cart) AS adds,
  SUM(is_purchase) AS purchases,
  SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv,
  MAX(followers) AS followers
FROM events
GROUP BY creator_id
ORDER BY gmv DESC;
"""
df_leader = pd.read_sql(sql_leaderboard, conn)
df_leader['conv_pct'] = (df_leader['purchases'] / df_leader['views'].replace(0, pd.NA) * 100).fillna(0).round(3)
df_leader.to_csv(OUT / "tableau_creator_leaderboard.csv", index=False)

# 2) Funnel snapshot (single-row)
sql_funnel = """
SELECT
  SUM(is_view) AS views,
  SUM(is_click) AS clicks,
  SUM(is_add_to_cart) AS adds,
  SUM(is_purchase) AS purchases,
  SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv
FROM events;
"""
pd.read_sql(sql_funnel, conn).to_csv(OUT / "tableau_funnel_snapshot.csv", index=False)

# 3) Creator x Category lift
sql_creator_cat = """
WITH cat AS (
  SELECT category,
         SUM(is_view) AS cat_views,
         SUM(is_purchase) AS cat_purchases
  FROM events
  GROUP BY category
),
creator_cat AS (
  SELECT creator_id, category,
         SUM(is_view) AS views,
         SUM(is_purchase) AS purchases,
         SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv
  FROM events
  GROUP BY creator_id, category
)
SELECT cc.creator_id, cc.category, cc.views, cc.purchases, cc.gmv,
       ROUND(100.0 * cc.purchases / NULLIF(cc.views,0),3) AS conv_pct,
       ROUND(100.0 * c.cat_purchases / NULLIF(c.cat_views,0),3) AS cat_conv_pct,
       CASE WHEN c.cat_purchases=0 THEN NULL ELSE ROUND((cc.purchases*1.0/NULLIF(cc.views,0)) / (c.cat_purchases*1.0/NULLIF(c.cat_views,0)),3) END AS lift
FROM creator_cat cc
JOIN cat c ON cc.category = c.category
ORDER BY lift DESC;
"""
df_cc = pd.read_sql(sql_creator_cat, conn)
df_cc.to_csv(OUT / "tableau_creator_category_lift.csv", index=False)

# 4) Daily time series
sql_daily = """
SELECT DATE(event_time) AS day,
       SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv,
       SUM(is_view) AS views,
       SUM(is_purchase) AS purchases
FROM events
GROUP BY day
ORDER BY day;
"""
pd.read_sql(sql_daily, conn).to_csv(OUT / "tableau_daily_timeseries.csv", index=False)

# 5) Cohort
sql_cohort = """
WITH first_event AS (
  SELECT user_id, DATE(MIN(event_time)) AS signup_date
  FROM events
  GROUP BY user_id
),
purchases AS (
  SELECT user_id, DATE(event_time) AS event_date
  FROM events
  WHERE is_purchase=1
)
SELECT fe.signup_date,
       CAST(julianday(p.event_date) - julianday(fe.signup_date) AS INTEGER) AS days_since_signup,
       COUNT(DISTINCT p.user_id) AS purchasers
FROM first_event fe
LEFT JOIN purchases p ON p.user_id = fe.user_id AND p.event_date >= fe.signup_date
GROUP BY fe.signup_date, days_since_signup
ORDER BY fe.signup_date, days_since_signup;
"""
pd.read_sql(sql_cohort, conn).to_csv(OUT / "tableau_cohort.csv", index=False)

conn.close()
print("Exported CSVs for Tableau to:", OUT)
