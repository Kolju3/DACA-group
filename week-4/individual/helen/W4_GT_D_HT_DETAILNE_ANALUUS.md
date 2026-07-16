# Nädal 4 – Roll D detailne analüüs

## 1. Projekti kontekst

UrbanStyle’i tegevjuht Kristi Tamm vajas juhatuse koosolekuks lühikesi ja kontrollitud koondnumbreid. Roll D ülesanne oli hinnata turunduskanalite efektiivsust, ühendades müügi-, kliendi- ja veebikülastuste andmed.

Analüüsi põhiküsimus oli:

> Millised turunduskanalid toovad kõige rohkem kliente, tellimusi ja käivet ning millistes kanalites on suurim keskmine tellimusväärtus ja müük kliendi kohta?

## 2. Andmeallikad

| Tabel | Kasutus |
|---|---|
| `sales` | müügitehingud, kuupäevad, kliendid ja käive |
| `customers` | kliendi põhiandmed ja tabelite ühendamine |
| `web_logs` | veebikülastuse allikas ehk `source` |

`web_logs.csv` imporditi Supabase’i. Kontrollpäringu tulemus oli **50 000 rida**.

Täiendav andmekvaliteedi kontroll näitas:

- **9 415 anonüümset logirida**;
- anonüümsete logide osakaal **18,83%**;
- `source` väljal **19 erinevat väärtust**;
- sama sisuline kanal esineb erinevate nimetustega.

Näited erinevatest kirjapiltidest:

- `google_organic`
- `Google Organic`
- `google organic`
- `Facebook`
- `facebook_ads`
- `Facebook Ads`
- `FB`
- `fb_ads`

## 3. Juhendi kohustuslikud päringud

### Päring 1 – kanalite koondandmed

Arvutati kanali kaupa:

- unikaalsete klientide arv;
- unikaalsete tellimuste arv;
- kogukäive;
- keskmine tellimusväärtus.

Kasutatud põhielemendid:

- `JOIN` ja `LEFT JOIN`;
- `GROUP BY`;
- `COUNT(DISTINCT ...)`;
- `SUM`;
- `AVG`;
- `ROUND`;
- `COALESCE`.

### Päring 2 – kanali efektiivsus CTE abil

CTE-dega eraldati:

1. kanali kogumüük ja tellimuste arv;
2. kanali klientide arv;
3. müük kliendi kohta.

`HAVING` filtriga jäeti analüüsi kanalid, millel oli vähemalt kümme tellimust.

### Päring 3 – kuised trendid

Kanalite tulemused grupeeriti kuu ja kanali järgi. Arvutati:

- unikaalsed kliendid;
- tellimused;
- kogukäive.

`HAVING` filtriga jäeti alles kanali-kuud, millel oli vähemalt viis tellimust.

## 4. Kriitiline kvaliteedikontroll

### Probleem

Ühel kliendil võib `web_logs` tabelis olla mitu logirida. Kui `sales` ühendatakse `web_logs` tabeliga ainult `customer_id` alusel, liitub sama müük kliendi iga logireaga.

Kontrolltulemused:

| Kontroll | Müügiread | Kogukäive |
|---|---:|---:|
| `sales` enne ühendamist | 10 118 | 2 909 177,98 € |
| otsese kolme tabeli JOIN-i järel | 121 131 | 34 527 628,19 € |

Seega ei olnud juhendi otsese JOIN-i `SUM(total_price)` ja `AVG(total_price)` tulemused juhtimisaruandluseks usaldusväärsed.

`COUNT(DISTINCT sale_id)` säilitas küll unikaalsete tellimuste arvu, kuid `SUM` ja `AVG` töötasid kordistatud ridadel.

## 5. Valideeritud lahendus

Koostasin lisapäringu, mis:

1. järjestab iga kliendi `web_logs` read kuupäeva järgi;
2. kasutab `ROW_NUMBER() OVER (PARTITION BY customer_id ...)`;
3. jätab igale kliendile ühe viimase teadaoleva kanali;
4. ühendab selle tulemuse müükidega;
5. agregeerib müügid alles pärast ühe kanali määramist.

Kasutatud reegel:

> Kõik kliendi müügid omistatakse tema viimasele teadaolevale turunduskanalile.

### Piirang

See reegel väldib müükide kordistumist, kuid ei tõesta, et kliendi viimane veebiallikas põhjustas kõik tema ostud. Tegemist on lihtsustatud kliendipõhise omistamisega, mitte tehingupõhise attribution-mudeliga.

## 6. Valideeritud kanalite koond

Suurima kogukäibega kanalid olid:

