# Nädal 4 – SQL agregatsioon: grupi koondülevaade

**Meeskond:** Operations Intelligence  
**Projekt:** UrbanStyle.ltd andmeanalüüsi simulatsioon  
**Nädal:** 4  
**Teema:** SQL agregatsioon – `GROUP BY`, agregaatfunktsioonid, `HAVING`, CTE-d ja window function'id  
**Keskkond:** Supabase / PostgreSQL  

---

## Ülesande eesmärk

Nädal 4 eesmärk oli muuta üksikud müügi-, kliendi-, toote-, varude- ja turundusread juhtimisotsusteks kasutatavateks koondnäitajateks.

UrbanStyle’i juhtkonna vaatest oli äriküsimus järgmine: **millised müügi-, kliendi-, toote- ja turundusmustrid peaksid Kristi Tammel olema juhatuse koosolekul nähtavad?**

Grupitöö fookus oli:

- koondada müük ajas, asukohtade ja kategooriate lõikes;
- segmenteerida kliendid väärtuse järgi;
- hinnata tootekategooriate müüki ja hinnataset;
- analüüsida turunduskanalite mõju müügile;
- kontrollida, millised piirangud mõjutavad tulemuste tõlgendamist.

---

## Kasutatud SQL-võtted

| Võte | Kasutus grupitöös |
|---|---|
| `GROUP BY` | Kuude, kanalite, kategooriate, segmentide ja asukohtade koondamiseks |
| `COUNT()` | Tellimuste, klientide, toodete ja ridade loendamiseks |
| `COUNT(DISTINCT ...)` | Unikaalsete klientide ja toodete arvu leidmiseks |
| `SUM()` | Kogukäibe ja müüdud koguste arvutamiseks |
| `AVG()` | Keskmise tellimusväärtuse, keskmise käibe ja keskmise hinna arvutamiseks |
| `MIN()` / `MAX()` | Hinnavahemike ja kontrollväärtuste leidmiseks |
| `HAVING` | Grupeeritud tulemuste filtreerimiseks |
| CTE / `WITH` | Mitmeastmeliste koondpäringute loetavamaks muutmiseks |
| Window functions | Trendide, järjestuste ja kategooriasiseste positsioonide arvutamiseks |

---

## Rollid ja individuaalsed panused

| Roll | Vastutaja | Fookus | Peamine väljund |
|---|---|---|---|
| Müügi ja kategooriate dünaamiline analüüs | Kalju | Müügitrendid, asukohad, kategooriad, sesoonsus | Ajalised ja kategooriapõhised müügikoondid |
| Kliendigruppide analüüs | Natalia | VIP / Regular / Uus segmendid | Kliendisegmentide koondtabel ja soovitused |
| Tootekategooriate ja varude analüüs | Olga | Kategooriate hinnad, müügikogused ja laovaru prioriteedid | Kategooriapõhine tootemüügi ja hinna ülevaade |
| Turunduskampaaniate efektiivsus | Helen | Turunduskanalid, käive, tellimused, attribution-piirangud | Valideeritud kanalipõhine turundusanalüüs |

---

## Peamised koondleiud

### 1. Müük kasvas 2023–2024 perioodil, kuid 2025 vajab eraldi kontrolli

Kalju dünaamiline müügianalüüs viitab, et 2023–2024 perioodil kasvas müük ligikaudu **50%**. Kiirema kasvuga kanalitena tõusid esile **online** ja **Tartu**. Suurema käibega tootekategooriatena tulid välja **meeste_riided**, **naiste_riided** ja **jalanõusid**.

Samas näitas analüüs 2025. aasta kohta järsku langust. Seda ei tohiks käsitleda kohe ärilise langusena ilma andmekvaliteedi kontrollita. Võimalik, et tegemist on puuduliku perioodi, mittetäieliku impordi või andmete katkemisega.

**Tõlgendus:** 2023–2024 kasv on juhtkonnale positiivne signaal, kuid 2025 langus vajab enne juhatusele esitamist valideerimist.

---

### 2. Müügis esineb selge sesoonsus

