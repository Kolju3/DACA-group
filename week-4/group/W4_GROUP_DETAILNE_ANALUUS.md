# Nädal 4 – grupi detailne analüüs ja valideerimisraport

**Meeskond:** Operations Intelligence  
**Projekt:** UrbanStyle.ltd  
**Teema:** SQL agregatsioon  
**Sihtrühm:** Kristi Tamm, CEO; Anna Mets, Marketing Lead  

## 1. Analüüsi eesmärk

Nädal 4 grupitöö eesmärk oli muuta detailandmed juhtkonnale kasutatavateks koondnäitajateks. Analüüs hõlmas nelja domeeni:

1. müügi koondandmed;
2. kliendigruppide analüüs;
3. tootekategooriad ja inventuuristatistika;
4. turunduskanalite efektiivsus.

Ametlik ühine väljund peab esitama Kristile viis koondnumbrit, suurima üllatuse, tegevussoovituse ja puuduvad andmed. Tulemused peavad põhinema tegelikel päringutulemustel, mitte juhendi näidisnumbritel.

## 2. Kasutatud SQL-võtted

| Võte | Rakendus |
|---|---|
| `GROUP BY` | Kuude, kategooriate, kliendisegmentide ja turunduskanalite koondamine |
| `COUNT()` ja `COUNT(DISTINCT ...)` | Ridade, tellimuste, klientide ja toodete loendamine |
| `SUM()` | Käibe ja müüdud koguste arvutamine |
| `AVG()` | Keskmise tellimuse, kliendikäibe ja tootehinna arvutamine |
| `MIN()` / `MAX()` | Hinnavahemike ja perioodide kontroll |
| `HAVING` | Grupeeritud tulemuste filtreerimine |
| CTE / `WITH` | Mitmeastmelise loogika eraldamine |
| `CASE WHEN` | Kliendisegmentide ja kanalite standardiseerimine |
| `ROW_NUMBER()` | Kliendi viimase teadaoleva kanali valimine |
| `LAG()` | Kuust-kuusse muutuse arvutamine |
| `DATE_TRUNC()` | Müügi koondamine kuude kaupa |

## 3. Allikate ja tulemuste usaldusjärjekord

Grupi sünteesis kasutati järgmisi põhimõtteid:

1. kontrollitud SQL-i väljundid ja CSV-tulemused;
2. dokumenteeritud kontrollsummad;
3. individuaalsed README-d ja analüütilised kokkuvõtted;
4. SQL-failid arvutusloogika kontrollimiseks;
5. nädala juhend rollide ja väljundi formaadi määratlemiseks.

Kui sama KPI kohta esines erinevaid väärtusi, eelistati tulemust, mille periood, filter ja kontrollsumma olid selgelt dokumenteeritud. Lahendamata vastuolusid ei esitata kinnitatud juhtimisnumbrina.

## 4. Kogu müügi kontrollväärtus

Täieliku `sales` tabeli kontroll:

| Näitaja | Tulemus |
|---|---:|
| Müügiridu | 10 118 |
| Unikaalseid `sale_id` väärtusi | 10 118 |
| Kogukäive | 2 909 177,98 € |
| 2023 käive | 1 234 758,90 € |
| 2024 käive | 1 470 358,02 € |
| 2024 kasv vs 2023 | 19,08% |
| 2024 tellimuste kasv vs 2023 | 20,19% |
| Suurim kuine käive | 170 623,28 € – detsember 2024 |

See on grupi peamine referentsväärtus. Kõik müüki sisaldavad alamkoondid peavad säilitama õige tellimuste arvu ja kogukäibe või selgitama täpselt, milline filter erinevuse põhjustab.

## 5. Roll A – müügi koondandmed

### Esitatud fookus

Roll A analüüsis:

- müüki asukohtade järgi;
- tootekategooriate käivet;
- sesoonsust;
- 2023.–2026. aasta muutusi;
- Online'i ja Tartu arengut.

Individuaalses kokkuvõttes esitati:

- ligikaudu 50% kasv 2023–2024;
- suvekuude ligikaudu 20% kõrgem müük;
- Online ja Tartu kui kiiremini kasvanud piirkonnad;
- tugev langus 2025. aastal.

### Ristkontroll

Täieliku `sales` tabeli aastakoond näitab 2024. aasta käibe kasvuks 19,08%, mitte ligikaudu 50%.

Võimalikud erinevuse põhjused:

- valitud asukoha või kategooria alamkogum;
- erinev perioodi algus ja lõpp;
- kasv indeksi, mitte tegeliku käibe alusel;
- 2023. aasta mittetäielik võrdlusperiood;
- erinev filter või tabeliversioon.

### QA otsus

