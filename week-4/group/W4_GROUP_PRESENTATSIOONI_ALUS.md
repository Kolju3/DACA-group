# Nädal 4 – grupi presentatsiooni alus

**Meeskond:** Operations Intelligence  
**Sihtrühm:** Kristi Tamm, CEO; Anna Mets, Marketing Lead  
**Ametlik formaat:** ligikaudu 3 minutit  
**Põhimõte:** esitle tulemust ja juhtimisotsust, mitte SQL-i kirjutamise protsessi  

---

# Ametlik 5-slaidiline juhtkonna versioon

## Slaid 1 – 10 118 müügireast viis juhtimisnumbrit

### Pealkiri

**UrbanStyle’i 10 118 müügitehingut koondusid viieks juhtimisnäitajaks**

### Slaidile

- analüüsiti müüki, kliente, tootekategooriaid ja turundust;
- kasutati `GROUP BY`, `HAVING`, CTE-sid ja window function’e;
- kontrollväärtus: **2 909 177,98 € käivet**;
- eesmärk: leida numbrid, mille põhjal juhtkond saab otsustada.

### Kõnealus – 20 sekundit

„Meie meeskond koostas UrbanStyle’i juhatuse jaoks agregatsiooniraporti. Analüüsisime müüki, kliendigruppe, tootekategooriaid ja turunduskanaleid. Kõigi müüki puudutavate tulemuste kontrollväärtus oli 10 118 tehingut ja 2,91 miljonit eurot käivet.”

### Visuaal

Üks suur KPI: **2,91 mln € / 10 118 müüki**  
All neli väikest domeenimärget: Müük – Kliendid – Tooted – Turundus.

---

## Slaid 2 – Kristile: TOP 5 koondnumbrit

### Pealkiri

**2024 kasv, väärtuslikud kliendid ja google_organic annavad juhtkonnale selge fookuse**

### Slaidile – viis KPI-kaarti

1. **2 909 177,98 €**  
   kogu käive, 10 118 müüki

2. **+19,08%**  
   2024 käive võrreldes 2023. aastaga

3. **18 VIP-klienti**  
   keskmine käive 745,20 €*

4. **4 121 ühikut**  
   `meeste_riided` müüdud kogus**

5. **666 444,98 €**  
   `google_organic`, 2 273 tellimust

### Jaluse märkused

\* Roll B analüüsitud kliendikogum; populatsioon vajab lõplikku ristkontrolli.  
\** Müüdud kogus, mitte tegelik laoseis.

### Kõnealus – 50 sekundit

„Kogu müügikäive oli 2,91 miljonit eurot. 2024. aasta käive kasvas 2023. aastaga võrreldes 19,08%. Kliendianalüüsis eristus 18 VIP-klienti keskmise käibega 745 eurot. Toodetest oli suurima müügikogusega meeste riiete kategooria – 4 121 ühikut. Turunduses oli suurima valideeritud müügimahuga google_organic, millele seostus 666 tuhat eurot käivet ja 2 273 tellimust.”

### Visuaal

Viis võrdselt suurt KPI-kaarti. Ärge lisage sellele slaidile täiendavat tabelit.

---

## Slaid 3 – Suurim üllatus: vale JOIN muutis 2,91 miljonit 34,53 miljoniks

### Pealkiri

**Tehniliselt töötav JOIN ülehindas käivet 11,87 korda**

### Slaidile

| Kontroll | Õige lähteväärtus | Otsene JOIN |
|---|---:|---:|
| Ridu | 10 118 | 121 131 |
| Unikaalseid müüke | 10 118 | 9 130 |
| Käive | 2,91 mln € | 34,53 mln € |

- ühe kliendi mitu veebilogirida kordistasid müüke;
- `INNER JOIN customers` jättis samal ajal välja 988 müüki;
- lõplik analüüs kasutas igale kliendile ühte viimast teadaolevat kanalit.

### Kõnealus – 40 sekundit

„Suurim üllatus ei olnud üksik kanal või kategooria, vaid andmekvaliteet. Otsene kolme tabeli JOIN andis 34,53 miljonit eurot käivet ehk 11,87 korda tegelikust rohkem ja jättis samal ajal välja 988 müüki. Põhjuseks oli mitu veebilogirida ühe kliendi kohta. Seetõttu valisime enne agregeerimist igale kliendile ühe viimase teadaoleva standardiseeritud kanali.”