Kalju analüüsi järgi on suvekuudel, eriti juuni–august, müük ligikaudu **20% kõrgem**. Samuti ilmnes aastalõpu kampaaniate mõju, kus aasta lõpus tekkis ühekuuline müügikasv.

**Tõlgendus:** varude, kampaaniate ja personalivajaduse planeerimisel tuleb arvestada suvise nõudluse kasvuga ning aasta lõpu kampaaniate mõjuga.

---

### 3. Kliendibaasi väärtus on kontsentreeritud väiksemasse segmenti

Natalia kliendisegmentide analüüs jaotas kliendid kogukäibe alusel kolmeks:

| Segment | Piirmäär | Klientide arv | Keskmine käive | Äriline fookus |
|---|---:|---:|---:|---|
| VIP | üle 500 € | 18 | 745,20 € | Personaalne lojaalsus ja hoidmine |
| Regular | 150–500 € | 54 | 312,50 € | Ristmüük ja ostusageduse kasvatamine |
| Uus | alla 150 € | 142 | 64,80 € | Automatiseeritud kordusostu kampaaniad |

**Tõlgendus:** VIP-kliente on vähe, kuid nende väärtus on kõrge. Regular-segment on realistlik kasvukoht. Uusi kliente on kõige rohkem, kuid nad vajavad automatiseeritud järelkommunikatsiooni, et nad ei jääks ühekordseteks ostjateks.

---

### 4. Tootekategooriad on müügikoguselt üsna ühtlased, kuid hinnatasemed erinevad

Olga kategooriaanalüüs näitas, et müüdud kogused on kategooriate vahel suhteliselt sarnased: keskmine müüdud kogus toote kohta jäi ligikaudu **1,78–1,84** vahemikku.

Olulisemad kategoorialeiud:

| Kategooria | Tooteid | Keskmine hind | Müüdud kogus |
|---|---:|---:|---:|
| meeste_riided | 82 | 189,91 € | 4 121 |
| jalanõusid | 73 | 214,10 € | 3 737 |
| laste_riided | 70 | 85,30 € | 3 686 |
| naiste_riided | 70 | 192,58 € | 3 604 |
| aksessuaarid | 67 | 125,71 € | 3 231 |

**Tõlgendus:** meeste_riided annab suurima müügikoguse, jalanõusid on kõrgeima keskmise hinnaga kategooria. Laste_riided on madalama hinnaga, kuid koguseliselt tugev. Varude planeerimisel tuleks prioriteetselt jälgida meeste riideid ja jalanõusid.

---

### 5. Turunduskanalite analüüsis oli tugevaim valideeritud kanal `google_organic`

Helen analüüsis turunduskanalite efektiivsust `sales`, `customers` ja `web_logs` tabelite põhjal. Esialgne otseühendus `customer_id` alusel kordistas müügiridu, sest ühel kliendil võib olla mitu veebikülastust. Lõplikus kontrollitud käsitluses määrati kliendile üks viimane teadaolev kanal.

Valideeritud tulemuses oli suurima kogukäibega kanal:

| Kanal | Kogukäive | Tellimused | Kliendid | Keskmine tellimus |
|---|---:|---:|---:|---:|
| google_organic | 582 912,57 € | 1 994 | 624 | 292,33 € |

Lisaks kasvas `google_organic` käive 2024. aasta novembrist detsembrini **13 834,38 eurolt 33 572,86 euroni**, ehk **142,7%**.

**Tõlgendus:** orgaaniline Google’i kanal on tugeva müügipotentsiaaliga. Samas tuleb arvestada, et tegemist on lihtsustatud kliendipõhise omistamisloogikaga, mitte täieliku tehingupõhise attribution-mudeliga.

---

## Olulised metoodilised piirangud

1. **Turunduse ROI-d ei saa lõplikult arvutada**, sest andmestikus puuduvad kampaaniate kulud.
2. **`web_logs` tabelis on ühe kliendi kohta mitu külastust**, mistõttu otseühendus müügiga kordistab tulemusi.
3. **2025. aasta müügilangus vajab andmekvaliteedi kontrolli**, enne kui seda käsitleda ärilise probleemina.
4. **Tootekategooriate müügikogused näitavad koondpilti**, kuid laoseisu otsusteks on vaja siduda tulemused tegeliku inventory seisuga.
5. **Kliendisegmentide piirmäärad on analüütilised tööpiirid**, mitte ametlik ärireegel. Need vajavad juhtkonna kinnitust.

