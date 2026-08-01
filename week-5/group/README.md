# 📊 Nädal 5 – Andmete visualiseerimine ja töölauad: grupi koondtöö

**Meeskond:** Operations Intelligence  
**Projekt:** UrbanStyle Ltd. andmeanalüüsi simulatsioon  
**Teema:** Interaktiivsed töölauad, KPI-d ja juhtimisvisuaalid (Power BI / Streamlit)  
**Keskkond:** Power BI / Python (Streamlit & Plotly) / PostgreSQL  

---

## 📋 Ülesande eesmärk

Nädal 5 eesmärk oli muuta UrbanStyle'i koondandmed selgeteks, visuaalseteks ja interaktiivseteks töölaudadeks (*dashboards*), mis vastavad otseselt juhtkonna, turunduse, operatsioonide ja investorite kriitilistele äriküsimustele.

Iga meeskonnaliige lõi spetsiifilise vaate (Rollid A–D), et tagada otsustajatele ülikiire (10–30 sekundiga) arusaam ettevõtte tervisest, müügikanalite efektiivsusest, laoseisude lahknevustest ja üldisest kasvupotentsiaalist.

---

## 👥 Meeskonna rollid ja vastutus

| Roll | Vastutaja | Töölaua vaade (Dashboard) | Peamine eesmärk ja tööriist | Lingid |
|---|---|---|---|---|
| **A** | **Helen** | **CEO Dashboard (Kristi vaade)** | Müügitulu kuine trend (2023 vs 2024), kasv % ja linnade võrdlus (Power BI) | [Helen'i kaust](../individual/helen/) |
| **B** | **Kalju** | **Marketing & Investor Dashboard** | Müügikanalite ja -trendide analüüs, top tooted (Python / Streamlit) | [Kalju kaust](../individual/kalju/) |
| **C** | **Natalia** | **Operations Dashboard (Liis'i vaade)** | Inventuur, laoseisude müügi- ja ostuväärtus, kriitiline ülevaru (Power BI) | [Natalia kaust](../individual/natalia/) |
| **D** | **Olga** | **Investor Dashboard (Koondvaade)** | Süntees investoritele: AOV, kogumüük, tellimused ja aastatrend (Power BI) | [Olga kaust](../individual/olga/) |

---

## 🎯 Juhtkonna TOP 5 koondmõõdikut (Executive Summary)

| Domeen | Koondnumber | Juhtimistähendus | Staatus |
|---|---:|---|---|
| **Kogu UrbanStyle** | **2,91M € müügitulu / 10 118 tellimust** | Kogu ajaloolise müügi kontrollsumma ja maht | Valideeritud |
| **Müügi kasv (Roll A)** | **1,47M € käivet 2024. a (+19,1% kasv)** | 2024 oli tugev kasvuaasta; enamik linnu kasvas (v.a Valga) | Valideeritud |
| **Keskmine Ostukorv (Roll D)** | **287,53 € (AOV)** | Tugev ja stabiilne tellimuse väärtus läbi perioodide | Valideeritud |
| **Lao Kapital (Roll C)** | **44,24M € ostuväärtus / 67,54M € müügiväärtus** | **🚩 PUNANE LIPP:** Pealaos (*ladu*) seisab hiiglaslik ülevaru (377K ühikut) | Kriitiline leid |
| **Regionaalne müük (Roll C)** | **Tallinn (37,5%) + Online (34,6%) = 72,1%** | Enamik müügist on koondunud pealinna ja veebikanalisse | Valideeritud |

---

## 🔍 Peamised leiud rollide lõikes

### 📈 Roll A: CEO Dashboard (Helen) — Kristi vaade
* **Tulemus:** Power BI vaade kuise võrdlusega (*2023 vs 2024*) ja linnade filtriga.
* **Peamised numbrid:** 2024. aasta müügitulu oli **1,47M €** (+19,1% võrreldes 2023. aastaga) ja ostnud kliente **2 113**.
* **Järeldus:** Kasv oli positiivne peaaegu kõigil kuudel (tipphetk detsembris). Linnade lõikes kasvas enamik regioone, vaid Valga tulemus jäi eelmise aasta tasemele.

---

### 📣 Roll B & D: Investor & Turundusvaade (Kalju & Olga)
* **Tulemus:** Olga luua oli Power BI koondvaade ning Kalju ehitas interaktiivse Streamlit/Plotly veebirakenduse.
* **Peamised numbrid:** Ajalooline kogukäive **2,91M €**, keskmine tellimus **287,53 €** ja kokku **10 118 tellimust**.
* **⚠️ Märkus aastate 2025–2026 kohta:** Graafikutel nähtav langus 2025. ja 2026. aastal on tingitud **andmekate piirangust/pooleliolevatest perioodidest**, mitte äritegevuse mahtude tegelikust kukkumisest.

---

### 📦 Roll C: Operations Dashboard (Natalia) — Liis'i vaade
* **Tulemus:** Lao ja inventuuri põhjalik analüüs koos müügi jaotusega linnade kaupa.
* **Peamised numbrid:** Laos on kokku **377 000 ühikut kaupa**, mille ostuväärtus on **44,24M €** ja potentsiaalne müügiväärtus **67,54M €**.
* **🚩 Punane lipp:** Aastase ~1,5M–2,9M € käibe juures on laos kinni **44,24 miljonit eurot kapitali**. Suurimad kogused seisavad pealaos (`ladu`) kategooriates *meeste_riided* (101K tk) ja *jalanõud* (86K tk).

---

## 🚨 Operatiivne tegevuskava juhtkonnale

1. **Lao optimeerimine:** Vabastada pealaost (*ladu*) seisev kaup, suunates selle kõige kõrgema nõudlusega kohtadesse (**Tallinn 37,5%** ja **Online 34,6%**).
2. **Andmekvaliteet ja perioodid:** Täpsustada 2025.–2026. aasta andmesisestust, et tagada investoritele korrektne ajakohane vaade.

---

## ✅ Kvaliteedikontroll

- [x] Kõik vaated (CEO, Operations, Investor) on visuaalselt teostatud
- [x] KPI kaardid sisaldavad konteksti (AOV, kasv %, koguväärtused)
- [x] Lao kapitaliseerituse risk ("punane lipp") on selgelt välja toodud
- [x] Andmete piirangud (2025-2026 andmekate) on dokumenteeritud
