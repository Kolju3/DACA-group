# Nädal 6 detailanalüüs — Roll B: Tartu kaupluse dashboard

## 1. Töö kontekst ja roll

Minu ametlik roll grupitöös oli **Roll B — Tartu kaupluse dashboard ja narratiiv**. Koostasin Power BI-s Tartu kaupluse juhtimisvaate, mis oli sisendiks meeskonna W6 koondtööle.

Käesolev dokument kirjeldab minu individuaalse väljundi tulemusi, interaktiivsust, arendusotsuseid ja piiranguid. Grupi koondlahendus valmib liikmete asukohapõhiste vaadete põhjal eraldi.

## 2. Äriküsimus

Dashboard vastab kolmele põhiküsimusele:

1. Kuidas muutus Tartu kaupluse 2024. aasta müügitulu võrreldes 2023. aastaga?
2. Kas muutus tulenes eelkõige tellimuste arvust või keskmise tellimuse väärtusest?
3. Millised kuud, tooted ja segmendid vajavad juhtimisotsuse seisukohalt tähelepanu?

Juhendi näitlik langustrend ei vastanud tegelikele andmetele. Tegelik andmestik näitas 2024. aastal kasvu, mistõttu narratiiv põhineb kontrollitud tulemustel.

## 3. Kasutatud andmed

Dashboard kasutab järgmisi Power BI mudeli osi:

- `public sales` — müügitulu, tellimused, kuupäev, kauplus ja toode;
- `Calendar` — aasta, kuu ja kuude järjestus;
- `public products` — tootenimi, kategooria ja alamkategooria;
- `public customers` — kliendigrupp (`loyalty_tier`).

Võrdlusperiood on **2023 vs 2024**.

## 4. Dashboard'i struktuur

Dashboard sisaldab:

- 2024 ja 2023 müügitulu KPI-sid ning aastast muutust;
- tellimuste arvu ja keskmise tellimuse võrdlust;
- kuist müügitulu ja kuist aastakasvu;
- TOP 5 toodete tulpdiagrammi;
- toote–alamkategooria–kategooria hierarhiat TOP 5 diagrammil;
- kaupluse valiku slicer'it;
- kategooria, alamkategooria ja kliendigrupi detailfiltreid;
- kahte annotatsiooni, viitejooni ja juhtimisnarratiivi.

TOP 5 diagrammi hierarhia näitab, millistesse alamkategooriatesse ja kategooriatesse valitud TOP 5 tooted kuuluvad. See ei ole eraldi kategooriate TOP 5 järjestus.

## 5. Kontrollväärtused

| Näitaja | 2023 | 2024 | Muutus |
|---|---:|---:|---:|
| Müügitulu | 229 316,99 € | 260 044,23 € | +13,4% |
| Tellimuste arv | 777 | 905 | +16,5% |
| Keskmine tellimus | 295,13 € | 287,34 € | −2,6% |

Müügitulu suurenes 30 727,24 euro võrra. Kasv tuli eelkõige suuremast tellimuste arvust, mitte keskmise ostukorvi suurenemisest.

Kuine võrdlus näitas:

- suurim langus aprillis: **−30,9%**;
- tugevaim kasv mais: **+96,9%**;
- positiivne muutus üheksal kuul kaheteistkümnest.

## 6. Tulemuste tõlgendus

Tartu müügitulu kasvas 13,4%, samal ajal kui keskmine tellimus vähenes 2,6%. See tähendab, et kasv saavutati suurema tehingumahu kaudu.

Aprilli langus ja mai väga tugev kasv vajavad täiendavat analüüsi. Dashboard ei sisalda kampaania-, konkurendi-, külastus- ega tööjõuandmeid, mistõttu ei saa kõikumise põhjust nimetada kinnitatud faktina.

TOP 5 toodete müügitulud on omavahel suhteliselt lähedased. Täpsemaks sortimendiotsuseks tuleks lisada müüdud kogused, marginaal ja laoseis.

## 7. Andmelugu ja soovitus

