# Nädal 7: RFM-kliendisegmenteerimine Pythoniga

## Eesmärk

Arvutada UrbanStyle'i puhastatud müügiandmetest kliendipõhised Recency, Frequency ja Monetary näitajad, määrata RFM-skoorid ning jaotada kliendid äriliselt kasutatavatesse segmentidesse.

## Minu roll

**Roll C — RFM Analysis.**

Minu töö algas Roll B puhastatud pandas DataFrame'ist `df`. Arvutasin iga kliendi:

- viimase ostu värskuse ehk Recency;
- ostude sageduse ehk Frequency;
- kogukulutuse ehk Monetary;
- R-, F- ja M-skoorid skaalal 1–5;
- RFM-koondskoori ja baastaseme kliendisegmendi.

Lisaks tegin vabatahtliku edasijõudnute osa: kaalutud RFM-skoor, detailsem segmentatsioon ja tulemuste eksport CSV-faili.

## Peamised tulemused

RFM-tabelis on **2 540 klienti**.

- **VIP Champions:** 455 klienti ehk 17,91% klientidest ja 42,82% analüüsitud kogukulutusest.
- **Loyal:** 679 klienti ehk 26,73% klientidest ja 29,75% kogukulutusest.
- **Potential:** 759 klienti ehk suurim kliendirühm.
- **At Risk:** 529 klienti ehk 20,83% klientidest ja 7,18% kogukulutusest.
- **Lost:** 118 klienti ehk 4,65% klientidest ja 0,76% kogukulutusest.

VIP- ja Loyal-segmendid moodustavad kokku **44,65% klientidest**, kuid **72,57% analüüsitud kogukulutusest**.

## Järeldus

Kõige olulisem äriline prioriteet on hoida VIP-kliente ning kasvatada Loyal- ja Potential-segmentide lojaalsust. At Risk segment on arvukas, kuid madalama rahalise osakaaluga, mistõttu tasub tagasivõitmise tegevused suunata eelkõige kõrgema `monetary_value` väärtusega klientidele.

RFM-viitekuupäev `2025-02-28` on Week 7 juhendis ette antud ja seda kasutati juhendile vastavuse tagamiseks. Kuna andmestikus on ka sellest hilisemaid müügikuupäevi, tekib 25 kliendil negatiivne Recency. See ei ole Roll C koodiviga, vaid juhendis määratud viitekuupäeva ja andmestiku kuupäevavahemiku vastuolu, mis on dokumenteeritud analüüsi piiranguna.

## Kasutatud oskused ja tööriistad

Python, pandas, Jupyter Notebook, `groupby`, `merge`, `pd.qcut`, `apply`, `value_counts`, andmekvaliteedi kontroll, RFM-segmenteerimine ja CSV-eksport.

## AI kasutamine

Kasutasin AI-d RFM-loogika ja pandas-süntaksi kontrollimiseks, veateadete tõlgendamiseks ning dokumentatsiooni korrastamiseks. Kõik kasutatud koodiosad käivitati notebook'is ja tulemusi kontrolliti DataFrame'i väljundite ning CSV-faili põhjal.

## Artefaktid

- [Roll C individuaalne notebook](week7_role_c_rfm_analysis.ipynb)
- [Detailne analüüs](analysis.md)
- [Grupi koondnotebook](../../group/urbanstyle_operatsioonid_week7_(a_b_c_d).ipynb)
- [Grupi RFM-tulemused CSV-failina](../../group/rfm_segments.csv)