| Kontroll | Staatus |
|---|---|
| Müügitrendid on analüüsitud | OK |
| Kasutatud on agregatsioone ja CTE-sid | OK |
| Ligikaudu 50% kasv on kogu ettevõtte aastakasvuna kinnitatud | EI |
| Juhtimisnumbrina kasutatav kasv | 19,08% |

### Äriline tõlgendus

2024 oli tugevam kui 2023. Tellimuste arv kasvas veidi kiiremini kui käive, mis viitab keskmise tellimuse väikesele langusele. Detsembri kõrge tulemus osutab aasta lõpu hooajalisusele. 2025.–2026. aasta järsk langus ei ole ilma andmekatte kontrollita piisav tõend tegeliku äritegevuse vähenemise kohta.

## 6. Roll B – kliendigruppide analüüs

### Esitatud segmentatsioon

| Segment | Definitsioon | Kliente | Keskmine käive |
|---|---|---:|---:|
| VIP | üle 500 € | 18 | 745,20 € |
| Regular | 150–500 € | 54 | 312,50 € |
| Uus | alla 150 € | 142 | 64,80 € |
| **Kokku** |  | **214** |  |

Esitatud täiendavad järeldused:

- VIP-klientide põhilised asukohad on Tallinn ja Tartu;
- Regular-segment moodustab esitatud analüüsis 42,7% käibest;
- uute klientide suur arv toetab automatiseeritud kordusostukampaaniat.

### Ristkontroll

Avalikus individuaalses kaustas on README ja koondpilt, kuid eraldi SQL-faili või CSV-väljundit ei ole grupi analüüsi jaoks nähtavalt dokumenteeritud.

Segmentide summa 214 on oluliselt väiksem kui kogu müügiandmestiku kliendimaht. See võib olla põhjendatud näiteks `INNER JOIN`, `HAVING` või kordusostu filtriga, kuid populatsiooni definitsioon peab olema README-s ja esitluses selgelt välja toodud.

### QA otsus

| Kontroll | Staatus |
|---|---|
| Segmentide piirid on määratud | OK |
| Segmentide koond on esitatud | OK |
| Segmentide lähtepopulatsioon on dokumenteeritud | VAJAB TÄPSUSTAMIST |
| 214 klienti on kogu kliendibaas | EI OLE TÕENDATUD |
| 18 VIP-klienti võib esitada | JAH, Roll B analüüsitud kogumi piiranguga |

### Äriline tõlgendus

VIP-segment vajab personaalset hoidmist. Regular-segment on tõenäoliselt kõige realistlikum kasvukoht, sest nende väärtus on juba olemas, kuid jääb alla VIP-piiri. Uute klientide suur arv toetab automatiseeritud onboarding'u ja kordusostu kommunikatsiooni.

## 7. Roll C – tootekategooriad ja inventuur

### Esitatud kategooriatulemused

| Kategooria | Tooteid | Keskmine hind | Min hind | Max hind | Müüdud kogus |
|---|---:|---:|---:|---:|---:|
| `meeste_riided` | 82 | 189,91 € | 48,85 € | 374,54 € | 4 121 |
| `jalanõusid` | 73 | 214,10 € | 58,49 € | 434,08 € | 3 737 |
| `laste_riided` | 70 | 85,30 € | 22,70 € | 168,82 € | 3 686 |
| `naiste_riided` | 70 | 192,58 € | 32,93 € | 351,33 € | 3 604 |
| `aksessuaarid` | 67 | 125,71 € | 13,53 € | 231,13 € | 3 231 |

Keskmine müüdud kogus jäi kategooriates esitatud päringu järgi ligikaudu 1,78–1,84 vahele.

### Ametliku ülesande võrdlus

Roll C ametlik ülesanne nõudis:

- tootekategooriate koondit;
- müüdud koguste analüüsi;
- laoseisu või `inventory_movements` kasutamist;
- probleemsete kategooriate leidmist;
- inventuuri ärisoovitust.

Avalik väljund tõendab tootekategooriate, hindade ja müüdud koguste analüüsi. Laoseisu, laoliikumiste, ülevaru või juurde tellimise tulemusi ei ole esitatud.

### QA otsus

| Kontroll | Staatus |
|---|---|
| Kategooriate `GROUP BY` koond | OK |
| Müüdud kogus kategooria järgi | OK |
| Window function toodete järjestamiseks | OK |
| Tegelik laoseis või `inventory_movements` analüüs | PUUDUB |
| Ülevaru või juurde tellimise risk | EI OLE KVANTIFITSEERITUD |

### Äriline tõlgendus

`meeste_riided` on suurima müügikogusega kategooria ja `jalanõusid` kõrgeima keskmise hinnaga kategooria. Nende varude planeerimine on prioriteetne, kuid ainult müüdud kogus ei näita, kas laoseis on piisav või liiga suur. Enne ostutellimuste otsust tuleb lisada tegelik laoseis, tellimispunkt, müügikiirus ja tarneaeg.

