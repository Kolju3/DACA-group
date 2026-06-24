🚀 Nädal 1: ALAÜLESANDE KAART C - Tooteandmed (UrbanStyle)
Koostaja: Natalia Krassilnikova

📝 Ülevaade
Selles ülesandes viisin läbi UrbanStyle andmebaasi analüüsi, et mõista toodete struktuuri, kategooriate jaotust ning hinnastatistikat.

📊 Analüüsi kokkuvõte
Andmebaas sisaldab kokku 362 toodet, mis jagunevad 5 põhikategooriasse: jalanõud, laste riided, aksessuaarid, naiste riided ja meeste riided.

Laste riiete kategooria: Sisaldab 5 alamkategooriat (jakid, kleidid, püksid, komplektid ja trikotaaž).

Hinnastatistika:

Soodsaim toode: "Vintage villane kangasvöö" (13.53€).

Kalleim toode: "õhuline sünteetiline sporditossud" (434€).

Andmekvaliteet: Andmed on korrektsed – puuduvad hinnad ja kategooriad puuduvad.

🛠 SQL Päringud ja Tõendusmaterjalid:
Päringu eesmärkTulemuse pilt (Screenshot)Üldine toodete arvToodete arv.pngTabeli veergude struktuurVeerud.pngUnikaalsed kategooriadkategooriad.pngKallim / Soodsaim toodeKallim toode.png, Soodsaim toode.pngLaste riiete alamkategooriadLasteriiete alamkategooriad.pngAndmete kvaliteedi kontrollpuuduvad kategooriad:hinnad.png

💡 Lisaülesanded (30%)
Jõudsin süvendatud analüüsini, kus grupeerisin tooted kategooriate kaupa ning arvutasin välja hinnastatistika.

1. Toodete arv ja keskmised hinnad kategooriates
Selle päringuga sain ülevaate iga kategooria mahtudest ja hinnavahemikest:

SQL
SELECT category, 
       COUNT(*) AS toodete_arv, 
       MIN(retail_price) AS min_hind, 
       MAX(retail_price) AS max_hind,
       ROUND(AVG(retail_price), 2) AS keskmine_hind
FROM products
GROUP BY category
ORDER BY max_hind DESC;
Tulemus: Keskmine hind kategooriates.png

2. Premium tooted laste riiete kategoorias (>50€)
Analüüsisin lasteriiete segmendi kallimaid tooteid:

SQL
SELECT * FROM products 
WHERE retail_price > 50 
  AND category = 'laste_riided' 
ORDER BY retail_price DESC;
Tulemus: Lasteriided üle 50€.png

Projekti SQL-baasi haldamine: https://supabase.com/dashboard/project/xwmwqxqorsiauliaynkk/sql/10b85090-f04c-4d82-b2d6-2a51fb279489
