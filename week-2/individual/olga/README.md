# Nädal 2 – olga individuaalne töö

## Ülesanne
ALAÜLESANDE KAART A: Müügiandmete Puhastamine
Element
Kirjeldus
ROLL
Müügiandmete puhastaja (Sales Data Cleaner)
ÜLESANNE
Leia duplikaadid, NULL väärtused ja vigased kuupäevad sales tabelis. Loo test koopia, puhasta ja dokumenteeri kõik muudatused.
SISEND
Tabel: sales (Supabase)
VÄLJUND
Puhastamisraport (duplikaadid leitud, NULL-id leitud, formaadivead, soovitused) + SQL skript

## Mida tegin
Mina puhastasin müügiandmeid. Leidsin 5116 duplikaatset rida ja 1487 NULL väärtust. See tähendab äriliselt, et müügiaruanded võivad olla ebatäpsed ning osa müüke ei ole võimalik konkreetsete klientidega siduda.

Soovitus

Toomas peaks esimesena eemaldama duplikaadid, sest neid on kõige rohkem (5116 rida) ning need võivad moonutada müügiaruandeid, käivet ja analüüse. Seejärel tuleks parandada või täiendada 1487 puuduvat customer_id väärtust, et kõik müügid oleksid seotud õige kliendiga. Kuna sale_date ja total_price väljad on korrektsed ning tuleviku kuupäevi ei esine, ei vaja need täiendavat puhastamist.

Samm 1. Loo test koopia (ära tööta production tabelil!):
CREATE TABLE sales_test AS SELECT * FROM sales;
-- Taga unikaalne rea-tunnus dedup'i jaoks (lisab `id` AINULT siis, kui see puudub).
-- NB: `CREATE TABLE ... AS SELECT` ei pärandata alati `id`-d — see rida teeb Sammu 3 töökindlaks.
ALTER TABLE sales_test ADD COLUMN IF NOT EXISTS id SERIAL;
-- Kontrolli ridade arvu

| ridade_arv |
| ---------- |
| 15234      |

Samm 2. Leia duplikaadid — millised tellimused (arved) korduvad?
SELECT invoice_id, COUNT(*) AS koopiate_arv
FROM sales_test
GROUP BY invoice_id
HAVING COUNT(*) > 1
ORDER BY koopiate_arv DESC;

| invoice_id       | koopiate_arv |
| ---------------- | ------------ |
| INV-202308-00283 | 6            |
| INV-202312-00423 | 6            |
| INV-202308-00280 | 5            |
| INV-202406-00248 | 5            |
| INV-202406-00316 | 5            |
| INV-202309-00023 | 5            |
| INV-202403-00012 | 5            |
| INV-202309-00228 | 5            |
| INV-202308-00266 | 5            |
| INV-202407-00450 | 5            |
| INV-202401-00024 | 5            |
| INV-202306-00380 | 5            |
| INV-202408-00030 | 5            |
| INV-202312-00289 | 5            |
| INV-202501-00124 | 5            |
| INV-202409-00044 | 5            |
| INV-202302-00131 | 4            |
| INV-202411-00278 | 4            |
| INV-202309-00184 | 4            |
| INV-202408-00182 | 4            |
| INV-202308-00064 | 4            |
| INV-202406-00292 | 4            |
| INV-202408-00190 | 4            |
| INV-202408-00503 | 4            |
| INV-202308-00258 | 4            |
| INV-202408-00002 | 4            |
| INV-202407-00069 | 4            |
| INV-202303-00038 | 4            |
| INV-202311-00249 | 4            |
| INV-202302-00228 | 4            |
| INV-202302-00213 | 4            |
| INV-202404-00034 | 4            |
| INV-202409-00052 | 4            |
| INV-202406-00356 | 4            |
| INV-202304-00183 | 4            |
| INV-202307-00241 | 4            |
| INV-202412-00028 | 4            |
| INV-202406-00507 | 4            |
| INV-202405-00063 | 4            |
| INV-202312-00086 | 4            |
| INV-202408-00129 | 4            |
| INV-202308-00087 | 4            |
| INV-202408-00459 | 4            |
| INV-202412-00296 | 4            |
| INV-202308-00203 | 4            |
| INV-202311-00238 | 4            |
| INV-202309-00073 | 4            |
| INV-202304-00040 | 4            |
| INV-202410-00301 | 4            |
| INV-202411-00081 | 4            |
| INV-202311-00124 | 4            |
| INV-202402-00033 | 4            |
| INV-202308-00285 | 4            |
| INV-202303-00128 | 4            |
| INV-202305-00120 | 4            |
| INV-202402-00076 | 4            |
| INV-202408-00455 | 4            |
| INV-202412-00402 | 4            |
| INV-202402-00222 | 4            |
| INV-202403-00113 | 4            |
| INV-202401-00136 | 4            |
| INV-202401-00152 | 4            |
| INV-202305-00268 | 4            |
| INV-202401-00258 | 4            |
| INV-202502-00206 | 4            |
| INV-202310-00099 | 4            |
| INV-202404-00162 | 4            |
| INV-202403-00092 | 4            |
| INV-202407-00192 | 4            |
| INV-202311-00167 | 4            |
| INV-202312-00450 | 4            |
| INV-202404-00170 | 4            |
| INV-202308-00319 | 4            |
| INV-202301-00029 | 4            |
| INV-202406-00156 | 4            |
| INV-202301-00076 | 4            |
| INV-202308-00256 | 4            |
| INV-202307-00365 | 4            |
| INV-202305-00162 | 4            |
| INV-202402-00152 | 4            |
| INV-202306-00267 | 4            |
| INV-202411-00393 | 4            |
| INV-202305-00221 | 4            |
| INV-202407-00077 | 4            |
| INV-202309-00122 | 4            |
| INV-202411-00001 | 4            |
| INV-202312-00209 | 4            |
| INV-202302-00010 | 4            |
| INV-202406-00321 | 4            |
| INV-202403-00211 | 4            |
| INV-202408-00242 | 4            |
| INV-202301-00047 | 4            |
| INV-202409-00110 | 4            |
| INV-202404-00400 | 4            |
| INV-202301-00242 | 4            |
| INV-202411-00272 | 4            |
| INV-202401-00035 | 4            |
| INV-202411-00341 | 4            |
| INV-202303-00257 | 4            |
| INV-202501-00283 | 4            |