## 8. Roll D – turunduskanalite efektiivsus

### Andmepuhastus

`web_logs` tabelis oli:

| Näitaja | Tulemus |
|---|---:|
| Logiridu | 50 000 |
| Tuvastatud kliendiga logisid | 40 585 |
| Anonüümseid logisid | 9 415 |
| Anonüümsete osakaal | 18,83% |
| Algseid `source` väärtusi | 19 |
| Standardiseeritud kanaleid | 10 |

Algne `source` säilitati ja analüüsiks loodi `source_clean`.

### Kriitiline JOIN-i kontroll

| Kontroll | `sales` enne JOIN-i | Otsene JOIN |
|---|---:|---:|
| Ridu | 10 118 | 121 131 |
| Unikaalseid müüke | 10 118 | 9 130 |
| Käive | 2 909 177,98 € | 34 527 628,19 € |

Põhjused:

- `INNER JOIN customers` eemaldas müügid, millel puudus kliendivaste;
- ühe kliendi mitu `web_logs` rida kordistasid iga sobiva müügi;
- `COUNT(DISTINCT sale_id)` ei paranda kordistatud `SUM`-i ja `AVG`-d.

### Valideeritud lahendus

Igale kliendile valiti üks viimane teadaolev kanal:

```sql
ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY visit_date DESC, log_id DESC
)
```

Seejärel agregeeriti müük standardiseeritud kanali järgi.

### Valideeritud tulemused

| Kanal | Kliente | Tellimusi | Käive | Keskmine tellimus | Müük kliendi kohta |
|---|---:|---:|---:|---:|---:|
| `google_organic` | 684 | 2 273 | 666 444,98 € | 293,20 € | 974,33 € |
| `facebook_ads` | 351 | 1 635 | 469 933,25 € | 287,42 € | 1 338,84 € |
| `direct` | 465 | 1 505 | 420 103,22 € | 279,14 € | 903,45 € |
| `unknown` | 90 | 1 338 | 383 127,19 € | 286,34 € | 4 256,97 €* |
| `email_campaign` | 275 | 1 024 | 300 296,85 € | 293,26 € | 1 091,99 € |
| `instagram` | 259 | 877 | 262 112,79 € | 298,87 € | 1 012,02 € |

\* `unknown` ei ole päris turunduskanal. NULL `customer_id` ei lähe klientide loendisse, kuid selle käive sisaldub grupis, mistõttu müük kliendi kohta ei ole võrreldav.

### QA otsus

| Kontroll | Staatus |
|---|---|
| Kanalite kirjapildid standardiseeritud | OK |
| JOIN-i ridade kordistumine kontrollitud | OK |
| Lõplik käive vastab `sales` kontrollsummale | OK |
| Kanal seotakse konkreetse tehinguga | EI |
| Tegelik ROI on arvutatav | EI – kulud puuduvad |

### Äriline tõlgendus

`google_organic` on suurima valideeritud müügimahuga kanal. `facebook_ads` seostub kõrgeima müügiga kliendi kohta ning `instagram` kõrgeima keskmise tellimusega. Kanalite paremusjärjestus ei ole ROI, sest kulud puuduvad ja omistamine toimub kliendi viimase teadaoleva kanali, mitte tehingu alusel.

## 9. Rollideülene süntees

### 9.1. Müügikasv ja nõudlus

2024. aasta kasv ja detsembri tipp viitavad nõudluse tugevnemisele ning hooajalisusele. See toetab varude ja kampaaniate varasemat planeerimist.

### 9.2. Kliendi- ja kanalistrateegia

VIP-klientide personaalne hoidmine ja Regular-segmendi kasvatamine tuleks siduda kanalitega:

- orgaanilise otsingu kaudu tulnud suure mahuga kliendid;
- `facebook_ads` kanaliga seotud kõrgem kliendiväärtus;
- e-posti kampaaniad kordusostu toetamiseks.

Praegused andmed ei võimalda kliendisegmenti ja turunduskanalit tehingupõhiselt ühendada.

### 9.3. Tooted ja varud

Kõrge müügikogusega `meeste_riided` ja kõrge hinnatasemega `jalanõusid` on prioriteetsed kategooriad. Nende kasumlikkust ja varuriski ei saa hinnata ilma omahinna, marginaali, laoseisu ja müügikiiruseta.

### 9.4. Andmekvaliteet kui juhtimisrisk

Kõige suurem üllatus oli, et vale JOIN muutis 2,91 miljoni euro suuruse käibe 34,53 miljoniks. Andmekvaliteedi kontroll ei ole tehniline lisategevus, vaid juhtimisaruandluse kohustuslik osa.

## 10. Kristile soovitatavad TOP 5 numbrit

