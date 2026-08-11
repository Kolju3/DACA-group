# Nädal 6 — Power BI ja Streamlit dashboard'id ning andmelugu

## Eesmärk

Koostada UrbanStyle'i kaupluste ja e-poe kohta interaktiivsed juhtimisvaated, mis ühendavad KPI-d, müügitrendid, filtreerimise ja selge andmeloo.

## Meeskonna rollid

- **Roll A — Tallinna kauplus:** Olga
- **Roll B — Tartu kauplus:** Helen
- **Roll C — Pärnu kauplus:** Kalju
- **Roll D — e-pood:** Natalia

## Grupi väljundid

| Kanal | Lahendus | Peamine tulemus |
|---|---|---|
| Tallinn | Power BI dashboard | kuutrend, TOP 5 tooted ja makseviiside jaotus; KPI-de filtrikontekst vajab kontrolli |
| Tartu | Power BI dashboard | 2024. aasta müügitulu kasvas 13,4%; kasv tuli suuremast tellimuste arvust |
| Pärnu | Streamlit ja Plotly dashboard | müügitulu kasvas 3,5%; tugev hooajalisus ja väiksem keskmine tellimus |
| E-pood | Power BI dashboard | käive 1,01 mln €, kasv 20,46%; tugevad tipud suvel ja detsembris |

## Peamised ühised leiud

- **E-pood** oli dokumenteeritud tulemuste põhjal kiireima kasvuga kanal.
- **Tartu** kasv tuli suuremast tellimuste arvust, samal ajal kui keskmine tellimus vähenes.
- **Pärnu** müük oli tugevalt hooajaline ning suur osa müügitulust pärines väljastpoolt Pärnut elavatelt klientidelt.
- **Tallinna** dashboard'i KPI-d näivad olevat arvutatud kogu ettevõtte, mitte ainult Tallinna andmetest. Enne tulemuste kasutamist tuleb kontrollida slicer'i mõju ja DAX-mõõdikute filtrikonteksti.

## Kasutatud lahendused ja oskused

Meeskonna töödes kasutati:

- Power BI-d;
- Pythonit, Streamliti ja Plotlyt;
- Supabase'i andmeühendust;
- DAX-mõõdikuid ja KPI-kaarte;
- kuiseid trendivaateid ning TOP-toodete analüüsi;
- slicer'eid, ristfiltreerimist ja drill-hierarhiaid;
- tingimuslikku vormindamist;
- annotatsioone, viitejooni ja tegevussoovitusi.

## Piirangud

- Müügitulemuste põhjal ei saa ilma täiendavate andmeteta kinnitada kampaaniate, hinnastamise või marginaali mõju.
- Pärnu puhul ei saa kõiki väljaspool Pärnut elavaid kliente automaatselt turistideks nimetada.
- Staatilised narratiivid ei pruugi filtrite muutmisel koos visuaalidega uueneda.
- Tallinna tulemused vajavad enne kanalitevahelist võrdlust valideerimist.

## Individuaalsed tööd

- [Olga — Roll A, Tallinn](individual/olga/)
- [Helen — Roll B, Tartu](individual/helen/)
- [Kalju — Roll C, Pärnu](individual/kalju/)
- [Natalia — Roll D, e-pood](individual/natalia/)

Täpsemad KPI-d, dashboard'ide kuvatõmmised, tehnilised lahendused ja individuaalsed järeldused on kirjeldatud liikmete kaustades.