Samm 3. Loe kokku duplikaatsete ridade arv:
SELECT COUNT(*) AS duplikaat_read
FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)
    FROM sales_test
    GROUP BY invoice_id
);

| duplikaat_read |
| -------------- |
| 5116           |

Samm 4. Leia NULL väärtused kriitilistes väljades:
SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS null_customer_id,
    COUNT(*) FILTER (WHERE sale_date IS NULL) AS null_sale_date,
    COUNT(*) FILTER (WHERE total_price IS NULL) AS null_total_price
FROM sales_test;

| null_customer_id | null_sale_date | null_total_price |
| ---------------- | -------------- | ---------------- |
| 1487             | 0              | 0                |

Samm 5. Kontrolli kuupäevade formaati — kas on tuleviku kuupäevi?
SELECT COUNT(*) AS tuleviku_kuupaevad
FROM sales_test
WHERE sale_date > CURRENT_DATE;

| tuleviku_kuupaevad |
| ------------------ |
| 0                  |

Samm 6. Koosta puhastamisraport:

| Kategooria          | Leitud probleeme | Kirjeldus                                                     |
| ------------------- | ---------------: | ------------------------------------------------------------- |
| Duplikaadid         |         **5116** | Korduvad `invoice_id` väärtused (duplikaattellimused)         |
| NULL `customer_id`  |         **1487** | Puuduv kliendi viide                                          |
| NULL `sale_date`    |            **0** | Puuduv kuupäev                                                |
| NULL `total_price`  |            **0** | Puuduv summa                                                  |
| Tuleviku kuupäevad  |            **0** | Kuupäev > tänane                                              |
| **KOKKU probleeme** |         **6603** | 5116 duplikaatset rida + 1487 puuduvat `customer_id` väärtust |

Soovitus

Toomas peaks esimesena eemaldama duplikaadid, sest neid on kõige rohkem (5116 rida) ning need võivad moonutada müügiaruandeid, käivet ja analüüse. Seejärel tuleks parandada või täiendada 1487 puuduvat customer_id väärtust, et kõik müügid oleksid seotud õige kliendiga. Kuna sale_date ja total_price väljad on korrektsed ning tuleviku kuupäevi ei esine, ei vaja need täiendavat puhastamist.

Kvaliteedikontroll
☑ Testkoopia on loodud (sales_test, mitte production tabel).
☑ Duplikaadid on leitud GROUP BY + HAVING abil.
☑ Raport sisaldab konkreetseid numbreid.


## SQL päringud / failid
_Lisa lingid_
https://supabase.com/dashboard/project/jrkmbzgrdxffhdmbtvey/sql/7464cfd4-9fde-4588-a4ff-2298bd66548c

CREATE TABLE sales_test AS SELECT * FROM sales;
-- Taga unikaalne rea-tunnus dedup'i jaoks (lisab `id` AINULT siis, kui see puudub).
-- NB: `CREATE TABLE ... AS SELECT` ei pärandata alati `id`-d — see rida teeb Sammu 3 töökindlaks.
ALTER TABLE sales_test ADD COLUMN IF NOT EXISTS id SERIAL;
-- Kontrolli ridade arvu
SELECT COUNT(*) AS ridade_arv FROM sales_test;

SELECT invoice_id, COUNT(*) AS koopiate_arv
FROM sales_test
GROUP BY invoice_id
HAVING COUNT(*) > 1
ORDER BY koopiate_arv DESC;

SELECT COUNT(*) AS duplikaat_read
FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)
    FROM sales_test
    GROUP BY invoice_id
);

SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS null_customer_id,
    COUNT(*) FILTER (WHERE sale_date IS NULL) AS null_sale_date,
    COUNT(*) FILTER (WHERE total_price IS NULL) AS null_total_price
FROM sales_test;

SELECT COUNT(*) AS tuleviku_kuupaevad
FROM sales_test
WHERE sale_date > CURRENT_DATE;

