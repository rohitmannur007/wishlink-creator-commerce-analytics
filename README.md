# Wishlink Creator Commerce Analytics


> An end-to-end data analytics pipeline analyzing 50 creators across 12 product categories on the Wishlink platform for the full year 2023. Built to demonstrate SQL, Python (ETL), and data visualization skills aligned with Wishlink's Product Analyst role.

---

## 🔗 Live Links

| Resource | Link |
|---|---|
| 🌐 Interactive HTML Dashboard | [rohitmannur007.github.io/wishlink-creator-commerce-analytics-dashbord](https://rohitmannur007.github.io/wishlink-creator-commerce-analytics-dashbord/) |
| 📊 Tableau Dashboard | [View on Tableau Public](https://public.tableau.com/app/profile/rohit.mannur3130/viz/Creator-DrivenCommerceAnalyticsWishlinkRohitMannur/WishlinkProductPerformanceDashboard?publish=yes) |
| 💻 GitHub Repository | [github.com/rohitmannur007](https://github.com/rohitmannur007) |

---

## 📌 Project Overview

Wishlink is a creator-driven commerce platform where influencers curate product wishlists and drive purchases. This project builds a full analytics pipeline to answer one core business question:

> **Which creators drive the most value, and how can Wishlink scale creator-led revenue?**

To answer this, I designed and built:
- A **Python ETL pipeline** to clean and transform raw transaction data
- **SQL queries** for aggregating KPIs, segmenting creators, and computing conversion metrics
- An **interactive HTML dashboard** with 5 analytical panels (Overview, Leaderboard, Funnel, Cohort, Lift)
- A **Tableau dashboard** for executive-level visualization
- **A/B test proposals** grounded in the data findings

---

## 📁 Repository Structure
```
wishlink-creator-commerce-analytics/
│
├── data/
│   ├── cleaned_wishlink.csv              # Cleaned transaction-level data
│   ├── creator_leaderboard.csv           # Per-creator aggregated metrics
│   ├── tableau_daily_timeseries.csv      # Daily GMV, views, purchases
│   ├── tableau_creator_leaderboard.csv   # Creator KPIs for Tableau
│   ├── tableau_cohort.csv                # Monthly cohort retention data
│   ├── tableau_creator_category_lift.csv # Creator × category lift scores
│   └── tableau_funnel_snapshot.csv       # Platform-wide funnel summary
│
├── scripts/
│   ├── etl.py                            # Main ETL: cleans raw data, outputs CSVs
│   ├── aggregates_for_tableau.py         # Builds all Tableau-ready aggregates
│   ├── make_cohort.py                    # Generates monthly cohort retention table
│   ├── ab_test_analysis.py               # A/B test significance calculations
│   └── load_to_sqlite.py                 # Loads data into SQLite for SQL querying
│
├── sql/
│   └── queries.sql                       # All SQL queries used in analysis
│
├── slides/
│   └── slide_notes.md                    # Presentation outline and speaker notes
│
├── Wishlink Product Performance Dashboard.png   # Tableau dashboard screenshot
├── requirements.txt                             # Python dependencies
└── README.md                                    # This file
```

---

## 📊 Dashboard Panels — What Each One Shows

### 1. ⬡ Overview — Platform Performance
**KPIs tracked:** Total GMV (₹), Total Purchases, Conversion Rate, Average Order Value (AOV)

Key findings:
- **₹57,608** total GMV generated across 50 creators in 2023
- **238 purchases** completed with a **96.7% click-to-purchase rate** — exceptionally high for e-commerce
- **₹242 average order value** — healthy ticket size for influencer-driven commerce
- January was the strongest acquisition month; revenue shows consistent weekly activity through the year

---

### 2. ◈ Creator Leaderboard — Who Drives the Most Value
**Metrics:** GMV, Purchases, Views, Clicks, Followers, Conversion Rate (Conv%), GMV Share

Key findings:
- **Creator #29** ranks #1 by GMV (₹2,893) with a 166% conversion rate
- **Creator #28** shows the highest Conv% at **700%** — extremely efficient despite low view volume, signaling a highly engaged niche audience
- **Creator #31** also stands out at 600% Conv% — a micro-creator with outsized impact
- Top 10 creators drive **~60% of total platform GMV** — classic 80/20 concentration
- High Conv% with low followers = niche creator worth scaling; Low Conv% with high followers = audience–product mismatch

> **Analyst insight:** Follower count alone is a poor predictor of GMV. Conversion rate per view is a far stronger signal for creator ROI.

---

### 3. ⬟ Conversion Funnel — End-to-End Journey
**Stages tracked:** Views → Clicks → Purchases → GMV

Key findings:
- **264 views → 246 clicks → 238 purchases**
- **View-to-Click rate: 93.2%** — near-perfect content relevance
- **Click-to-Purchase rate: 96.7%** — users who click are almost certain to buy
- **Overall funnel efficiency: 90.2%** end-to-end
- The bottleneck is not conversion — it is **top-of-funnel volume (views)**

> **Analyst insight:** The platform does not have a conversion problem — it has a reach problem. The growth lever is driving more eyeballs to creator content, not optimizing the checkout flow.

---

### 4. ⊞ Cohort Retention — Long-Term Engagement
**Method:** Monthly cohort analysis tracking % of users active in each subsequent month

Key findings:
- **January 2023 cohort** is the largest at **81 users** — likely a campaign-driven spike
- Retention follows a standard decay curve: ~30% active at M0, dropping to ~7–12% by M3–M6
- Several cohorts show **rising retention at later months** (e.g., Feb cohort spikes at M5 and M10) — a signal of delayed re-engagement, possibly driven by seasonal demand or email re-activation
- **August cohort** shows the highest M0 rate (40%) despite the smallest size — highly engaged early adopters

> **Analyst insight:** Re-engagement spikes at months 5–6 suggest a natural repurchase cycle. This is the ideal window to trigger push notifications or email campaigns featuring the same creator's new wishlist drops.

---

### 5. ◬ Category Lift — Creator × Category Matching
**What is lift?** Lift = Creator's conversion rate ÷ Category average conversion rate. Lift > 1.0 = creator outperforms the category baseline.

Key findings:
- **Creator #15 × Toys: 3.31× lift** — the single highest-performing creator–category pairing
- **Creator #49 × Home: 3.14× lift** — strong for high-ticket home goods
- **Creator #9 × Food: 2.68× lift** — food category shows consistent above-baseline performance
- **Creator #43 × Fashion: 2.53× lift** — fashion creators show strong relevance signals
- 12 creator–category pairs show lift > 1.5×, making them strong candidates for pinning experiments

> **Analyst insight:** Lift is the core metric for creator–product page matching. Placing Creator #15 on the Toys category page is a near-zero-risk A/B test with strong prior evidence.

---

## 🧪 A/B Test Proposals

### Experiment 1: Creator Category Page Pinning
- **Hypothesis:** Displaying a high-lift creator's content on their best-fit category page increases purchases per 1,000 category impressions
- **Variant A (Control):** Default category page (no creator pinning)
- **Variant B (Treatment):** Top-lift creator featured prominently on category page
- **Primary metric:** Purchases per 1,000 category impressions
- **Guardrail metrics:** Bounce rate, page load time, checkout errors
- **Target pairs:** Creator #15 × Toys, Creator #49 × Home, Creator #9 × Food

---

### Experiment 2: Creator Badge on Product Page
- **Hypothesis:** Adding a "Recommended by [Creator]" badge on product pages increases add-to-cart rate for products promoted by high-lift creators
- **Variant A:** Product page without creator attribution
- **Variant B:** Product page with creator badge and link to their wishlist
- **Primary metric:** Add-to-cart rate
- **Guardrail metrics:** Return rate, average order value

---

### Experiment 3: Personalized Creator Feed
- **Hypothesis:** Showing users a feed ranked by creator–category lift score (vs. chronological) increases weekly active purchases
- **Variant A:** Chronological creator feed
- **Variant B:** Lift-score ranked feed (best-fit creators shown first)
- **Primary metric:** Purchases per weekly active user
- **Guardrail metrics:** Session length, creator page CTR

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Cleaning & ETL | Python 3, Pandas, NumPy |
| Database & Querying | SQLite, SQL |
| Cohort & Lift Analysis | Python (custom aggregation scripts) |
| Visualization (BI) | Tableau Public |
| Visualization (Web) | HTML, CSS, JavaScript, Chart.js |
| Version Control | Git, GitHub |
| Hosting | GitHub Pages |

---

## 🗄️ Key SQL Queries

### Top Creators by GMV
```sql
SELECT
    creator_id,
    SUM(gmv)          AS total_gmv,
    COUNT(*)          AS total_purchases,
    AVG(gmv)          AS avg_order_value,
    SUM(purchases) * 100.0 / NULLIF(SUM(views), 0) AS conv_pct
FROM cleaned_wishlink
GROUP BY creator_id
ORDER BY total_gmv DESC
LIMIT 10;
```

### Category Lift Score
```sql
WITH creator_conv AS (
    SELECT
        creator_id,
        category,
        SUM(purchases) * 100.0 / NULLIF(SUM(views), 0) AS creator_conv_pct
    FROM cleaned_wishlink
    GROUP BY creator_id, category
),
category_avg AS (
    SELECT
        category,
        SUM(purchases) * 100.0 / NULLIF(SUM(views), 0) AS cat_conv_pct
    FROM cleaned_wishlink
    GROUP BY category
)
SELECT
    c.creator_id,
    c.category,
    c.creator_conv_pct,
    a.cat_conv_pct,
    ROUND(c.creator_conv_pct / NULLIF(a.cat_conv_pct, 0), 3) AS lift
FROM creator_conv c
JOIN category_avg a ON c.category = a.category
WHERE c.creator_conv_pct IS NOT NULL
ORDER BY lift DESC;
```

### Monthly Cohort Retention
```sql
WITH first_purchase AS (
    SELECT
        creator_id AS user_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM cleaned_wishlink
    GROUP BY creator_id
),
activity AS (
    SELECT
        f.user_id,
        f.cohort_month,
        DATE_TRUNC('month', w.order_date) AS active_month,
        (EXTRACT(YEAR FROM w.order_date) - EXTRACT(YEAR FROM f.cohort_month)) * 12
        + (EXTRACT(MONTH FROM w.order_date) - EXTRACT(MONTH FROM f.cohort_month))
        AS month_number
    FROM cleaned_wishlink w
    JOIN first_purchase f ON w.creator_id = f.user_id
)
SELECT
    cohort_month,
    month_number,
    COUNT(DISTINCT user_id) AS active_users,
    COUNT(DISTINCT user_id) * 100.0 / MAX(COUNT(DISTINCT user_id)) OVER (PARTITION BY cohort_month) AS retention_pct
FROM activity
GROUP BY cohort_month, month_number
ORDER BY cohort_month, month_number;
```

---

## ▶️ How to Run Locally
```bash
# 1. Clone the repository
git clone https://github.com/rohitmannur007/wishlink-creator-commerce-analytics.git
cd wishlink-creator-commerce-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the ETL pipeline
python scripts/etl.py

# 4. Generate all Tableau-ready CSVs
python scripts/aggregates_for_tableau.py

# 5. Build cohort data
python scripts/make_cohort.py

# 6. Load into SQLite (optional, for SQL querying)
python scripts/load_to_sqlite.py

# 7. Open the dashboard
open index.html   # or double-click the HTML file
```

---

## 📝 Resume Bullets

- Built an end-to-end creator commerce analytics pipeline using **Python, SQL, and Tableau**, analyzing 50 creators across 12 categories to identify ₹57K+ GMV drivers and surface high-ROI creator–category pairings
- Engineered a **category lift metric** (creator conv% ÷ category baseline) to rank creator–product fit, identifying Creator #15 × Toys at 3.31× lift — directly informing a creator page-pinning A/B test proposal
- Achieved a **96.7% click-to-purchase conversion rate** across the platform funnel, diagnosing reach (views) as the primary growth lever rather than checkout optimization
- Designed **monthly cohort retention analysis** across 8 cohorts, identifying re-engagement spikes at months 5–6 as an opportunity for automated creator drop notification campaigns
- Deployed an **interactive HTML dashboard** on GitHub Pages with 5 drill-down panels, Chart.js visualizations, and recruiter-ready metric explanations

---

## 👤 About

**Rohit Mannur** — Aspiring Product Analyst with a focus on creator economics, e-commerce analytics, and data-driven experimentation.

- 🌐 Dashboard: [rohitmannur007.github.io/wishlink-creator-commerce-analytics-dashbord](https://rohitmannur007.github.io/wishlink-creator-commerce-analytics-dashbord/)
- 📊 Tableau: [View Dashboard](https://public.tableau.com/app/profile/rohit.mannur3130/viz/Creator-DrivenCommerceAnalyticsWishlinkRohitMannur/WishlinkProductPerformanceDashboard)
- 💻 GitHub: [github.com/rohitmannur007](https://github.com/rohitmannur007)

