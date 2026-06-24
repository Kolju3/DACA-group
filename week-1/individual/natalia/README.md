🚀 Nädal 1: ALAÜLESANDE KAART C - Tooteandmed (UrbanStyle)
Koostaja: Natalia Krassilnikova

📊 Analüüsi kokkuvõte

See projekt keskendub UrbanStyle tooteandmebaasi analüüsile. Andmebaas sisaldab kokku 362 toodet, mis jagunevad viide põhikategooriasse: jalanõud, laste riided, aksessuaarid, naiste riided ja meeste riided.

Peamised leiud:

Andmekvaliteet: Andmed on korrektsed, puuduvaid hindu ega kategooriaid ei tuvastatud.

Laste riided: Kategooria jaguneb 5 alamkategooriaks (jakid, kleidid, püksid, komplektid ja trikotaaž).

Hinnavahemik:

💰 Soodsaim toode: "Vintage villane kangasvöö" (13.53€)

💎 Kalleim toode: "Õhuline sünteetiline sporditossud" (434€)

📸 Tõendusmaterjal
Analüüsi käigus tehtud ekraanitõmmised ja kontrollpäringud:

Eesmärk	Fail
Üldine toodete arv	Toodete arv.png
Tabeli struktuuri uurimine	Veerud.png
Unikaalsed kategooriad	kategooriad.png
Hinnastatistika (min/max)	Kallim toode.png, Soodsaim toode.png
Lasteriiete alamkategooriad	Lasteriiete alamkategooriad.png
Andmekvaliteedi kontroll	puuduvad kategooriad:hinnad.png


💡 Süvendatud analüüs (Lisaülesanded)

Andmete põhjalikumaks uurimiseks grupeerisin tooted ja arvutasin hinnastatistika.

1. Toodete arv kategooriate kaupa

SELECT category, COUNT(*) AS toodete_arv
FROM products    
GROUP BY category
ORDER BY toodete_arv DESC;

2. Põhjalik hinnastatistika kategooriates

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

📁 Failid ja lingid
SQL päringute fail: week_1_grupitoo_tootekaart_c.sql

Supabase Dashboard: Vaata päringuid siit

L
