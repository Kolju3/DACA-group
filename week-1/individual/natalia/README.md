🚀 Nädal 1: ALAÜLESANDE KAART C - Tooteandmed (UrbanStyle)
Koostaja: Natalia Krassilnikova

📊 Analüüsi kokkuvõte
Andmebaas sisaldab kokku 362 toodet, mis jagunevad 5 põhikategooriasse: jalanõud, laste riided, aksessuaarid, naiste riided ja meeste riided.

Laste riiete kategooria: Sisaldab 5 alamkategooriat (jakid, kleidid, püksid, komplektid ja trikotaaž).

Hinnastatistika:

Soodsaim toode: "Vintage villane kangasvöö" (13.53€).

Kalleim toode: "õhuline sünteetiline sporditossud" (434€).

Andmekvaliteet: Andmed on korrektsed – puuduvaid hinnad ja kategooriaid ei esine.

Päringu eesmärk	             Tõendusmaterjal	
Üldine toodete arv	             Toodete arv.png	
Tabeli struktuuri uurimine	      Veerud.png	
Unikaalsed kategooriad	      kategooriad.png	
Kallim ja soodsaim toode	      Kallim toode.png, Soodsaim toode.png	
Laste riiete alamkategooriad      Lasteriiete alamkategooriad.png	
Andmekvaliteedi kontroll	      puuduvad kategooriad:hinnad.png	

💡 Lisaülesanded (30%)
Siin on süvendatud analüüs, kus grupeerisin tooted kategooriate kaupa ning arvutasin hinnastatistika.

1. Tooteid kategooriate kaupa
Tulemus: "Tooted kategooriate järgi kokku"

SQL
SELECT category, COUNT(*) AS toodete_arv
FROM products    
GROUP BY category
ORDER BY toodete_arv DESC;

2. Põhjalik hinnastatistika
Tulemus: "Keskimne hind kategooriates"

SQL
SELECT category, 
       COUNT(*) AS toodete_arv, 
       MIN(retail_price) AS min_hind, 
       MAX(retail_price) AS max_hind,
       AVG(retail_price) AS keskmine_hind
FROM products
GROUP BY category
ORDER BY max_hind DESC;

3. Premium-tooted (laste_riided > 50€)
Tulemus: "Lasteriided üle 50€"

SQL
SELECT * FROM products 
WHERE retail_price > 50  
  AND category = 'laste_riided' 
ORDER BY retail_price DESC;

Kõik päringud on salvestatud faili: week_1_grupitoo_tootekaart_c.sql

Päringud tehtud: https://supabase.com/dashboard/project/xwmwqxqorsiauliaynkk/sql/10b85090-f04c-4d82-b2d6-2a51fb279489
