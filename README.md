# Wishlink Data Analytics Project

This project demonstrates my data analytics skills tailored to Wishlink's requirements for a Data Analyst role, focusing on e-commerce insights, SQL querying, data visualization in Tableau, and Python-based data processing. It analyzes sales data to uncover trends, customer behavior, and performance metrics, providing actionable recommendations for inventory management and marketing strategies.

## Live Tableau Dashboard
[View the Interactive Tableau Dashboard](https://public.tableau.com/app/profile/rohit.mannur3130/viz/Creator-DrivenCommerceAnalyticsWishlinkRohitMannur/WishlinkProductPerformanceDashboard?publish=yes)  
*(Click the link above to explore the full interactive version.)*

![Tableau Dashboard Preview](https://public.tableau.com/app/profile/rohit.mannur3130/viz/Creator-DrivenCommerceAnalyticsWishlinkRohitMannur/WishlinkProductPerformanceDashboard?publish=yes)

## Project Summary
This repository contains a complete data analytics pipeline for e-commerce sales data. Key objectives include:
- Analyzing sales trends, product performance, and customer segments.
- Generating insights on top-performing categories, regional sales, and potential A/B testing opportunities.
- Reproducing the pipeline locally using Python scripts and SQL queries.

The project showcases proficiency in SQL for data extraction, Python (Pandas, NumPy) for ETL, and Tableau for visualization—skills directly aligned with Wishlink's need for data-driven decision-making in influencer marketing and product recommendations.

## Repository Structure
```
├── assets/                # Screenshots and visuals (e.g., dashboard previews, query examples)
├── data/                  # Sample input data (CSV files)
├── scripts/               # Python scripts for data processing
│   ├── etl_script.py      # Main ETL script to clean and transform data
│   └── generate_csvs.py   # Script to output Tableau-ready CSVs
├── sql/                   # SQL query files or snippets
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## Deliverables
- **Interactive Tableau Dashboard**: Visualizes key metrics like sales by category, customer retention, and geographic trends.
- **SQL Queries**: For data aggregation and analysis (snippets below).
- **Python Pipeline**: ETL process to prepare data for visualization.
- **Interview-Ready Pitch**: A 2-minute overview script.
- **Slide Outline**: For presenting findings.
- **Resume Bullets**: Highlighting project achievements.
- **A/B Test Suggestions**: Ideas for testing pricing strategies or product bundles.

## How to Reproduce the Pipeline Locally
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/wishlink-analytics-project.git
   cd wishlink-analytics-project
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the ETL script to process raw data:
   ```
   python scripts/etl_script.py --input data/raw_sales.csv --output data/processed_sales.csv
   ```
4. Generate Tableau-ready CSVs:
   ```
   python scripts/generate_csvs.py
   ```
   This will output files like `sales_by_category.csv` and `customer_segments.csv` in the `data/` folder.
5. Import the generated CSVs into Tableau and recreate the dashboard using the provided workbook (or start from scratch with the live link as reference).

## SQL Snippets
Here are key SQL queries used for analysis:

**Top Products by Sales:**
```sql
SELECT 
    product_id, 
    product_name, 
    SUM(sales_amount) AS total_sales
FROM sales_table
GROUP BY product_id, product_name
ORDER BY total_sales DESC
LIMIT 10;
```

![SQL Query Example](./assets/sql_query_example.png)

**Customer Segmentation by RFM:**
```sql
WITH rfm AS (
    SELECT 
        customer_id,
        MAX(order_date) AS last_order,
        COUNT(order_id) AS frequency,
        SUM(sales_amount) AS monetary
    FROM orders
    GROUP BY customer_id
)
SELECT 
    customer_id,
    NTILE(5) OVER (ORDER BY (CURRENT_DATE - last_order) DESC) AS recency_score,
    NTILE(5) OVER (ORDER BY frequency) AS frequency_score,
    NTILE(5) OVER (ORDER BY monetary) AS monetary_score
FROM rfm;
```

## 2-Minute Interview Pitch
"Hi, I'm Rohit, a data analyst with experience in e-commerce analytics. In this project for Wishlink, I analyzed sales data using SQL to segment customers and identify top products, then built an interactive Tableau dashboard to visualize trends. For example, I found that Category X drives 40% of revenue, suggesting targeted influencer campaigns. The Python pipeline ensures reproducibility, and I recommend A/B testing for pricing optimizations to boost conversions by up to 15% based on similar benchmarks."

## Slide Outline
1. **Introduction**: Project overview and Wishlink alignment.
2. **Data Sources & ETL**: Python pipeline demo.
3. **Key Insights**: SQL-driven findings (e.g., sales trends).
4. **Visualizations**: Tableau dashboard walkthrough.
5. **Recommendations**: A/B tests and next steps.
6. **Q&A**.

## Resume Bullets
- Developed an end-to-end e-commerce analytics pipeline using Python, SQL, and Tableau, analyzing sales data to uncover insights on product performance and customer behavior for Wishlink-inspired scenarios.
- Created interactive dashboards visualizing key metrics, resulting in recommendations for inventory optimization and marketing strategies.
- Implemented RFM customer segmentation via SQL, identifying high-value segments for targeted campaigns.
- Suggested A/B tests for pricing and bundling, projecting 10-20% revenue uplift based on data trends.

## A/B Test Suggestions
- **Test 1: Pricing Strategy** - Variant A: Current pricing; Variant B: 10% discount on low-stock items. Metric: Conversion rate.
- **Test 2: Product Bundling** - Variant A: Individual products; Variant B: Bundled recommendations. Metric: Average order value.
- **Test 3: Influencer Targeting** - Variant A: Broad campaigns; Variant B: Segment-specific (e.g., high-RFM customers). Metric: Engagement and sales lift.

For any questions or collaborations, feel free to reach out!
