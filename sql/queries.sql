-- Top creators by GMV + conversion
SELECT
  creator_id,
  SUM(CASE WHEN is_view=1 THEN 1 ELSE 0 END) AS views,
  SUM(CASE WHEN is_purchase=1 THEN 1 ELSE 0 END) AS purchases,
  SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv,
  ROUND(100.0 * SUM(CASE WHEN is_purchase=1 THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN is_view=1 THEN 1 ELSE 0 END),0),3) AS conv_pct
FROM events
GROUP BY creator_id
ORDER BY gmv DESC
LIMIT 100;

-- Funnel snapshot
SELECT
  SUM(is_view) AS views,
  SUM(is_click) AS clicks,
  SUM(is_add_to_cart) AS adds,
  SUM(is_purchase) AS purchases,
  SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv
FROM events;

-- Creator x category lift
WITH cat AS (
  SELECT category, SUM(is_view) AS cat_views, SUM(is_purchase) AS cat_purchases
  FROM events
  GROUP BY category
), creator_cat AS (
  SELECT creator_id, category, SUM(is_view) AS views, SUM(is_purchase) AS purchases,
         SUM(CASE WHEN is_purchase=1 THEN price ELSE 0 END) AS gmv
  FROM events
  GROUP BY creator_id, category
)
SELECT cc.creator_id, cc.category, cc.views, cc.purchases, cc.gmv,
       ROUND(100.0 * cc.purchases / NULLIF(cc.views,0),3) AS conv_pct,
       ROUND(100.0 * c.cat_purchases / NULLIF(c.cat_views,0),3) AS cat_conv_pct,
       CASE WHEN c.cat_purchases=0 THEN NULL ELSE ROUND((cc.purchases*1.0/NULLIF(cc.views,0)) / (c.cat_purchases*1.0/NULLIF(c.cat_views,0)),3) END AS lift
FROM creator_cat cc JOIN cat c ON cc.category = c.category
ORDER BY lift DESC;
