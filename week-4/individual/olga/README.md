# Nädal 4 – olga individuaalne töö

## Ülesanne
Analüüsi tootekategooriaid, laoseisu ja müüdud vs laos suhteid. Kasuta GROUP BY, HAVING ja window functions, et leida probleemsed kategooriad.

## Mida tegin
3 SQL päringut + kokkuvõtlik tabel (kategooriate raport + soovitused)

Analüüsi põhjal on kõige suurema müügimahuga kategooria meeste_riided, kus müüdi kokku 4121 toodet. Kõige kõrgema keskmise hinnaga kategooria on jalanõusid (214,10 €), mis viitab sellele, et selles kategoorias müüakse kallimaid tooteid. Samal ajal on laste_riided madalaima keskmise hinnaga kategooria (85,30 €), kuid selle müügimaht on siiski väga hea, mis näitab stabiilset nõudlust. Kategooriate keskmine müüdud kogus toote kohta jääb vahemikku 1,78–1,84, mis tähendab, et müük on eri kategooriates üsna ühtlane. Annale soovitan hoida piisavat laovaru meeste riiete ja jalanõude kategooriates, sest nende müügimaht ja toodete väärtus on kõrged, ning jälgida regulaarselt kallimate toodete laoseisu, et vältida populaarsete toodete otsalõppemist.

## SQL päringud / failid

https://supabase.com/dashboard/project/xwmwqxqorsiauliaynkk/sql/de596388-f3c9-4556-898d-828530cab064

SELECT      p.category,      COUNT(DISTINCT p.product_id) AS tooteid,      ROUND(AVG(p.retail_price), 2) 
AS keskmine_hind,      MIN(p.retail_price) 
AS min_hind,      MAX(p.retail_price) 
AS max_hind    
FROM products p    
GROUP BY p.category    
ORDER BY tooteid DESC;

| category      | tooteid | keskmine_hind | min_hind | max_hind |
| ------------- | ------- | ------------- | -------- | -------- |
| meeste_riided | 82      | 189.91        | 48.85    | 374.54   |
| jalanõusid    | 73      | 214.10        | 58.49    | 434.08   |
| laste_riided  | 70      | 85.30         | 22.70    | 168.82   |
| naiste_riided | 70      | 192.58        | 32.93    | 351.33   |
| aksessuaarid  | 67      | 125.71        | 13.53    | 231.13   |

SELECT
    p.category,
    SUM(s.quantity) AS muudud_kokku,
    AVG(s.quantity) AS keskmine_muudud_kogus_toote_kohta
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY p.category
HAVING SUM(s.quantity) > 100;

| category      | muudud_kokku | keskmine_muudud_kogus_toote_kohta |
| ------------- | ------------ | --------------------------------- |
| jalanõusid    | 3737         | 1.8399803052683407                |
| laste_riided  | 3686         | 1.8184509126788357                |
| aksessuaarid  | 3231         | 1.8233634311512415                |
| naiste_riided | 3604         | 1.7823936696340257                |
| meeste_riided | 4121         | 1.8186231244483672                |

SELECT      p.product_name,      p.category,      p.retail_price,      ROW_NUMBER() OVER (        PARTITION BY p.category        
ORDER BY p.retail_price DESC      ) 
AS koht_kategoorias    
FROM products p;

