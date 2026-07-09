# Nädal 3: Müügi ja kliendiandmete ühendamine

**Roll:** A — Müük + kliendid  
**Autor:** Natalia  
**Andmebaas:** Supabase / PostgreSQL  
**Tabelid:** `sales`, `customers`  
**Põhiteema:** `INNER JOIN`, koondpäringud, kliendi- ja müügivaate ühendamine

---

## Projekti kontekst

UrbanStyle.ltd müügiandmeid tuleb analüüsida koos kliendiandmetega, et mõista, kes ostavad, millistest linnadest müük tuleb ja kuidas lojaalsustasemed müügiga seotud on.

Nädala 3 ülesande fookus oli ühendada `sales` ja `customers` tabelid `INNER JOIN` abil. See näitab ainult neid müügiridu, mille `customer_id` leiab vaste ka `customers` tabelist.

---

## Kasutatud SQL-loogika

Analüüsis kasutati järgmisi SQL-võtteid:

- `INNER JOIN` — müügi- ja klienditabeli ühendamiseks;
- `COUNT()` ja `COUNT(DISTINCT ...)` — müükide ja klientide arvu leidmiseks;
- `SUM(total_price)` — kogumüügi arvutamiseks;
- `GROUP BY` — klientide, linnade ja lojaalsustasemete lõikes koondamiseks;
- `ORDER BY ... DESC` — suurimate tulemuste ette toomiseks;
- `HAVING` ja alampäring — üle keskmise kogumüügiga klientide leidmiseks.

---

## Failid

| Fail | Sisu |
|---|---|
| [SQL-fail](<./W3_GT_A-Müügi ja klientide ühendamine.sql>) | Kõik kasutatud SQL-päringud |
| [1. Kliendid, kes on ostnud](<./1. Kliendid kes on ostnud (INNER JOIN).png>) | Näide müügiridadest koos kliendiandmetega |
| [2. TOP 10 klienti kogumüügi järgi](<./2. TOP 10 klienti kogumüügi järgi.png>) | Suurima kogumüügiga kliendid |
| [3. Müügianalüüs linnade kaupa](<./3. Müügianalüüs linnade kaupa.png>) | Müügi ja klientide jaotus linnade lõikes |
| [4. Müük lojaalsustasemete kaupa](<./4. Müük lojaalsustasemete kaupa.png>) | Müük lojaalsustasemete lõikes |
| [5. Lisakontroll INNER JOINist välja jäänud ridade kohta](<./5. Lisakontroll_ kui palju sales ridu jäi INNER JOINist välja.png>) | Andmekvaliteedi lisakontroll |
| [6. Üle keskmise kogumüügiga kliendid](<./6. Kliendid, kelle kogumüük on üle keskmise kliendimüügi.png>) | Täiendav kliendisegmendi analüüs |

---

## 1. Kliendid, kes on ostnud

Esimene päring ühendas `sales` ja `customers` tabelid ning näitas müügiridu koos kliendi nime, e-posti, linna, tehingu kuupäeva ja müügisummaga.

**Mida see näitas?**

`INNER JOIN` tulemus sisaldab ainult neid müügiridu, millel on vastav klient olemas `customers` tabelis. See annab analüüsiks usaldusväärsema kliendivaate, kuid jätab kõrvale need müügiread, mille kliendivaste puudub.

Näitevaates olid suurimate tehingute seas järgmised kliendid:

| Klient | Linn | Müügisumma |
|---|---:|---:|
| Madis Roots | Valga | 2170.40 |
| Laura Tammik | Pärnu | 2013.10 |
| Kati Teder | Tallinn | 1881.65 |
| Toomas Sild | Tartu | 1881.65 |
| Tiina Pärn | Tartu | 1876.70 |

---

## 2. TOP 10 klienti kogumüügi järgi

Teine päring koondas müügid kliendi kaupa ja sorteeris kliendid kogumüügi järgi kahanevalt.

| Koht | Klient | Linn | Ostude arv | Kogumüük |
|---:|---|---|---:|---:|
| 1 | Tiina Pärn | Tartu | 73 | 27668.02 |
| 2 | Priit Rand | Pärnu | 76 | 26286.10 |
| 3 | Kevin Org | Tallinn | 78 | 23467.13 |
| 4 | Laura Tammik | Pärnu | 74 | 23385.82 |
| 5 | Erkki Ilves | Tartu | 72 | 22942.42 |
| 6 | Anu Kuusik | Tallinn | 77 | 21626.10 |
| 7 | Kersti Lill | Tallinn | 71 | 21137.47 |
| 8 | Riina Lill | Pärnu | 67 | 20972.33 |
| 9 | Annika Saar | Viljandi | 66 | 20726.79 |
| 10 | Ago Kull | Pärnu | 64 | 20124.61 |

**Järeldus:** suurima väärtusega kliendid ei paikne ainult Tallinnas. TOP 10 seas on mitu klienti Tartust ja Pärnust, mis näitab, et tugevaid kliendisuhteid on ka väljaspool peamist müügipiirkonda.

---

## 3. Müügianalüüs linnade kaupa

Kolmas päring näitas, kuidas müük ja kliendid jagunevad linnade lõikes.

| Linn | Kliente | Oste | Kogumüük |
|---|---:|---:|---:|
| Tallinn | 1007 | 3601 | 1006252.88 |
| Tartu | 525 | 1764 | 523286.64 |
| Pärnu | 276 | 1231 | 374005.86 |
| Narva | 145 | 438 | 122226.14 |
| Viljandi | 94 | 359 | 102314.94 |
| Rakvere | 90 | 338 | 93379.03 |
| Jõhvi | 71 | 290 | 77691.15 |
| Kuressaare | 80 | 256 | 76509.61 |
| Haapsalu | 73 | 252 | 73492.83 |
| Võru | 66 | 216 | 60983.07 |
| Valga | 69 | 216 | 59530.76 |
| Paide | 55 | 169 | 53148.87 |

