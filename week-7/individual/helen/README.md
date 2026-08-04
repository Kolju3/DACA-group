# Nädal 7 — Roll C: RFM kliendisegmenteerimine

## Eesmärk

Roll C ülesanne on arvutada Roll B puhastatud tehinguandmete põhjal
Recency, Frequency ja Monetary mõõdikud ning jagada kliendid
RFM-segmentidesse.

## Minu vastutus

- Recency, Frequency ja Monetary arvutamine
- R-, F- ja M-skooride määramine
- RFM-koondskoori arvutamine
- viie baastaseme kliendisegmendi loomine
- segmentide klientide arvu ja osakaalu kontroll
- edasijõudnute kaalutud RFM-skoori loomine
- detailsemate kliendisegmentide määramine
- tulemuste CSV-faili eksportimise ettevalmistamine

## Failid

- `week7_role_c_rfm_analysis.ipynb` — Roll C Jupyter Notebook
- `analysis.md` — töö ulatuse, meetodite ja sõltuvuste kirjeldus

## Praegune seis

Notebook sisaldab juhendipärast Roll C baas- ja edasijõudnute
töövoogu.

Roll C sisendiks on Roll B ettevalmistatud pandas DataFrame `df`.
Seetõttu kinnitatakse lõplikud veerunimed, viitekuupäev ja tulemused
pärast Roll A ja Roll B töö valmimist ning grupi ühisesse notebook’i
lisamist.