| product_name                               | category     | retail_price | koht_kategoorias |
| ------------------------------------------ | ------------ | ------------ | ---------------- |
| Luksuslik metallist labakindad             | aksessuaarid | 231.13       | 1                |
| Moodne keraamiline nahkvöö                 | aksessuaarid | 225.28       | 2                |
| Kerge siidine nahkkindad                   | aksessuaarid | 219.83       | 3                |
| Kerge siidine nahkkindad                   | aksessuaarid | 219.83       | 4                |
| Stiilne kangast nokamüts                   | aksessuaarid | 219.38       | 5                |
| Stiilne villane seljakott                  | aksessuaarid | 215.58       | 6                |
| Praktiline kangast reisikott               | aksessuaarid | 208.72       | 7                |
| Stiilne puust müts                         | aksessuaarid | 205.89       | 8                |
| Stiilne puust müts                         | aksessuaarid | 205.89       | 9                |
| Praktiline villane kott                    | aksessuaarid | 204.87       | 10               |
| Boheemlaslik villane barett                | aksessuaarid | 203.39       | 11               |
| Õhuline villane sõrmus                     | aksessuaarid | 199.80       | 12               |
| Kerge metallist labakindad                 | aksessuaarid | 194.57       | 13               |
| Vintage kangast vöö                        | aksessuaarid | 191.48       | 14               |
| Klassikaline nahkne sõrmus                 | aksessuaarid | 188.91       | 15               |
| Stiilne villane sõrmkindad                 | aksessuaarid | 184.15       | 16               |
| Trendikas kangast kindad                   | aksessuaarid | 184.02       | 17               |
| Moodne siidine sall                        | aksessuaarid | 183.40       | 18               |
| Boheemlaslik siidine sõrmkindad            | aksessuaarid | 183.31       | 19               |
| Boheemlaslik kangast kangasvöö             | aksessuaarid | 181.68       | 20               |
| Praktiline kangast elastne vöö             | aksessuaarid | 176.65       | 21               |
| Elegantne siidine müts                     | aksessuaarid | 173.62       | 22               |
| Praktiline keraamiline kaabu               | aksessuaarid | 169.95       | 23               |
| Õhuline nahkne elastne vöö                 | aksessuaarid | 156.13       | 24               |
| Elegantne keraamiline rahakott             | aksessuaarid | 155.84       | 25               |
| Elegantne keraamiline rahakott             | aksessuaarid | 155.84       | 26               |
| Moodne kangast sõrmus                      | aksessuaarid | 155.45       | 27               |
| Minimalistlik puust kootud müts            | aksessuaarid | 153.11       | 28               |
| Luksuslik keraamiline elastne vöö          | aksessuaarid | 149.55       | 29               |
| Luksuslik keraamiline elastne vöö          | aksessuaarid | 149.55       | 30               |
| Praktiline nahkne sõrmus                   | aksessuaarid | 149.47       | 31               |
| Moodne keraamiline sall                    | aksessuaarid | 147.16       | 32               |
| Moodne keraamiline sall                    | aksessuaarid | 147.16       | 33               |
| Trendikas nahkne sõrmus                    | aksessuaarid | 145.72       | 34               |
| Klassikaline nahkne nahkkindad             | aksessuaarid | 144.36       | 35               |
| Elegantne keraamiline labakindad           | aksessuaarid | 134.94       | 36               |
| Moodne metallist rätik                     | aksessuaarid | 122.07       | 37               |
| Luksuslik keraamiline seljakott            | aksessuaarid | 121.98       | 38               |
| Trendikas kangast nokamüts                 | aksessuaarid | 117.05       | 39               |
| Trendikas villane nahkkindad               | aksessuaarid | 113.86       | 40               |
| Klassikaline puust nahkvöö                 | aksessuaarid | 111.74       | 41               |
| Elegantne villane kaabu                    | aksessuaarid | 109.42       | 42               |
| Minimalistlik siidine labakindad           | aksessuaarid | 107.26       | 43               |
| Vintage metallist seljakott                | aksessuaarid | 106.71       | 44               |
| Klassikaline kangast nahkkindad            | aksessuaarid | 95.39        | 45               |
| Elegantne kangast kindad                   | aksessuaarid | 93.13        | 46               |
| Õhuline siidine kaelakee                   | aksessuaarid | 74.81        | 47               |
| Minimalistlik keraamiline sall             | aksessuaarid | 66.88        | 48               |
| Elegantne puust kootud müts                | aksessuaarid | 65.60        | 49               |
| Boheemlaslik kangast reisikott             | aksessuaarid | 62.56        | 50               |
| Kerge puust barett                         | aksessuaarid | 57.08        | 51               |
| Elegantne klaasist barett                  | aksessuaarid | 51.10        | 52               |
| Praktiline puust sall                      | aksessuaarid | 50.85        | 53               |
| Praktiline klaasist sõrmkindad             | aksessuaarid | 47.88        | 54               |
| Boheemlaslik klaasist kaelakee             | aksessuaarid | 47.07        | 55               |
| Stiilne siidine labakindad                 | aksessuaarid | 45.21        | 56               |
| Mugav klaasist kõrvarõngad                 | aksessuaarid | 29.48        | 57               |
| Kerge nahkne õlakott                       | aksessuaarid | 29.42        | 58               |
| Trendikas keraamiline sõrmkindad           | aksessuaarid | 28.56        | 59               |
| Vintage keraamiline barett                 | aksessuaarid | 26.79        | 60               |
| Moodne nahkne müts                         | aksessuaarid | 23.45        | 61               |
| Elegantne metallist sall                   | aksessuaarid | 22.04        | 62               |
| Luksuslik nahkne käekott                   | aksessuaarid | 17.97        | 63               |
| Moodne villane kaelasall                   | aksessuaarid | 16.62        | 64               |
| Soe siidine kaelakee                       | aksessuaarid | 16.37        | 65               |
| Praktiline siidine rätik                   | aksessuaarid | 15.09        | 66               |
| Vintage villane kangasvöö                  | aksessuaarid | 13.53        | 67               |
| Õhuline sünteetiline sporditossud          | jalanõusid   | 434.08       | 1                |
| Klassikaline seemisnahkne jooksutossud     | jalanõusid   | 402.62       | 2                |
| Õhuline villane jooksutossud               | jalanõusid   | 376.33       | 3                |
| Soe sünteetiline loaferid                  | jalanõusid   | 375.34       | 4                |
| Luksuslik villane pahkluu saapad           | jalanõusid   | 371.79       | 5                |
| Trendikas goretex oxfordid                 | jalanõusid   | 371.05       | 6                |
| Stiilne goretex kingad                     | jalanõusid   | 368.97       | 7                |
| Moodne villane nahk sandaalid              | jalanõusid   | 368.67       | 8                |
| Moodne villane nahk sandaalid              | jalanõusid   | 368.67       | 9                |
| Sportlik kangast tossud                    | jalanõusid   | 358.41       | 10               |
| Õhuline goretex tennised                   | jalanõusid   | 350.19       | 11               |
| Boheemlaslik villane tennised              | jalanõusid   | 339.21       | 12               |
| Õhuline nahkne sporditossud                | jalanõusid   | 329.99       | 13               |
| Boheemlaslik kangast rannasandaalid        | jalanõusid   | 324.38       | 14               |
| Praktiline kangast kõrge kontsaga kingad   | jalanõusid   | 319.98       | 15               |
| Sportlik seemisnahkne nahk sandaalid       | jalanõusid   | 307.27       | 16               |
| Õhuline sünteetiline rannasandaalid        | jalanõusid   | 302.86       | 17               |
| Sportlik villane tossud                    | jalanõusid   | 292.61       | 18               |
| Õhuline sünteetiline kõrge kontsaga kingad | jalanõusid   | 291.72       | 19               |
| Sportlik kangast tennised                  | jalanõusid   | 282.29       | 20               |
| Minimalistlik nahkne platvormi kontsad     | jalanõusid   | 280.13       | 21               |
| Klassikaline kangast tennised              | jalanõusid   | 276.97       | 22               |
| Õhuline goretex kingad                     | jalanõusid   | 274.87       | 23               |
| Soe seemisnahkne nahk sandaalid            | jalanõusid   | 273.32       | 24               |
| Boheemlaslik goretex kingad                | jalanõusid   | 273.06       | 25               |
| Vintage villane rannasandaalid             | jalanõusid   | 271.35       | 26               |
| Soe nahkne platvormi kontsad               | jalanõusid   | 270.69       | 27               |
| Klassikaline kangast platvormi kontsad     | jalanõusid   | 253.80       | 28               |
| Soe sünteetiline sandaalid                 | jalanõusid   | 252.10       | 29               |
| Õhuline villane platvorm sandaalid         | jalanõusid   | 251.52       | 30               |
| Õhuline seemisnahkne rannasandaalid        | jalanõusid   | 241.13       | 31               |
| Boheemlaslik nahkne talvesaapad            | jalanõusid   | 234.91       | 32               |
| Klassikaline villane madalad kontsad       | jalanõusid   | 232.61       | 33               |

<img width="1035" height="708" alt="GT WEEK 4 OLGA L ROLL C" src="https://github.com/user-attachments/assets/9c1a4cd7-4c2b-4f98-9d6e-a4942b724586" />


