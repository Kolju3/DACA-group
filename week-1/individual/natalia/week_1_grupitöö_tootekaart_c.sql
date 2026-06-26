
ALAÜLESANDE KAART C: Tooteandmed - UrbanStyle
Koostaja: Natalia Krassilnikova

-- 1. Üldine toodete arv
SELECT COUNT(*) AS toodete_arv 
       FROM products;

-- 2. Veergude struktuuri kontroll
SELECT * 
       FROM products 
       LIMIT 10;

-- 3. Unikaalsed kategooriad
SELECT DISTINCT category 
       FROM products;

-- 4. Kõige kallimad ja soodsamad tooted
SELECT product_name, category, retail_price 
FROM products 
ORDER BY retail_price DESC 
LIMIT 10;

SELECT product_name, category, retail_price 
FROM products 
ORDER BY retail_price ASC 
LIMIT 10;

-- 5. 'laste_riided' analüüs
SELECT * FROM products 
WHERE category = 'laste_riided' 
ORDER BY retail_price DESC;

-- 'laste_riided' alamkategooriad
SELECT DISTINCT subcategory
FROM products
WHERE category = 'laste_riided'
ORDER BY subcategory;

-- 6. Andmete kvaliteedi kontroll (puuduvate väärtuste leidmine)
SELECT COUNT(*) - COUNT(retail_price) AS puuduvad_hinnad 
       FROM products;
SELECT COUNT(*) - COUNT(category) AS puuduvad_kategooriad
       FROM products;

LISA 30% 

1. Tooteid kategooriate kaupa


SELECT category, COUNT(*) AS toodete_arv
FROM products    
GROUP BY category
ORDER BY toodete_arv DESC;

2. Põhjalik hinnastatistika


SELECT category, 
       COUNT(*) AS toodete_arv, 
       MIN(retail_price) AS min_hind, 
       MAX(retail_price) AS max_hind,
       AVG(retail_price) AS keskmine_hind
FROM products
GROUP BY category
ORDER BY max_hind DESC;

3. Premium-tooted (laste_riided > 50€)


SELECT * FROM products 
WHERE retail_price > 50  
  AND category = 'laste_riided' 
ORDER BY retail_price DESC;
