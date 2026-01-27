Slide 1 — Problem & Goal
- Problem: Which creators drive purchases & GMV on Wishlink?
- Goal: Build a reproducible pipeline to identify top creators, measure lift, and recommend product experiments to scale creator-driven revenue.

Slide 2 — Key Metrics & Findings
- KPIs: Views, Clicks, Purchases, Conversion %, GMV, AOV
- Top finding example: "Top 10 creators drive X% of purchases" (replace X with real number)
- Example lift: "Creator A shows 3.2× conversion lift for Dresses vs category average."

Slide 3 — Creator Prioritization
- Show table: Top 5 creators by GMV, conv%, followers
- Scoring (explain): conv_pct (50%) + gmv_per_1k_views (35%) + followers (15%)

Slide 4 — Product Experiments
- Exp1: Pin top creators on category pages (Randomized)
  - Primary metric: Purchases per 1k category impressions
  - Guardrails: Bounce rate, checkout errors
- Exp2: Creator Badge on Product Page
- Exp3: Personalized creator feed pilot

Slide 5 — Next Steps & Operationalization
- Daily ETL -> update materialized view and CSVs
- Weekly report emailed + Slack alert for new top creators
- Run prioritized A/B test and iterate
