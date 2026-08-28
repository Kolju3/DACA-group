# Week 10: Portfolio Defense — Operations Intelligence

## Eesmärk

Week 10 koondas 10 nädala töö üheks tõendatavaks portfoolio- ja esitluslooks. Meeskonna lõppesitluse eesmärk oli näidata mitte ainult tehtud SQL-, Python- ja Power BI töid, vaid seda, **mida UrbanStyle andmetest õppis ja milliseid otsuseid tulemused toetavad**.

Lõppesitlus järgis ametlikku 7-minutilist struktuuri:

1. sissejuhatus — 1 min;
2. andmete ülevaade — 2 min;
3. visualiseeringud — 2 min;
4. kolm juhtimissoovitust — 1 min;
5. AI kasutamine — 1 min.

## Meeskond

**Operations Intelligence**

Lõppesitluses osalesid:
- Kalju Tamme
- Helen Tanner
- Natalia Krassilnikova

## Esitluse põhisõnum

**Andmed → kontroll → analüüs → visuaalne tõend → äriline järeldus → tegevus**

Läbiv kontrollküsimus oli: **„Ja mis siis?“**  
Iga põhitulemus pidi näitama mitte ainult numbrit, vaid ka selle tähendust otsustaja jaoks.

## Peamised leiud

### 1. Andmekvaliteet — Natalia

Puhastamisel eemaldati **5 116 duplikaatrida**.

- algne müügitulu: ~**4,37 mln €**
- kontrollitud müügitulu: ~**2,91 mln €**
- erinevus: ~**1,46 mln €**

**Tähendus:** juhtimisotsus ei saa olla usaldusväärsem kui selle aluseks olevad andmed.

[CASE ↗ Natalia — Week 2](https://github.com/Nata376/daca-portfolio/tree/main/week-2)

### 2. Müügi koondumine — Natalia

Analüüs näitas, et müük ei jaotu müügikohtade ja kanalite vahel ühtlaselt. Tulemust kasutati selleks, et tõsta esile vajadus juhtida tähelepanu kohtadele ja kanalitele, kus äriline mõju on suurim.

[CASE ↗ Natalia — Week 4](https://github.com/Nata376/daca-portfolio/tree/main/week-4)

### 3. Varude tasakaal — Helen

Inventuurianalüüs tõi välja:

- **221** reorder-risk / juurdetellimise kontrollpositsiooni;
- **730** ebatavaliselt kõrge laoseisu kontrollpositsiooni.

**Oluline piirang:** 730 ei tähenda tõestatud ülevaru. `reorder_point` on juurdetellimise käivituspunkt, mitte optimaalne maksimaalne laotase.

**Tähendus:** ühes kohas võib tekkida saadavusrisk ajal, mil mujal on varu ebaproportsionaalselt palju.

[CASE ↗ Helen — Week 3](https://github.com/HelenTanner3/daca-portfolio/tree/main/01-sql/week-3)

### 4. Kõrge väärtusega kliendid — Kalju

RFM-põhise visualiseeringu üks tugevamaid tulemusi:

**TOP 10 VIP Champions = 8,64% RFM-analüüsis arvestatud käibest.**

**Tähendus:** väga väike kõrge väärtusega kliendigrupp võib anda ebaproportsionaalselt suure osa kliendiväärtusest.

[CASE ↗ Kalju — Week 7](https://github.com/Kolju3/DACA-portfolio/tree/main/Week%207)

## Visualiseeringud

### Helen — Tartu Power BI

Tartu kaupluse 2024 tulemused:

- müügitulu ~**260 044 €**
- müügitulu **+13,4%**
- tellimuste arv **+16,5%**
- keskmine tellimuse väärtus (AOV) **−2,6%**

**Järeldus:** kasv tuli suuremast tellimuste arvust, mitte suuremast keskmisest ostukorvist.

[CASE ↗ Helen — Week 6 Power BI](https://github.com/HelenTanner3/daca-portfolio/tree/main/02-power-bi/week-6)

### Kalju — Python / Streamlit dashboard

Kalju kasutas enda Python/Streamlit dashboard'i, et näidata müügi ajajoont ja andmete täielikkuse küsimust.

Pärast 2024. aastat langeb olemasolevate müügiandmete maht järsult. Kuna hilisemates perioodides leidub siiski üksikuid tehinguid, käsitleti seda esmalt **andmete täielikkuse kontrollküsimusena**, mitte automaatselt müügi kokkuvarisemisena.

## Kolm juhtimissoovitust

1. **Kontrolli andmekvaliteeti enne juhtimisotsust.**  
   5 116 duplikaatrida muutsid müüginumbrit ligikaudu 1,46 mln € võrra ning hilisemate perioodide andmete täielikkus vajab kontrolli.

2. **Juhi väärtust, mitte ainult mahtu.**  
   Käivet, tellimuste/müügi mahtu ja keskmist väärtust tuleb vaadata koos.

3. **Kaitse kõrge väärtusega kliendibaasi.**  
   RFM-analüüs näitas kliendiväärtuse tugevat kontsentratsiooni; VIP/Loyal klientide hoidmist tasub juhtida sihitult ja mõõdetavalt.

## AI kasutamine

AI-d kasutati 10 nädala jooksul eelkõige:
- SQL-, Python- ja DAX-loogika mõtestamiseks ja veaotsinguks;
- lahendusvariantide võrdlemiseks;
- dokumentatsiooni ja README-de struktureerimiseks;
- esitlusloo, ajastuse ja sõnastuse viimistlemiseks.

**Analüütiline vastutus jäi inimesele:** kontrolliti ridade arvu, duplikaate, kuupäevi, kontrollsummasid, KPI-sid, allikaid ning seda, mida tulemus tegelikult tõendab.

> Töötav kood ei tähenda automaatselt õiget tulemust.

## Tõendid ja portfooliod

- [Helen Tanner — DACA portfolio](https://github.com/HelenTanner3/daca-portfolio)
- [Kalju Tamme — DACA portfolio](https://github.com/Kolju3/DACA-portfolio)
- [Natalia Krassilnikova — DACA portfolio](https://github.com/Nata376/daca-portfolio)

## Artefaktid

Week 10 ühine põhiartefakt on **7-minutiline lõppesitlus koos Q&A tõendusslaididega**.

Lõplik `.pptx` / `.pdf` fail lisatakse Week 10 kausta pärast viimast eksporti.