**Järeldus:** Tallinn on selgelt suurim müügipiirkond nii klientide arvu, ostude arvu kui ka kogumüügi poolest. Samas on Tartu ja Pärnu samuti olulised müügiturud ning neid ei tohiks klienditurunduses käsitleda kõrvalisena.

---

## 4. Müük lojaalsustasemete kaupa

Neljas päring koondas müügi `loyalty_tier` väärtuse järgi.

| Lojaalsustase | Kliente | Kogumüük |
|---|---:|---:|
| NULL | 1024 | 1071805.32 |
| silver | 560 | 593470.07 |
| gold | 491 | 533601.64 |
| bronze | 476 | 423854.75 |

**Järeldus:** suurim kogumüük on klientidel, kelle `loyalty_tier` on puudu ehk `NULL`. See ei tähenda tingimata, et lojaalsusprogramm ei tööta. Pigem viitab see sellele, et lojaalsustaseme andmed vajavad kontrolli ja täiendamist.

---

## 5. Lisakontroll: INNER JOINist välja jäänud müügiread

Lisakontroll võrdles kõiki `sales` tabeli ridu nende ridadega, mis jõudsid `INNER JOIN` tulemusse.

| Näitaja | Väärtus |
|---|---:|
| Müügiridu kokku `sales` tabelis | 10118 |
| `INNER JOIN` tulemusse jõudnud ridu | 9130 |
| JOINist välja jäänud ridu | 988 |

**Järeldus:** 988 müügirida ei leidnud `customers` tabelist vastavat klienti. See on oluline andmekvaliteedi leid, sest kliendipõhises analüüsis jääb osa müügist kõrvale.

---

## 6. Üle keskmise kogumüügiga kliendid

Täiendav päring leidis kliendid, kelle kogumüük oli üle keskmise kliendimüügi. Tulemuses oli **900 klienti**.

**Äriline tähendus:** need kliendid võivad moodustada esmase sihtrühma lojaalsuskampaaniateks, personaalseteks pakkumisteks või edasiseks kliendisegmentide analüüsiks.

---

## Peamised leiud

1. `INNER JOIN` abil saab siduda müügiread kliendiandmetega ja luua kliendipõhise müügivaate.
2. Kõrgeima kogumüügiga klient oli **Tiina Pärn Tartust** kogumüügiga **27668.02**.
3. Suurim müügipiirkond oli **Tallinn**, kus oli **1007 klienti**, **3601 ostu** ja kogumüük **1006252.88**.
4. Suurim kogumüük lojaalsustasemete lõikes tuli klientidelt, kelle `loyalty_tier` oli **NULL**.
5. `INNER JOIN`ist jäi välja **988 müügirida**, mis tähendab, et kõiki müüke ei saa hetkel kliendianalüüsi kaasata.
6. Üle keskmise kogumüügiga kliente oli **900**, mis annab võimaliku sisendi lojaalsus- või VIP-segmendi määramiseks.

---

## Suurim üllatus

Suurim üllatus oli see, et lojaalsustaseme järgi oli suurim kogumüük `NULL` väärtusega klientide grupis. See viitab sellele, et osa väärtuslikust kliendibaasist ei ole lojaalsusprogrammi andmetes korrektselt liigitatud.

---

## Soovitus Annale

Enne kliendikampaaniate või lojaalsusprogrammi otsuste tegemist tuleks parandada kliendiandmete kvaliteeti: kontrollida `customer_id` vastavusi `sales` ja `customers` tabeli vahel ning täiendada puuduvaid `loyalty_tier` väärtusi. Alles seejärel saab lojaalsustasemete põhjal teha usaldusväärsemaid äriotsuseid.

---

## Soovitus Toomasele

Andmebaasi tasemel tuleks kontrollida, miks **988 müügirida** ei jõua `INNER JOIN` tulemusse. Võimalikud põhjused on puuduv `customer_id`, vigane `customer_id` või kliendikirje puudumine `customers` tabelis. See vajab eraldi andmekvaliteedi kontrolli enne juhtimisaruandlusse lisamist.

---

## Puuduvad andmed / piirangud

- 988 müügirida ei leidnud klienditabelist vastet.
- Lojaalsustase on `NULL` 1024 ostuga kliendi puhul.
- Analüüs ei näita veel, kas `NULL` lojaalsustase tähendab puuduvat andmesisestust, registreerimata klienti või tehnilist andmeülekande probleemi.
- `INNER JOIN` sobib kliendipõhiseks analüüsiks, kuid ei sobi kogu müügi täielikuks kontrolliks, sest see jätab vasteta müügiread välja.

---

## Kokkuvõte

Natalia analüüs näitab, et UrbanStyle'i müügi- ja kliendiandmete ühendamine annab väärtusliku vaate parimatele klientidele, linnade müügipanusele ja lojaalsustasemete mõjule. Samal ajal tõi analüüs välja olulise andmekvaliteedi probleemi: ligi tuhat müügirida ei ole hetkel klienditabeliga seostatav ning suur osa müügist on seotud puuduva lojaalsustasemega klientidega. Seetõttu tuleb kliendiandmeid enne kampaaniate ja juhtimisotsuste tegemist täpsustada.
