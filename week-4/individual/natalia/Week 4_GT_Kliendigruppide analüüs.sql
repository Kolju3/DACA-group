WITH kliendi_baasandmed AS (
  SELECT
    c.customer_id,
    c.city,
    SUM(o.total_price) AS kogukäive
  FROM customers c
  JOIN sales o ON c.customer_id = o.customer_id
  GROUP BY c.customer_id, c.city
),
segmenteeritud_baas AS (
  SELECT
    customer_id,
    city,
    kogukäive,
    CASE
      WHEN kogukäive > 500 THEN 'VIP'
      WHEN kogukäive > 150 THEN 'Regular'
      ELSE 'Uus'
    END AS segment
  FROM kliendi_baasandmed
)
SELECT 
    segment,
    COUNT(customer_id) AS klientide_arv,
    ROUND(AVG(kogukäive), 2) AS keskmine_kaive,
    -- Kuvab linnad, kus selle segmendi kliendid asuvad
    STRING_AGG(DISTINCT city, ', ') AS asukohalinnad
FROM segmenteeritud_baas
GROUP BY segment
ORDER BY keskmine_kaive DESC;