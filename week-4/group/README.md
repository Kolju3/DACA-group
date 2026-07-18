# Nädal 4 – SQL agregatsioon: grupi koondtöö

**Meeskond:** Operations Intelligence  
**Projekt:** UrbanStyle.ltd andmeanalüüsi simulatsioon  
**Teema:** SQL agregatsioon  
**Keskkond:** Supabase / PostgreSQL  

## Ülesande eesmärk

Nädal 4 eesmärk oli muuta müügi-, kliendi-, toote-, inventuuri- ja turundusandmed juhtkonnale kasutatavateks koondnäitajateks.

UrbanStyle’i tegevjuht Kristi Tamm vajab juhatuse koosolekuks vastuseid järgmistele küsimustele:

- kuidas muutus müük ajas;
- millised kliendigrupid loovad enim väärtust;
- millised tootekategooriad vajavad juhtimisotsust;
- millised turunduskanalid seostuvad suurima müügimahuga;
- milliseid numbreid saab andmekvaliteedi piiranguid arvestades usaldada.

Töös kasutati `GROUP BY`, agregaatfunktsioone, `HAVING`-filtrit, CTE-sid ning window function’e.

## Meeskonna rollid

| Roll | Vastutaja | Analüüsidomeen | Individuaalne töö |
|---|---|---|---|
| A | Kalju | Müügi koondandmed ja trendid | [Roll A kaust](../individual/kalju/) |
| B | Natalia | Kliendigruppide analüüs | [Roll B kaust](../individual/natalia/) |
| C | Olga | Tootekategooriad ja inventuuristatistika | [Roll C kaust](../individual/olga/) |
| D | Helen | Turunduskanalite efektiivsus ja täiendav QA | [Roll D kaust](../individual/helen/) |

## Kristile: TOP 5 koondnumbrit

| Domeen | Koondnumber | Juhtimistähendus | Staatus |
|---|---:|---|---|
| Kogu UrbanStyle | **10 118 müügitehingut ja 2 909 177,98 € käivet** | Kontrollväärtus, mille vastu võrreldi liidetud ja agregeeritud tulemusi | Valideeritud |
| Müük | **2024 käive 1 470 358,02 €; kasv 2023. aastaga võrreldes 19,08%** | 2024 oli tugevam aasta, kuid hilisemate perioodide andmekate vajab kontrolli | Valideeritud `sales` koondiga |
| Kliendid | **18 VIP-klienti; keskmine käive 745,20 €** | Väikest kõrge väärtusega gruppi tasub hoida personaalse lojaalsustegevusega | Roll B esitatud; populatsioon vajab ristkontrolli |
| Tooted | **`meeste_riided`: 4 121 müüdud ühikut** | Suurima müügikogusega kategooria vajab nõudlusele vastavat varude planeerimist | Roll C esitatud; laoseisu näitaja puudub |
| Turundus | **`google_organic`: 666 444,98 € käivet ja 2 273 tellimust** | Suurima valideeritud müügimahuga tuvastatud kanal | Valideeritud standardiseeritud kanalitega |

## Peamised leiud

### Müük

Täieliku `sales` tabeli kontrolli järgi kasvas 2024. aasta käive 2023. aastaga võrreldes **19,08%** ning tellimuste arv **20,19%**. Suurim kuine käive oli 2024. aasta detsembris: **170 623,28 €**.

Roll A individuaalses kokkuvõttes esitatud ligikaudu 50% kasv ei ole otseselt võrreldav kogu `sales` tabeli aastase kontrolliga, sest kasutatud perioodid, filtrid või võrdlusloogika võivad erineda. Grupi juhtimisnumbrina kasutame kontrollitud aastavõrdlust 19,08%.

### Kliendid

Roll B jaotas analüüsitud kliendid kolme gruppi:

| Segment | Kliente | Keskmine käive |
|---|---:|---:|
| VIP | 18 | 745,20 € |
| Regular | 54 | 312,50 € |
| Uus | 142 | 64,80 € |

Segmentatsioon annab selge tegevusloogika: VIP-klientide hoidmine, Regular-klientide kasvatamine ja uute klientide automatiseeritud järelkommunikatsioon.

Kliendisegmentide koguarv 214 ei ole grupi materjalides veel täielikult ristkontrollitud kogu müügiklientide populatsiooni ja kasutatud `HAVING`-filtriga. Seetõttu tuleb segmentide numbreid esitleda Roll B analüüsitud kliendikogumi, mitte kogu UrbanStyle’i kliendibaasina.

### Tooted ja inventuur

Roll C tulemuste järgi:

| Kategooria | Tooteid | Keskmine hind | Müüdud kogus |
|---|---:|---:|---:|
| `meeste_riided` | 82 | 189,91 € | 4 121 |
| `jalanõusid` | 73 | 214,10 € | 3 737 |
| `laste_riided` | 70 | 85,30 € | 3 686 |
| `naiste_riided` | 70 | 192,58 € | 3 604 |
| `aksessuaarid` | 67 | 125,71 € | 3 231 |

`meeste_riided` oli suurima müügikogusega kategooria ning `jalanõusid` kõrgeima keskmise hinnaga kategooria.

