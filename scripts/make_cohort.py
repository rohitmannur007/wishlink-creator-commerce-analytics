import pandas as pd

# Load cleaned event-level data
df = pd.read_csv("data/cleaned_wishlink.csv", low_memory=False)

# Parse datetime
df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')

# Ensure user_id is string
df['user_id'] = df['user_id'].astype(str)

# Get first event per user = signup
user_first = df.groupby('user_id')['event_time'].min().reset_index()
user_first.columns = ['user_id', 'signup_time']
user_first['cohort_month'] = user_first['signup_time'].dt.to_period('M').dt.to_timestamp()

# Merge cohort month back
df = df.merge(user_first[['user_id','cohort_month']], on='user_id', how='left')

# Create event month
df['event_month'] = df['event_time'].dt.to_period('M').dt.to_timestamp()

# Calculate months since signup
df['month_number'] = (
    (df['event_month'].dt.year - df['cohort_month'].dt.year) * 12 +
    (df['event_month'].dt.month - df['cohort_month'].dt.month)
)

# Only count users who made a purchase (real retention)
purchases = df[df['event_type'].str.lower() == 'purchase']

# Count cohort sizes
cohort_sizes = user_first.groupby('cohort_month')['user_id'].nunique().reset_index()
cohort_sizes.columns = ['cohort_month','cohort_size']

# Count active purchasers per cohort per month
active = purchases.groupby(['cohort_month','month_number'])['user_id'].nunique().reset_index()
active.columns = ['cohort_month','month_number','active_users']

# Merge
cohort = active.merge(cohort_sizes, on='cohort_month')

# Retention %
cohort['retention_pct'] = cohort['active_users'] / cohort['cohort_size']

# Save for Tableau
cohort.to_csv("data/tableau_cohort.csv", index=False)

print("Cohort file created: data/tableau_cohort.csv")
print(cohort.head())
