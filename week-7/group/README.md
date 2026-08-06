# Nädal 7 — UrbanStyle RFM-kliendisegmenteerimine Pythoniga

## Eesmärk

Koostada UrbanStyle'i müügi- ja kliendiandmetest kliendipõhine RFM-analüüs, mis aitab eristada väärtuslikke, lojaalseid, kasvupotentsiaaliga ja lahkumisriskiga kliente ning toetab tootejuht Marko Saare kampaaniaotsuseid.

RFM-meetodis mõõdab:

- **Recency** viimase ostu värskust;
- **Frequency** ostude sagedust;
- **Monetary** kliendi kogukulutust.

## Meeskonna rollid

- **Roll A — andmete laadimine:** Natalia
- **Roll B — andmete puhastamine:** Olga
- **Roll C — RFM-analüüs:** Helen
- **Roll D — visualiseerimine ja äritõlgendus:** Kalju

## Töövoog

1. Supabase'ist laaditi `sales` ja `customers` tabelite kõik read 1000 rea kaupa.
2. Tabelid ühendati `customer_id` alusel.
3. Andmed puhastati RFM-arvutuseks sobivaks.
4. Iga kliendi kohta arvutati Recency, Frequency ja Monetary väärtused.
5. Kliendid jaotati RFM-skoori põhjal viide põhisegmenti.
6. RFM-tulemused eksporditi CSV-faili Roll D visualiseerimise sisendiks.

## Andmemahud

- `sales`: **10 118 rida**
- `customers`: **3 150 rida**
- ühendatud andmestik: **10 118 rida ja 20 veergu**
- pärast puhastamist: **8 950 rida**
- RFM-tabel: **2 540 klienti**

## Peamised tulemused

| Segment | Kliente | Klientide osakaal | Kogukulutuse osakaal |
|---|---:|---:|---:|
| VIP Champions | 455 | 17,91% | 42,82% |
| Loyal | 679 | 26,73% | 29,75% |
| Potential | 759 | 29,88% | 19,49% |
| At Risk | 529 | 20,83% | 7,18% |
| Lost | 118 | 4,65% | 0,76% |

VIP- ja Loyal-segmendid moodustavad kokku **44,65% klientidest**, kuid **72,57% analüüsitud kogukulutusest**.

## Järeldus

Kõige olulisem tegevusprioriteet on hoida VIP-kliente ning kasvatada Loyal- ja Potential-segmentide lojaalsust. At Risk segment on arvukas, kuid väiksema rahalise osakaaluga, mistõttu tasub tagasivõitmise tegevused suunata eelkõige kõrgema `monetary_value` väärtusega klientidele.

## Piirang

RFM-viitekuupäev `2025-02-28` on Week 7 juhendis ette antud ja seda kasutati juhendile vastavuse tagamiseks. Kuna andmestik sisaldab ka sellest hilisemaid müügikuupäevi, on 25 kliendil negatiivne Recency.

See ei ole Roll C koodiviga, vaid juhendis määratud viitekuupäeva ja andmestiku kuupäevavahemiku vastuolu. Piirang tuleb lõppvisualiseeringus selgelt välja tuua; viitekuupäeva muutmine oleks eraldi alternatiivne analüüs.

## Töö seis

Rollid A–C on koondnotebook'is rakendatud ja RFM-tulemused on CSV-failina olemas. Roll D visualiseeringud ja lõplik äritõlgendus on veel koostamisel.

## Kasutatud oskused ja tööriistad

- Python ja pandas
- Jupyter Notebook
- Supabase
- `.env` ja `python-dotenv`
- `groupby`, `merge`, `pd.qcut`, `apply` ja `value_counts`
- andmete puhastamine ja valideerimine
- RFM-kliendisegmenteerimine
- CSV-eksport
- Git ja GitHub

## AI kasutamine

AI-d kasutati õppematerjalide tõlgendamisel, pandas- ja Supabase'i koodi kontrollimisel, vigade analüüsimisel ning dokumentatsiooni vormistamisel. Lõplikud arvud kontrolliti notebook'i väljundite ja `rfm_segments.csv` faili põhjal.

## Grupi artefaktid

- [Koondnotebook](urbanstyle_operatsioonid_week7_(a_b_c_d).ipynb)
- [RFM-segmendid CSV-failina](rfm_segments.csv)

## Individuaalsed väljundid

- [Natalia — Roll A](../individual/natalia/)
- [Olga — Roll B](../individual/olga/)
- [Helen — Roll C](../individual/helen/)
- [Kalju — Roll D](../individual/helen/)