| # | Number | Domeen | Miks see on juhtkonnale oluline |
|---:|---|---|---|
| 1 | **2 909 177,98 € käivet; 10 118 müüki** | Kogu ettevõte | Kinnitatud kontrollsumma |
| 2 | **2024 käive +19,08% vs 2023** | Müük | Näitab aastast arengut |
| 3 | **18 VIP-klienti, keskmine käive 745,20 €** | Kliendid | Näitab hoidmist vajavat kõrge väärtusega segmenti |
| 4 | **4 121 müüdud ühikut kategoorias `meeste_riided`** | Tooted | Näitab suurimat koguselist nõudlust |
| 5 | **666 444,98 € ja 2 273 tellimust kanalist `google_organic`** | Turundus | Näitab suurima valideeritud müügimahuga kanalit |

Juhtkonna slaidil tuleb lisada märkus, et kliendi number põhineb Roll B analüüsitud kliendikogumil ning tootekategooria number ei ole laoseisu mõõdik.

## 11. Suurim üllatus

**Otsene turunduse JOIN ülehindas käivet 11,87 korda ja eemaldas samal ajal 988 müüki.**

See on olulisem kui üksiku kanali või kategooria edetabel, sest vale liitmisloogika oleks võinud muuta kogu juhtimisotsuse aluse.

## 12. Juhtimissoovitused

### Otsus 1 – kasvatada väärtuslikke kliendisuhteid

- hoida VIP-kliente personaalselt;
- kujundada Regular-segmendile ristmüük;
- automatiseerida uute klientide kordusostuteekond;
- valideerida segmentide populatsioon enne eelarve jaotamist.

### Otsus 2 – ühendada nõudlus tegeliku varuga

- jälgida `meeste_riided` ja `jalanõusid` kategooriaid;
- lisada laoseis, müügikiirus ja tarneaeg;
- eristada müügikaotuse risk ja ülevaru risk;
- mitte teha tellimisotsust ainult ajaloolise müügikoguse põhjal.

### Otsus 3 – parandada turunduse mõõtmist

- säilitada `source_clean` standard;
- lisada kampaania ID, UTM-parameetrid ja kulud;
- siduda müük sessiooni või lähima varasema külastusega;
- eristada orgaaniline, tasuline ja täpsustamata liiklus;
- uurida `unknown` grupi suurt käivet.

## 13. Puuduvad andmed

| Domeen | Puuduv info | Mõju |
|---|---|---|
| Müük | Tagastused ja tühistamised | Netokäive võib erineda |
| Kliendid | Segmentide täielik populatsioon ja filtri kirjeldus | Segmentide osakaalu ei saa kogu kliendibaasile üldistada |
| Tooted | Omahind ja marginaal | Kategooria kasumlikkust ei saa hinnata |
| Inventuur | Laoseis, laoliikumised, tellimispunkt ja tarneaeg | Ülevaru ja puudujääki ei saa kvantifitseerida |
| Turundus | Kampaaniakulud ja tehingupõhine seos | ROI-d ja põhjuslikku mõju ei saa arvutada |
| Periood | Täielik 2025.–2026. aasta andmekate | Hilisemat langust ei saa kindlalt tõlgendada |

## 14. Valideerimisraport

| Valdkond | Kontroll | Tulemus | Tegevus |
|---|---|---|---|
| Müük | Kogukäive ja tellimused | OK | Kasutada referentsväärtusena |
| Roll A | 2023–2024 kasv | PARANDA | Kasutada 19,08% või dokumenteerida teine filter |
| Roll B | Segmentide summa ja lähtepopulatsioon | KONTROLLI | Lisada SQL/CSV ning `HAVING`-filtri kirjeldus |
| Roll C | Kategooriad ja müüdud kogus | OK | Võib kasutada kategooriaanalüüsina |
| Roll C | Inventuuristatistika | PUUDULIK | Lisada `inventory_movements` või laoseis |
| Roll D | Kanalite standardiseerimine | OK | Kasutada `source_clean` |
| Roll D | Otsene JOIN | PARANDATUD | Kasutada ühe kanalireaga lahendust |
| Esitlus | TOP 5 numbrite ühine periood ja definitsioon | OSALISELT | Lisada numbrite juurde periood ja piirang |

## 15. Lõppjäreldus

UrbanStyle’i juhtimisotsused peaksid põhinema kolmel paralleelsel tegevusel:

1. kasvatada 2024. aastal tugevnenud müüki väärtuslike klientide ja toimivate kanalite kaudu;
2. siduda kõrge nõudlusega kategooriad tegeliku laoseisu ja marginaaliga;
3. muuta andmekvaliteedi kontroll iga raporti kohustuslikuks osaks.

**Kõige olulisem õppetund oli, et koondnumber on usaldusväärne ainult siis, kui selle lähtepopulatsioon, periood, JOIN-i loogika ja kontrollsumma on dokumenteeritud.**
