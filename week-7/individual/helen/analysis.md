# Nädal 7 — Roll C RFM-analüüsi detailne ülevaade

## 1. Roll ja töö ulatus

Minu põhiroll oli **Roll C — RFM Analysis**.

Roll C ei laadinud ega puhastanud lähteandmeid. Sisendiks oli Roll B puhastatud pandas DataFrame `df`, milles olid RFM-arvutuseks vajalikud väljad:

- `customer_id`;
- `sale_date`;
- `sale_id`;
- `total_price`.

Minu väljundiks oli kliendipõhine DataFrame `rfm`, mille Roll D saab kasutada visualiseerimiseks ja äritõlgenduseks.

## 2. Sisendandmete seis

Grupi koondnotebook'i järgi oli Roll C sisendiks:

| Näitaja | Tulemus |
|---|---:|
| puhastatud müügiridu | 8 950 |
| unikaalseid kliente | 2 540 |
| puhastatud andmete kuupäevavahemik | 2023-01-01 kuni 2026-06-28 |

Need arvud pärinevad Roll B väljundist. Roll C ei muutnud enam müügiridade sisu, vaid koondas need kliendipõhiseks RFM-tabeliks.

## 3. RFM-metoodika

### 3.1. Recency

Recency arvutati iga kliendi viimase ostukuupäeva põhjal:

```python
recency = (
    df.groupby("customer_id")["sale_date"]
    .max()
    .reset_index()
)
```

Viitekuupäevaks kasutati juhendis ette antud kuupäeva:

```python
today = pd.to_datetime("2025-02-28")
```

Recency väärtus näitab päevade arvu viitekuupäeva ja kliendi viimase ostu vahel. Väiksem väärtus tähendab hiljutisemat ostu.

### 3.2. Frequency

Frequency arvutati kliendi `sale_id` väärtuste arvuna:

```python
frequency = (
    df.groupby("customer_id")["sale_id"]
    .count()
    .reset_index()
)
```

Suurem Frequency tähendab suuremat ostuaktiivsust.

### 3.3. Monetary

Monetary arvutati kliendi `total_price` väärtuste summana:

```python
monetary = (
    df.groupby("customer_id")["total_price"]
    .sum()
    .reset_index()
)
```

Suurem Monetary tähendab suuremat ajaloolist kogukulutust.

### 3.4. RFM-tabeli loomine

Recency, Frequency ja Monetary tabelid ühendati `customer_id` alusel üheks kliendipõhiseks tabeliks.

Tulemuseks oli **2 540 reaga RFM-tabel**, kus iga klient esines ühe korra.

## 4. Skooride määramine

Iga RFM-mõõdik jaotati `pd.qcut()` abil viide ligikaudu võrdsesse rühma.

- Recency puhul sai väiksem väärtus kõrgema skoori.
- Frequency puhul sai suurem väärtus kõrgema skoori.
- Monetary puhul sai suurem väärtus kõrgema skoori.

Skooride vahemik oli 1–5 ning koondskoor arvutati:

```python
RFM_Score = R_score + F_score + M_score
```

Baastaseme segmendid määrati koondskoori järgi:

| RFM-skoor | Segment |
|---:|---|
| 13–15 | VIP Champions |
| 10–12 | Loyal |
| 7–9 | Potential |
| 4–6 | At Risk |
| 3 | Lost |

## 5. Kvaliteedikontroll

Roll C kvaliteedikontroll kinnitas:

| Kontroll | Tulemus |
|---|---:|
| kliente RFM-tabelis | 2 540 |
| segmendita kliente | 0 |
| R-skoori vahemik | 1–5 |
| F-skoori vahemik | 1–5 |
| M-skoori vahemik | 1–5 |
| klientide osakaalude summa | 100,00% |

## 6. Baastaseme tulemused

Analüüsitud kogukulutus oli **2 676 850,54 eurot**.

| Segment | Kliente | Klientide osakaal | Kogukulutus, € | Kogukulutuse osakaal |
|---|---:|---:|---:|---:|
| VIP Champions | 455 | 17,91% | 1 146 295,15 | 42,82% |
| Loyal | 679 | 26,73% | 796 357,18 | 29,75% |
| Potential | 759 | 29,88% | 521 792,88 | 19,49% |
| At Risk | 529 | 20,83% | 192 170,22 | 7,18% |
| Lost | 118 | 4,65% | 20 235,11 | 0,76% |

## 7. Segmentide profiil

| Segment | Keskmine kogukulutus, € | Keskmine Frequency | Keskmine Recency |
|---|---:|---:|---:|
| VIP Champions | 2 519,33 | 7,68 | 48,66 |
| Loyal | 1 172,84 | 3,84 | 145,29 |
| Potential | 687,47 | 2,49 | 207,49 |
| At Risk | 363,27 | 1,59 | 309,57 |
| Lost | 171,48 | 1,01 | 516,88 |

Recency keskmist tuleb tõlgendada ettevaatlikult, sest 25 kliendil on praeguse viitekuupäeva tõttu negatiivne Recency.

## 8. Analüütilised leiud

### 8.1. VIP-klientide osakaal väärtusest on ebaproportsionaalselt suur

VIP Champions moodustab 17,91% klientidest, kuid 42,82% analüüsitud kogukulutusest. VIP-kliendi keskmine kogukulutus on ligikaudu 2 519 eurot.

**Tõlgendus:** VIP-klientide hoidmine on suurema ärilise mõjuga kui kõigile klientidele ühetaolise kampaania pakkumine.

### 8.2. VIP ja Loyal koondavad suurema osa väärtusest