> **Tulemus:** Tartu müügitulu kasvas 2024. aastal 13,4%.  
> **Kõikumine:** suurim langus oli aprillis −30,9% ja tugevaim kasv mais +96,9%.  
> **Tegevus:** analüüsida aprilli ja mai toote-, kategooria- ning kliendisegmendi struktuuri, et tuvastada korratavad kasvutegurid.

## 8. Interaktiivsus ja kujundusotsused

Kaupluse valik on paigutatud dashboard'i ülaossa kui peamine juhtimisfilter. Kategooria, alamkategooria ja kliendigrupi filtrid on paigutatud lehe alaossa, et esimene vaade jääks rahulikuks ning detailfiltrid oleksid kättesaadavad sügavamat analüüsi vajavale kasutajale.

TOP 5 toodete diagrammil saab drillimise abil liikuda toote, alamkategooria ja kategooria tasemete vahel.

Narratiiv ja aprilli/mai annotatsioonid on staatilised ning kirjeldavad Tartut. Filtrite muutmisel tuleb tõlgendada dünaamilisi visuaale eraldi staatilisest tekstist.

## 9. Juhendaja tagasiside ja refleksioon

Juhendaja soovitas kaaluda:

- detailfiltrite paigutamist dashboard'i ülaossa kokkupandava ehk akordioni-tüüpi filtriplokina;
- uuema aasta kuvamist heledama põhiseeriaks ning võrdlusaasta muutmist hallikamaks ja vähem domineerivaks.

Neid muudatusi lõppversiooni ei viidud. Praegune filtripaigutus säilitati teadliku informatsioonihierarhiana ning värvilahendus jäeti varasema dashboard'iga järjepidevaks. Tagasiside jääb järgmiste Power BI lahenduste arenduspunktiks.

## 10. Valideerimine

Kontrollitud on:

- aastasummade ja kuusummade kooskõla;
- aastase muutuse arvutus;
- tellimuste arvu ja keskmise tellimuse loogika;
- narratiivi vastavus kuistele tulemustele;
- TOP 5 toodete hierarhia olemasolu;
- kategooria, alamkategooria ja kliendigrupi slicer'ite olemasolu.

Enne avalikku jagamist tuleb `Edit interactions` vaates üle kontrollida kõigi slicer'ite mõju KPI-dele ja diagrammidele.

## 11. Piirangud ja edasised arendused

- Staatiline narratiiv ei muutu filtritega kaasa.
- TOP 5 hierarhia kirjeldab toodete kuuluvust, mitte kategooriate eraldi edetabelit.
- Dashboard ei sisalda marginaali, kampaaniate, konkurentide, külastuste ega tööjõuandmeid.
- TOP 5 võrdlus põhineb müügitulul, mitte kasumlikkusel või laoseisul.
- Analüüs ei sisalda prognoosi.

Edasised arendused:

- kokkupandav filtriplokk;
- võrdlusaasta visuaalne taandamine;
- dünaamiline narratiiv;
- kategooriate eraldi müügiedetabel;
- müügitulemuse sidumine varu- ja marginaaliandmetega.

## 12. Individuaalse ja grupitöö eristus

### Individuaalne väljund

- Tartu kaupluse Power BI dashboard;
- Tartu KPI-d, trendid, TOP 5 tooted ja narratiiv;
- toodete drill-hierarhia;
- kategooria, alamkategooria ja kliendigrupi detailfiltrid;
- PBIX, kuvatõmmis, README ja detailanalüüs.

### Grupitöö

Minu väljund on üks sisend meeskonna W6 koondtöösse. Grupi koondnarratiiv ja asukohtade võrdlus on eraldi ühine töö.

## 13. Artefaktid

- [Power BI fail](daca_data_w6_role_b_2026-07-30.pbix)
- [Kuvatõmmis](screenshots/w6_role_b_tartu_kaupluse_dashboard.png)
- [Lühike README](README.md)
- [Isiklik portfoolioversioon](https://github.com/HelenTanner3/daca-portfolio/tree/main/week-6)
