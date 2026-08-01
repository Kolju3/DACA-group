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
| **B** | **Kalju** | **Marketing Dashboard (Anna vaade)** | Müügitrendid, top tooted ja linnade jaotus (Python / Streamlit) | [Kalju kaust](../individual/kalju/) |
| **C** | **Natalia** | **Operations Dashboard (Liis'i vaade)** | Inventuur, laoseisude müügi- ja ostuväärtus, kriitiline ülevaru (Power BI) | [Natalia kaust](../individual/natalia/) |
| **D** | **Olga** | **Investor Dashboard (Koondvaade)** | AOV, kogumüük, tellimuste arv ja aastate lõike müügitrend (Power BI) | [Olga kaust](../individual/olga/) |

---

## 🎯 Juhtkonna TOP 5 koondmõõdikut (Executive Summary)

| Domeen | Koondnumber | Juhtimistähendus | Staatus |
|---|---:|---|---|
| **Kogu UrbanStyle** | **2,91M € müügitulu / 10 118 tellimust** | Kogu ajaloolise müügi kontrollsumma ja maht | Valideeritud |
| **Müügi kasv (Roll A)** | **1,47M € käivet 2024. a (+19,1% kasv)** | 2024 oli tugev kasvuaasta; enamik linnu kasvas (v.a Valga) | Valideeritud |
| **Keskmine Ostukorv (Roll D)** | **287,53 € (AOV)** | Tugev ja stabiilne tellimuse väärtus läbi perioodide | Valideeritud |
| **Lao Kapital (Roll C)** | **44,24M € ostuväärtus / 67,54M € müügiväärtus** | **🚩 PUNANE LIPP:** Pealaos (*ladu*) seisab hiiglaslik ülevaru (377K ühikut) | Kriitiline leid |
| **Regionaalne müük (Roll C & B)** | **Tallinn (37,5%) + Online (34,6%) = 72,1%** | Enamik müügist on koondunud pealinna ja veebikanalisse | Valideeritud |

---

## 🔍 Peamised leiud rollide lõikes

### 📈 Roll A: CEO Dashboard (Helen) — Kristi vaade
* **Tulemus:** Power BI vaade kuise müügitulu võrdlusega (*2023 vs 2024*) ja linnade filtriga.
* **Peamised numbrid:** 2024. aasta müügitulu oli **1,47M €** (+19,1% võrreldes 2023. aastaga) ja ostnud kliente **2 113**.
* **Järeldus:** Kasv oli positiivne peaaegu kõigil kuudel (tipphetk detsembris). Linnade lõikes kasvas enamik regioone, vaid Valga tulemus jäi eelmise aasta tasemele.

---

### 📣 Roll B: Marketing Dashboard (Kalju) — Anna vaade
* **Tulemus:** Interaktiivne Streamlit/Plotly rakendus müügitrendide, asukohtade ja top toodete filtreerimiseks.
* **Peamised numbrid:** Tuvastas top tooted müügitulu järgi (kõige edukam: *Õhuline Sünteetiline Spordidressup*, üle 25K €) ning kinnitas, et Tallinn (38.6%) ja Tartu (20%) on suurimad füüsilised turud.
* **Märkus:** Rakenduse päises kasutusel olnud pealkiri kergelt varieerus, kuid sisu keskendub turundus- ja tooteandmete analüüsile.

---

### 📦 Roll C: Operations Dashboard (Natalia) — Liis'i vaade
* **Tulemus:** Lao ja inventuuri põhjalik Power BI analüüs koos müügi jaotusega linnade kaupa.
* **Peamised numbrid:** Laos on kokku **377 000 ühikut kaupa**, mille ostuväärtus on **44,24M €** ja potentsiaalne müügiväärtus **67,54M €**.
* **🚩 Punane lipp:** Aastase ~1,5M–2,9M € käibe juures on laos kinni **44,24 miljonit eurot kapitali**. Suurimad kogused seisavad pealaos (`ladu`) kategooriates *meeste_riided* (101K tk) ja *jalanõud* (86K tk).

---

### 💼 Roll D: Investor Dashboard (Olga) — Koondvaade
* **Tulemus:** Power BI koondvaade investoritele, mis koondab peamised finantsmõõdikud ühele ekraanile.
* **Peamised numbrid:** Kogukäive **2,91M €**, keskmine tellimuse väärtus (AOV) **287,53 €** ja kokku **10 118 tellimust** (10.118K).
* **⚠️ Märkus 2025–2026 aastatrendi kohta:** Graafikul nähtav langus alates 2025. aastast on tingitud **andmekate piirangust (pooleliolevad perioodid)**, mitte ettevõtte tegevuse kukkumisest.

---

## 🚨 Operatiivne tegevuskava juhtkonnale

1. **Lao optimeerimine:** Vabastada pealaost (*ladu*) seisev kaup, suunates selle kõige kõrgema nõudlusega kohtadesse (**Tallinn 37,5%** ja **Online 34,6%**).
2. **Andmekvaliteet ja perioodid:** Täpsustada 2025.–2026. aasta andmesisestust, et tagada investoritele korrektne ja ajakohane vaade.

---

## ✅ Kvaliteedikontroll

- [x] Kõik neli rolli (Helen - A, Kalju - B, Natalia - C, Olga - D) on selgelt eraldatud
- [x] KPI kaardid sisaldavad võrdluskonteksti (AOV, kasv %, koguväärtused)
- [x] Lao kapitaliseerituse risk ("punane lipp") on selgelt välja toodud
- [x] Andmete piirangud (2025-2026 perioodide andmekate) on dokumenteeritud
