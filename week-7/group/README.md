# UrbanStyle RFM kliendisegmenteerimine Pythoniga

## Eesmärk

Koostada UrbanStyle'i müügi- ja kliendiandmetest RFM-segmendid, mille põhjal saab tootejuht Marko Saar kavandada erinevatele kliendirühmadele sobivaid tegevusi ja kampaaniaid.

RFM-meetodis mõõdab **Recency** viimase ostu värskust, **Frequency** ostude sagedust ja **Monetary** kliendi kogukulutust.

## Meeskonna rollid

- **Roll A — andmete laadimine:** Natalia
- **Roll B — andmete puhastamine:** Olga
- **Roll C — RFM-analüüs:** Helen
- **Roll D — visualiseerimine ja äritõlgendus:** Kalju

## Töö seis

Rollid A–C on koondnotebook'is rakendatud ning RFM-tulemused on eksporditud CSV-faili. Roll D visualiseeringud ja lõplik äritõlgendus on veel koostamisel.

Andmed laaditi Supabase'ist lehekülgede kaupa, et vältida ühe päringu 1000 rea piirangut:

- `sales`: 10 118 rida;
- `customers`: 3 150 rida;
- pärast ühendamist: 10 118 rida ja 20 veergu;
- pärast puhastamist: 8 950 rida ja 2 540 unikaalset klienti.

## Peamised esialgsed tulemused

Praeguse `rfm_segments.csv` põhjal:

- **VIP Champions:** 455 klienti ehk 17,91% klientidest; 42,82% analüüsitud kogukulutusest;
- **Loyal:** 679 klienti ehk 26,73%; 29,75% kogukulutusest;
- **Potential:** 759 klienti ehk 29,88%; suurim kliendirühm;
- **At Risk:** 529 klienti ehk 20,83%, kuid ainult 7,18% kogukulutusest;
- **Lost:** 118 klienti ehk 4,65% ja 0,76% kogukulutusest.

VIP- ja Loyal-segmendid moodustavad kokku 44,65% klientidest ning 72,57% analüüsitud kogukulutusest.

## Järeldus

Esimene tegevusprioriteet on hoida VIP-kliente ja kasvatada Loyal- ning Potential-segmentide lojaalsust. At Risk klientide puhul tasub üldise kampaania asemel eelistada kõrgema rahalise väärtusega kliente.

Tulemused on esialgsed, kuni meeskond kinnitab RFM-viitekuupäeva käsitluse. Andmestikus on oste pärast notebook'is kasutatud kuupäeva `2025-02-28`, mistõttu 25 kliendil on negatiivne Recency.

## Kasutatud oskused ja tööriistad

Python, pandas, Jupyter Notebook, Supabase, RFM-segmenteerimine, `groupby`, `merge`, `qcut`, andmekvaliteedi kontroll ja CSV-eksport.

## AI kasutamine

AI-d kasutati õppematerjalide tõlgendamisel, koodi ja kontrollide ülevaatamisel ning dokumentatsiooni koostamisel. Tulemused kontrolliti notebook'i väljundite ja CSV-faili põhjal.

## Artefaktid

- [Koondnotebook](urbanstyle_operatsioonid_week7_(a_b_c_d).ipynb)
- [RFM-segmendid CSV-failina](rfm_segments.csv)

