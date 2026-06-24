# Nädal 1 – ALAÜLESANDE KAART C: Tooteandmed - UrbanStyle
Koostaja: Natalia Krassilnikova

## Ülesanne
Eesmärk on uurida Tooteandmed tabelit ja analüüsida sealt leitavaid andmeid. 

## Mida tegin
Uurisin toodete kategooriad, alamkategooriaid. Vaatasin lähemalt lasteriiete kategooriat. Leidsin kõige kallima ja soodsama hinna kõikide toodete seast. Oma päringud sallvestasin SQL failina ja screenshotid tulemustest on leitavad siin https://github.com/Kolju3/DACA-group/tree/main/week-1/individual/natalia.

## SQL päringud / failid
ANALÜÜSI KOKKUVÕTE:
Andmebaas sisaldab kokku 362 toodet, mis jagunevad 5 põhikategooriasse: 
jalanõud, laste riided, aksessuaarid, naiste riided ja meeste riided. 

Kategooriad jagunevad alamkategooriateks. Näiteks 'laste_riided' 
kategoorias on 5 alamkategooriat: jakid, kleidid, püksid, komplektid ja trikotaaž.

Hinnastatistika:
- Kõige soodsam toode on "Vintage villane kangasvöö" (aksessuaaride kat.), hinnaga 13.53€.
- Kõige kallim toode on "õhuline sünteetiline sporditossud" (jalanõude kat.), hinnaga 434€.

Andmete kvaliteet:
Kõikidel toodetel on määratud hind ja kategooria (puuduvaid väärtusi ei esine).
============================================================
*/

https://supabase.com/dashboard/project/xwmwqxqorsiauliaynkk/sql/10b85090-f04c-4d82-b2d6-2a51fb279489

-- 1. Üldine toodete arv LISA "Toodete arv.png"
SELECT COUNT(*) AS toodete_arv FROM products;

-- 2. Veergude struktuuri kontroll Lisa:"Veerud.png"
SELECT * FROM products LIMIT 10;

-- 3. Unikaalsed kategooriad (Lisa:"kategooriad.png")
SELECT DISTINCT category FROM products;

-- 4. Kõige kallimad ja soodsamad tooted (Lisa:"Kallim toode.png"; "Soodsaim toode.png")
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

-- 'laste_riided' alamkategooriad (Lisa:"Lasteriiete alamkategooriad.png")
SELECT DISTINCT subcategory
FROM products
WHERE category = 'laste_riided'
ORDER BY subcategory;

-- 6. Andmete kvaliteedi kontroll (puuduvate väärtuste leidmine) (Lisa:"puuduvad kategooriad:hinnad.png")
SELECT COUNT(*) - COUNT(retail_price) AS puuduvad_hinnad FROM products;
SELECT COUNT(*) - COUNT(category) AS puuduvad_kategooriad FROM products;


SQL fail: week_1_grupitoo_tootekaart_c.sql.