### Visuaal

Kõrvuti kaks numbrit:

- **2,91 mln € – kontrollväärtus**
- **34,53 mln € – vale JOIN-i tulemus**

Nende vahel märge **11,87×**.

---

## Slaid 4 – Kolm juhtimisotsust

### Pealkiri

**Kasv tuleb siduda kliendi hoidmise, varude ja mõõdetava turundusega**

### Slaidile

### 1. Kliendid

**Hoida VIP-e, kasvatada Regular-segmenti ja automatiseerida uute klientide kordusostuteekond.**

### 2. Tooted ja varud

**Planeerida `meeste_riided` ja `jalanõusid` kategooriaid, kuid lisada enne tellimisotsuseid tegelik laoseis ja müügikiirus.**

### 3. Turundus

**Toetada suure mahuga `google_organic` kanalit ning siduda tasulised kanalid kampaaniakulude ja tehingupõhise atribuutikaga.**

### Kõnealus – 40 sekundit

„Soovitame kolme tegevust. Esiteks hoida VIP-kliente personaalselt ja kasvatada Regular-segmenti. Teiseks siduda kõrge müügikogusega kategooriad tegeliku laoseisu ja tarneinfoga. Kolmandaks toetada google_organic kanalit, kuid võrrelda tasuliste kanalite efektiivsust alles pärast kulude ja kampaaniaandmete lisamist.”

### Visuaal

Kolm horisontaalset otsuseplokki: Kliendid – Varud – Turundus.

---

## Slaid 5 – Piirangud ja järgmine samm

### Pealkiri

**Järgmine kvaliteeditase nõuab ühiseid definitsioone ja täiendavaid andmeid**

### Slaidile

Puudusid või vajavad täpsustamist:

- kampaaniakulud ja tehingu–sessiooni seos;
- omahind, marginaal ja tegelik laoseis;
- kliendisegmentide täielik lähtepopulatsioon;
- 2025.–2026. aasta andmekatte terviklikkus;
- tagastused ja tühistatud müügid.

**Järgmine samm:** ühtne valideeritud CEO-raport, kus iga KPI juures on periood, definitsioon, lähtepopulatsioon ja kontrollsumma.

### Lõppsõnum

**UrbanStyle saab müüki kasvatada väärtuslike klientide, tugeva nõudlusega kategooriate ja toimivate kanalite kaudu ainult siis, kui juhtimisnumbrid on enne otsustamist ristkontrollitud.**

### Kõnealus – 30 sekundit

„Me ei saanud arvutada tegelikku turunduse ROI-d ega täielikku varuriski, sest puudusid kulud, marginaal ja laoseisu detailid. Samuti vajab kliendisegmentide populatsioon täpsustamist. Järgmine samm on ühtne CEO-raport, kus iga number on seotud kindla perioodi, definitsiooni ja kontrollsummaga.”

---

# 3-minutiline ajajaotus

| Aeg | Sisu |
|---|---|
| 0:00–0:20 | Kontekst ja kontrollväärtus |
| 0:20–1:10 | TOP 5 koondnumbrit |
| 1:10–1:50 | Suurim üllatus – JOIN-i moonutus |
| 1:50–2:30 | Kolm juhtimisotsust |
| 2:30–3:00 | Piirangud ja lõppsõnum |

---

# Laiendatud 7-slaidiline portfoolioversioon

## Slaid 1 – SQL agregatsioonist juhtimisotsusteni

Kontekst, andmed, rollid ja kontrollväärtus.

## Slaid 2 – Juhtkonna TOP 5

Viis KPI-kaarti ametliku 3-minutilise versiooni järgi.

## Slaid 3 – 2024 kasvas 19,08% ja detsember oli tippkuu

Soovitatav visuaal: 2023–2024 kuise käibe joondiagramm või aastate võrdlustulbad.

## Slaid 4 – VIP-kliente on vähe, kuid nende väärtus on kõrge

