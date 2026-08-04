# Nädal 7 — Roll C RFM-analüüs

## 1. Ülesanne

Minu ametlik vastutus grupitöös on Roll C — RFM Analysis.

Roll C kasutab Roll B puhastatud tehinguandmeid ning arvutab iga
kliendi kohta:

- Recency — päevade arv viimasest ostust;
- Frequency — ostude arv;
- Monetary — ostude kogusumma.

Nende põhjal määratakse R-, F- ja M-skoorid ning kliendisegmendid.

## 2. Rollidevaheline sõltuvus

Roll C ei laadi ega puhasta lähteandmeid.

Töövoog on:

1. Roll A laadib ja ühendab müügi- ning kliendiandmed.
2. Roll B puhastab ühendatud andmestiku.
3. Roll C kasutab puhastatud DataFrame’i `df`.
4. Roll D kasutab Roll C loodud RFM-tabelit visualiseerimiseks.

Roll C eeldab, et sisendtabel sisaldab vähemalt järgmisi veerge:

- `customer_id`
- `sale_date`
- `sale_id`
- `total_price`

Lõplik sisendi struktuur kontrollitakse pärast Roll A ja Roll B töö
valmimist.

## 3. Baastaseme meetodid

Notebook sisaldab juhendipärast baastaseme töövoogu:

1. analüüsi viitekuupäeva määramine;
2. kliendi viimase ostukuupäeva leidmine;
3. Recency arvutamine päevades;
4. Frequency arvutamine ostude arvu järgi;
5. Monetary arvutamine ostusummade liitmisega;
6. kolme RFM-tabeli ühendamine;
7. kvintiilipõhiste R-, F- ja M-skooride määramine;
8. RFM-koondskoori arvutamine;
9. viie kliendisegmendi määramine;
10. segmentide klientide arvu ja osakaalu kontroll.

Baastaseme segmendid on:

| RFM-skoor | Segment |
|---:|---|
| 13–15 | VIP Champions |
| 10–12 | Loyal |
| 7–9 | Potential |
| 4–6 | At Risk |
| 3 | Lost |

## 4. Edasijõudnute osa

Notebook sisaldab ka juhendi edasijõudnute ülesandeid:

- Monetary kahekordse kaaluga RFM-skoor;
- kuus detailsemat kliendisegmenti;
- tulemuste eksport faili `rfm_segments.csv`.

Kaalutud skoor arvutatakse kujul:

`R_score + F_score + 2 × M_score`

Detailsemad segmendid on:

- VIP Champions
- Loyal Customers
- Regular Customers
- New Customers
- At Risk
- Lost

## 5. Viitekuupäev

Notebook’is on praegu kasutatud juhendis toodud näidiskuupäeva
`2025-02-28`.

See kuupäev tuleb enne lõpliku grupitöö kinnitamist üle kontrollida.
Kui Roll B puhastatud andmestik sisaldab sellest hilisemaid tehinguid,
tuleb valida andmestiku tegeliku ajavahemikuga sobiv viitekuupäev.

## 6. Praegune seis

Roll C notebook on koostatud juhendi meetodite järgi, kuid ei ole veel
Roll A ja Roll B lõpliku väljundiga tervikuna käivitatud.

Pärast eelnevate rollide töö valmimist tuleb:

1. kontrollida Roll B DataFrame’i nime ja veerge;
2. ühendada Roll C sektsioon grupi ühisesse notebook’i;
3. kontrollida viitekuupäeva;
4. käivitada RFM-arvutused;
5. kontrollida skooride ja segmentide tulemusi;
6. edastada valmis RFM-tabel Roll D-le;
7. täiendada dokumentatsiooni tegelike tulemustega.

## 7. Roll C väljund

Roll C annab Roll D-le kliendipõhise RFM-tabeli, mis sisaldab vähemalt:

- `customer_id`
- Recency
- Frequency
- Monetary
- R-, F- ja M-skoorid
- RFM-koondskoor
- kliendisegment

Edasijõudnute osas sisaldab tabel lisaks kaalutud RFM-skoori ja
detailsemat segmenti.