VIP ja Loyal moodustavad kokku:

- 1 134 klienti ehk 44,65% kliendibaasist;
- 1 942 652,33 eurot ehk 72,57% analüüsitud kogukulutusest.

**Tõlgendus:** lojaalsusprogrammi põhifookus võiks olla VIP-klientide hoidmisel ja Loyal-klientide VIP-tasemele kasvatamisel.

### 8.3. Potential on suurim kasvurühm

Potential-segment on 759 kliendiga suurim rühm ning moodustab 29,88% klientidest.

**Tõlgendus:** Potential-klientidele sobivad järgmise ostu stiimulid, ristmüük ja lojaalsusprogrammi aktiveerimine.

### 8.4. At Risk on arvukas, kuid madalama rahalise osakaaluga

At Risk segment moodustab 20,83% klientidest, kuid ainult 7,18% analüüsitud kogukulutusest.

**Tõlgendus:** kõigile At Risk klientidele sama kuluka kampaania tegemine ei pruugi olla efektiivne. Esmalt võiks valida kõrgema `monetary_value` väärtusega kliendid.

### 8.5. Lost-segmendi rahaline osakaal on väike

Lost-kliente on 118 ning nende kogukulutuse osakaal on 0,76%.

**Tõlgendus:** see segment on madalama prioriteediga ning sobib pigem piiratud testkampaaniale kui suure eelarvega tegevusele.

## 9. Edasijõudnute osa

Lisaks baastasemele arvutasin:

```python
Weighted_RFM_Score = R_score + F_score + 2 * M_score
```

Monetary sai kahekordse kaalu, et rõhutada kliendi rahalist väärtust.

Lisasin ka detailsema kuue segmendi jaotuse ning eksportisin RFM-tulemused CSV-faili.

Oluline piirang: praeguses koodis määratakse `Advanced_Segment` endiselt tavalise `RFM_Score`, mitte `Weighted_RFM_Score` järgi. Kaalutud skoor on seega abimõõdik, kuid ei muuda praegu segmendi nime.

## 10. Piirangud ja kontrollimist vajavad küsimused

### 10.1. Juhendis ette antud RFM-viitekuupäev

Week 7 juhend määrab Roll C viitekuupäevaks:

```python
today = pd.to_datetime("2025-02-28")
```

Kasutasin sama kuupäeva juhendile vastavuse tagamiseks. Puhastatud andmed ulatuvad samal ajal `2026-06-28`-ni.

Praeguses CSV-failis on:

- 25 negatiivse `recency_days` väärtusega klienti;
- minimaalne Recency `-485`;
- neist 18 on VIP Champions ja 7 Loyal.

See ei ole Roll C koodiviga ega minu vabalt valitud kuupäev, vaid juhendis fikseeritud viitekuupäeva ja andmestiku tegeliku kuupäevavahemiku vastuolu.

Põhitulemuses säilitan juhendi kuupäeva. Piirang tuleb dokumenteerida ning vajaduse korral mentoriga üle kontrollida. Viitekuupäeva muutmine või hilisemate müükide eemaldamine oleks eraldi alternatiivne analüüs, mitte juhendi põhivoo vaikne parandamine.

### 10.2. Frequency definitsioon

Frequency arvutatakse praegu `sale_id` väärtuste loendusega. Kui üks tellimus võib sisaldada mitut müügirida, tuleks kaaluda unikaalsete tellimuste loendamist.

Praeguse grupikontrolli järgi ei leitud korduvaid `invoice_id` väärtusi, kuid Frequency äriline definitsioon tuleb siiski dokumenteerida.

### 10.3. CSV-väljundi vorming

Praeguses `rfm_segments.csv` failis:

- on 11 analüütilist veergu;
- puuduvad kliendi nimi ja e-post;
- `customer_id` on salvestatud ujukomaarvuna, näiteks `2001.0`.

Visualiseerimiseks on fail piisav. Turunduskampaania sihtnimekirjaks vajaks tulemus kliendiandmetega ühendamist ja `customer_id` vormingu korrastamist.

## 11. Soovitused Markole

- **VIP Champions:** hoidmisprogramm, varajane ligipääs ja personaalsed eelised.
- **Loyal:** lojaalsuse premeerimine ning VIP-tasemele kasvatamine.
- **Potential:** järgmise ostu stiimul, ristmüük ja lojaalsusprogrammi aktiveerimine.
- **At Risk:** sihitud win-back eelkõige kõrgema rahalise väärtusega klientidele.
- **Lost:** madalama kuluga testkampaania ja tasuvuse kontroll.

## 12. Roll D-le üle antud väljund

Roll D saab kasutada grupi faili:

```text
week-7/group/rfm_segments.csv
```

Põhiveerud visualiseerimiseks:

- `customer_id`;
- `recency_days`;
- `frequency`;
- `monetary_value`;
- `RFM_Score`;
- `Segment`;
- `Advanced_Segment`.

Soovitatav on kasutada põhiloos baastaseme `Segment` veergu ning käsitleda detailsemat segmentatsiooni eraldi vabatahtliku lisavaatena.

## 13. Õppetunnid

Selle rolli kaudu kinnistus:

- kliendipõhine koondamine `groupby()` abil;
- mitme arvutustabeli ühendamine `merge()` abil;
- kvintiilide kasutamine `pd.qcut()` abil;
- funktsiooni rakendamine DataFrame'i ridadele;
- tehnilise skoori tõlkimine äriliseks segmendiks;
- kontrollväärtuste ja metoodiliste piirangute dokumenteerimine;
- arusaam, et töötav kood ei taga automaatselt korrektset analüütilist tulemust.