Näita VIP, Regular ja Uus segmenti. Lisa nähtav märkus: „Roll B analüüsitud kogum, n = 214; populatsiooni definitsioon vajab täpsustamist.”

## Slaid 5 – Suurima müügikogusega kategooria oli `meeste_riided`

Näita kategooriate müüdud koguseid ja keskmisi hindu. Lisa nähtav märkus: „Müüdud kogus ei võrdu laoseisuga.”

## Slaid 6 – `google_organic` tõi suurima valideeritud müügimahu

Soovitatav visuaal: standardiseeritud kanalite käibe horisontaalne tulpdiagramm. `unknown` kuvada eraldi hoiatusgrupina.

## Slaid 7 – Vale JOIN oli suurim juhtimisrisk

Näita 2,91 mln € vs 34,53 mln €, kolm soovitust, puuduvad andmed ja lõppsõnum.

---

# Esitluse sisureeglid

## Kasuta

- „valideeritud käive”;
- „Roll B analüüsitud kliendikogum”;
- „müüdud kogus”;
- „viimane teadaolev kliendikanal”;
- „kanalite efektiivsus”;
- „tegelik ROI ei ole kuludeta arvutatav”.

## Väldi

- Roll A ligikaudu 50% näitamist kogu ettevõtte kinnitatud aastakasvuna;
- 214 kliendi nimetamist kogu UrbanStyle’i kliendibaasiks;
- müüdud koguse nimetamist laoseisuks;
- `unknown` grupi käsitlemist päris turunduskanalina;
- „parim ROI” väljendit;
- otsese JOIN-i käibe kasutamist juhtimisnumbrina;
- 2025. aasta languse nimetamist ärikriisiks enne andmekatte kontrolli.

---

# Võimalikud küsimused ja vastused

## Miks kasutame 19,08% kasvu, mitte Roll A kokkuvõtte ligikaudu 50%?

Täieliku `sales` tabeli aastakoond annab 2024. aasta käibe kasvuks 19,08%. Ligikaudu 50% võib põhineda teisel perioodil, alamkogumil või indeksil. Grupi juhtimisnumbrina kasutame kontrollitud kogu ettevõtte aastavõrdlust.

## Kas 18 VIP-klienti on kogu kliendibaasi tulemus?

See on Roll B esitatud segmentatsiooni tulemus. Segmentide kogum sisaldab 214 klienti ja vajab kasutatud JOIN-i ning `HAVING`-filtri dokumenteerimist enne kogu kliendibaasile üldistamist.

## Kas `meeste_riided` 4 121 tähendab laoseisu?

Ei. See on müüdud kogus. Tegeliku varuriski hindamiseks on vaja hetke laoseisu, laoliikumisi, müügikiirust, tellimispunkti ja tarneaega.

## Kas `google_organic` oli parima ROI-ga kanal?

Seda ei saa väita. Kanalil oli suurim valideeritud müügimaht, kuid kampaaniakulud puuduvad ja kanal on kliendipõhiselt, mitte tehingupõhiselt omistatud.

## Miks oli otsese JOIN-i käive nii suur?

Ühel kliendil oli mitu veebilogirida. Sama müük liitus kliendi iga logireaga ja läks `SUM`-i mitu korda.

## Miks kadus JOIN-is 988 müüki?

`INNER JOIN customers` jättis välja müügid, mille `customer_id` ei leidnud klienditabelis vastet või puudus.

---

# Soovitatavad visuaalid

1. viis KPI-kaarti TOP 5 jaoks;
2. 2023 vs 2024 käibe võrdlus;
3. kliendisegmentide kolm tulpa;
4. kategooriate müüdud koguste horisontaalne tulpdiagramm;
5. standardiseeritud turunduskanalite käibe horisontaalne tulpdiagramm;
6. 2,91 mln € vs 34,53 mln € JOIN-i kontrollvõrdlus.

Kõik graafiku pealkirjad peavad olema järeldused, mitte neutraalsed nimetused.

---

# Ühe lause lõppjäreldus

**Kasvuotsused peavad ühendama müügi, kliendid, tooted ja turunduse, kuid ükski koondnumber ei jõua juhtkonnani ilma perioodi, populatsiooni ja JOIN-i kontrollita.**