| Kanal | Kliente | Tellimusi | Kogukäive | Keskmine tellimus |
|---|---:|---:|---:|---:|
| `google_organic` | 624 | 1 994 | 582 912,57 € | 292,33 € |
| `facebook_ads` | 326 | 1 563 | 453 275,00 € | 290,00 € |
| `direct` | 465 | 1 505 | 420 103,22 € | 279,14 € |
| Tundmatu / kanal puudub | 90 | 1 338 | 383 127,19 € | 286,34 € |
| `email_campaign` | 275 | 1 024 | 300 296,85 € | 293,26 € |
| `instagram` | 243 | 822 | 247 965,12 € | 301,66 € |
| `google_ads` | 196 | 664 | 185 438,12 € | 279,27 € |
| `tiktok` | 127 | 463 | 127 929,88 € | 276,31 € |

### Tõlgendus

`google_organic` oli suurima kogukäibega ja tõi kõige rohkem tellimusi. See ei tähenda siiski automaatselt, et kanalil oli parim ROI, sest:

- orgaanilise ja tasulise turunduse kulustruktuur on erinev;
- kampaaniate kulusid ei ole andmestikus;
- kanalite nimed ei ole veel ühtlustatud;
- omistamine on tehtud kliendi viimase teadaoleva kanali järgi.

## 7. Müük kliendi kohta ja AOV

Toorväärtuste põhjal oli suurim müük kliendi kohta grupis **„Tundmatu / kanal puudub” – 4 256,97 € kliendi kohta**. Seda ei saa käsitleda parima turunduskanalina, sest kanal pole tuvastatud.

Tuvastatud source-väärtustest oli kõrgeim müük kliendi kohta väärtusel **`Google Organic` – 1 700,21 € kliendi kohta**. Tulemus ei ole lõplikult võrreldav enne kanalite nimetuste standardiseerimist.

Kõrgeim keskmine tellimusväärtus oli eraldi väärtusel **`google organic` – 311,37 €**. Ka seda väärtust tuleb käsitleda sama piiranguga.

Seetõttu on juhtkonna jaoks usaldusväärsem keskenduda:

- suure mahuga standardsele kanalile `google_organic`;
- valideeritud kogukäibele ja tellimuste arvule;
- kuisele trendile;
- andmekvaliteedi parandamise vajadusele.

## 8. Kuine trend

`google_organic` käive muutus 2024. aasta lõpus järsult:

| Kuu | Käive |
|---|---:|
| oktoober 2024 | 32 353,14 € |
| november 2024 | 13 834,38 € |
| detsember 2024 | 33 572,86 € |

Novembrist detsembrini:

- kasv eurodes: **19 738,48 €**;
- kasv protsentides: **142,7%**;
- tellimuste arv detsembris: **111**.

Kasv on oluline signaal, kuid seda tuleks kontrollida koos kampaaniakalendri, hooajalisuse ja reklaamikuludega.

## 9. Ärilised järeldused

1. **`google_organic` on suurima mahuga tuvastatud kanal.**  
   Seda kanalit tasub toetada SEO, sisuturunduse ja maandumislehtede kvaliteedi kaudu.

2. **Detsembri kasv vajab põhjuse analüüsi.**  
   Tuleb võrrelda kampaaniaid, hooajalisust, sortimenti ja tellimuste väärtust.

3. **Kanalite nimetused tuleb standardiseerida.**  
   Vastasel juhul jaguneb sama kanal mitmeks grupiks ja juhtimisraport moonutub.

4. **Anonüümne ja teadmata kanaliga liiklus on oluline.**  
   Tuvastamata allikaga müükide suur maht vähendab attribution-analüüsi usaldusväärsust.

5. **ROI arvutamiseks tuleb lisada kulud.**  
   Vajalikud on vähemalt kampaania-, kanali- ja perioodipõhised turunduskulud.

## 10. Soovitus järgmisteks sammudeks

- luua `source` väärtuste standardiseerimise reegel;
- siduda veebikülastus konkreetse ostuga ajaliselt;
- lisada kampaania ID ja turunduskulud;
- eristada esimese ja viimase kontakti kanal;
- kontrollida tulemusi Roll A müügikoondiga;
- dokumenteerida attribution-reegel juhtimisaruandes.

## 11. Õpitulemus

Selle töö käigus rakendasin:

- `GROUP BY` ja agregaatfunktsioone;
- `HAVING` filtrit;
- mitme tabeli `JOIN`-e;
- CTE-sid;
- `ROW_NUMBER()` ja `LAG()` window function’e;
- ridade kordistumise kontrolli;
- analüütilise tulemuse eristamist tehniliselt töötavast, kuid äriliselt ebausaldusväärsest päringust.

## 12. Seotud failid

- [SQL-päringud](./W4_GT_D_HT_Turunduskampaaniate%20efektiivsus.sql)
- [Kuvatõmmised ja CSV-tulemused](./kuvat%C3%B5mmised/)
- [Lühike README](./README.md)
- [Presentatsiooni kokkuvõte](./W4_GT_D_HT_PRESENTATSIOONI_KOKKUVOTE.md)
- [Grupi ühine töö](../../group/)