---

## Soovitused Kristile ja Annale

### 1. Keskenduda kasvu näidanud kanalitele ja asukohtadele

Online ja Tartu näitasid kiiremat kasvu. Neid tasub käsitleda kui prioriteetseid kasvusuundi, kuid otsus peab põhinema kontrollitud perioodiandmetel.

### 2. Kontrollida 2025. aasta andmete täielikkust

Enne 2025. aasta languse juhatusele esitamist tuleb kontrollida, kas kogu aasta või periood on andmetes täielikult kaetud.

### 3. Hoida VIP-kliente personaalselt

VIP-segment on väike, kuid kõrge väärtusega. Nende puhul sobivad personaalsed pakkumised ja erikohtlemine, mitte masskampaaniad.

### 4. Suunata Regular-segmenti ristmüüki

Regular-klientide kasvatamine VIP-tasemele on realistlik kasvuhoob. Neile sobivad täiendtoodete ja kategooriapõhised pakkumised.

### 5. Automatiseerida uute klientide järeltegevused

Uusi kliente on palju, kuid nende keskmine käive on madal. Esimese ostu järel tuleks rakendada automatiseeritud tervitus- ja kordusostukampaaniaid.

### 6. Planeerida varusid sesoonsuse ja kategooria väärtuse järgi

Suveperioodi müügitõus ja meeste_riided / jalanõusid kategooriate tugev positsioon viitavad vajadusele planeerida laovarusid enne müügitippe.

### 7. Standardiseerida turunduskanalite nimetused

Sama turunduskanal esineb mitme kirjapildiga. Kanalite nimetuste standardiseerimine parandaks raportite usaldusväärsust ja vähendaks käsitööd.

---

## Slaidide genereerimise alus

Selle README põhjal saab hiljem koostada 8–10 slaidiga koondesitluse.

Soovitatav slaidistruktuur:

1. **Nädal 4 eesmärk** – SQL agregatsioon kui toorandmete muutmine juhtimisinfoks
2. **Metoodika** – GROUP BY, HAVING, CTE ja window functions
3. **Müügi üldtrend** – 2023–2024 kasv, 2025 kontrollivajadus
4. **Sesoonsus ja kanalid** – suvine kasv, online ja Tartu
5. **Kliendisegmendid** – VIP / Regular / Uus
6. **Tootekategooriad** – müügikogused ja hinnatasemed
7. **Turunduskanalid** – `google_organic` ja attribution-piirang
8. **Riskid ja andmekvaliteedi piirangud**
9. **Soovitused juhtkonnale**
10. **Järgmised sammud**

---

## Failid ja viited

| Kaust / fail | Kirjeldus |
|---|---|
| [`../individual/helen/`](../individual/helen/) | Turunduskanalite efektiivsuse analüüs |
| [`../individual/kalju/`](../individual/kalju/) | Müügi ja kategooriate dünaamiline trendianalüüs |
| [`../individual/natalia/`](../individual/natalia/) | Kliendigruppide segmentatsioon |
| [`../individual/olga/`](../individual/olga/) | Tootekategooriate ja varude analüüs |

---

## Lühikokkuvõte

Nädal 4 töö näitas, et SQL agregatsioon võimaldab muuta UrbanStyle’i detailsed tehingu-, kliendi-, toote- ja turundusandmed juhtimisotsusteks kasutatavaks koondinfoks. Peamine äriline pilt on positiivne: 2023–2024 müük kasvas, online ja Tartu on tugevad kasvusuunad, VIP-kliendid on kõrge väärtusega ning meeste_riided ja jalanõusid on varude planeerimisel prioriteetsed kategooriad.

Samas vajavad enne lõplikku juhtimisotsust kontrolli kolm teemat: 2025. aasta müügilanguse andmekvaliteet, turunduskanalite attribution-loogika ning kampaaniakulude puudumine ROI arvutamiseks.