Nädala ametlik Roll C ülesanne hõlmas ka laoseisu ja `inventory_movements` andmeid. Avalikus väljundis on tõendatud kategooria-, hinna- ja müügikoguse analüüs, kuid tegelikku laoseisu, ülevaru või juurde tellimise riski ei ole veel kvantifitseeritud. Seetõttu nimetame seda grupi kokkuvõttes tootekategooriate, mitte lõplikuks inventuuririski analüüsiks.

### Turundus

Enne analüüsi standardiseeriti 19 algset `source` väärtust 10 kanaliks uues `source_clean` väljas.

Valideeritud kanalitulemuste järgi:

| Kanal | Käive | Tellimusi | Keskmine tellimus |
|---|---:|---:|---:|
| `google_organic` | 666 444,98 € | 2 273 | 293,20 € |
| `facebook_ads` | 469 933,25 € | 1 635 | 287,42 € |
| `direct` | 420 103,22 € | 1 505 | 279,14 € |
| `email_campaign` | 300 296,85 € | 1 024 | 293,26 € |
| `instagram` | 262 112,79 € | 877 | 298,87 € |

- `google_organic` oli suurima valideeritud käibe ja tellimuste arvuga kanal.
- `facebook_ads` oli tuvastatud kanalitest suurima müügiga kliendi kohta.
- `instagram` oli suurima keskmise tellimusväärtusega kanal.
- tegelikku ROI-d ei saa arvutada, sest kampaaniakulud puuduvad.

## Suurim üllatus

Otsene `sales`–`customers`–`web_logs` JOIN andis **34 527 628,19 € käivet**, kuigi `sales` tabeli tegelik kontrollsumma oli **2 909 177,98 €**.

JOIN:

- suurendas ridade arvu 10 118 realt 121 131 reale;
- ülehindas käivet 11,87 korda;
- jättis samal ajal `INNER JOIN customers` tõttu välja 988 müüki.

See näitas, et tehniliselt töötav päring võib anda äriliselt vale tulemuse. Lõplikus turundusanalüüsis valiti igale kliendile `ROW_NUMBER()` abil üks viimane teadaolev standardiseeritud kanal.

## Soovitused Annale ja Kristile

1. **Müük ja kliendid:** hoida VIP-kliente personaalselt ning suunata Regular-segmendile ristmüügi ja ostusageduse kasvatamise tegevused.
2. **Tooted ja varud:** planeerida eeskätt `meeste_riided` ja `jalanõusid` kategooriate varusid, kuid enne tellimisotsuseid lisada analüüsi tegelik laoseis ja laoliikumised.
3. **Turundus:** toetada suure mahuga `google_organic` kanalit, kuid võrrelda tasulisi kanaleid alles pärast kampaaniakulude lisamist.
4. **Andmekvaliteet:** kasutada analüüsis standardiseeritud `source_clean` väärtust ning valideerida kõik JOIN-id algse ridade arvu ja käibe vastu.
5. **Atribuutika:** siduda kanal tulevikus konkreetse sessiooni või müügitehinguga, mitte kogu kliendi viimase teadaoleva kanaliga.

## Puuduvad või täiendamist vajavad andmed

- turunduskampaaniate kulud, kampaania ID-d ja UTM-parameetrid;
- tehingu ja veebisessiooni otsene seos;
- brutomarginaal ja toote omahind;
- tegelik laoseis, laoliikumised, tellimispunkt ja tarneaeg;
- tagastused ja tühistatud tehingud;
- kliendisegmentatsiooni täielik populatsioon ja filtrite dokumentatsioon;
- 2025.–2026. aasta andmekatte terviklikkuse kontroll.

## Kvaliteedikontroll

| Kontroll | Tulemus |
|---|---|
| Kõik neli domeeni on koondis esindatud | OK |
| Kogu müügi kontrollsumma on teada | OK |
| Turunduse JOIN-i kordistumine on tuvastatud ja parandatud | OK |
| Turunduskanalite nimetused on standardiseeritud | OK |
| Roll A kasvunumber on ühtlustatud kogu `sales` aastakoondiga | PARANDATUD |
| Roll B segmentide populatsioon on kogu kliendibaasiga ristkontrollitud | VAJAB KONTROLLI |
| Roll C sisaldab ametlikus ülesandes nõutud laoseisu mõõdikuid | OSALISELT |
| Kampaaniate tegelik ROI on arvutatav | EI – kulud puuduvad |

## Grupifailid

| Fail | Kirjeldus |
|---|---|
| [README.md](./README.md) | Grupi koondülevaade ja peamised tulemused |
| [W4_GROUP_DETAILNE_ANALUUS.md](./W4_GROUP_DETAILNE_ANALUUS.md) | Rollideülene analüüs, ristkontroll ja piirangud |
| [W4_GROUP_PRESENTATSIOONI_ALUS.md](./W4_GROUP_PRESENTATSIOONI_ALUS.md) | 3-minutilise juhtkonna esitluse alus ja kõneleja märkmed |

## Peamine õppetund

**Agregatsioon annab juhtimisinfo alles siis, kui grupid, filtrid, JOIN-i detailsusaste ja kontrollsummad on enne järelduste tegemist üheselt määratletud.**

