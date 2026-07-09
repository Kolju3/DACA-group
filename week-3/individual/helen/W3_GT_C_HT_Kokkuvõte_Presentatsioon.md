# Analüüsi kokkuvõte — Tooted + inventuur

## Ühe lausega järeldus

UrbanStyle’i toote- ja inventuuriandmed näitavad tugevat müüki jalanõude ja meeste riiete kategoorias, kuid varude juhtimise risk on kahesuunaline: osa tooteid vajab täiendamist või andmekvaliteedi kontrolli, samal ajal kui suur hulk ridu viitab võimalikule ülevarule.

---

## Peamised arvud

| Teema | Tulemus | Tõlgendus |
|---|---:|---|
| Müümata tooted | 12 | Kataloogis on tooteid, millel puudub müügiseos. Need vajavad ärilist kontrolli. |
| Suurim kategooria kogumüügi järgi | jalanõusid — 774 034.75 | Jalanõud on käibe seisukohalt tugevaim kategooria. |
| Suurim kategooria müügikordade järgi | meeste_riided — 2 266 müüki | Meeste riided liiguvad mahult kõige rohkem. |
| Inventuuri ridu | 1 412 | Tegemist on toote-asukoha taseme inventuuriandmetega. |
| `TELLI JUURDE` ridu | 221 | Need read on tellimispunktist madalamal või sellega võrdsed. |
| `KONTROLLI LAOSEISU` ridu | 10 | Negatiivsed laoseisud; andmekvaliteedi või protsessivea kandidaadid. |
| `INVENTUUR PUUDUB` ridu | 12 | Neid ei tohi vaikimisi lugeda korras seisuks. |
| `VÕIMALIK ÜLEVARU` ridu | 730 | Laoseis on vähemalt 3 korda suurem kui tellimispunkt. Vajab eraldi kontrolli. |
| Ülevaru ridu vähemalt 10x kordajaga | 214 | Võimalik kapitali sidumine või andmeviga. |
| Ülevaru ridu vähemalt 100x kordajaga | 31 | Ekstreemsed juhtumid, mida tuleks kontrollida esimesena. |
| Suurim ülevaru kordaja | 628.60x | Tõenäoline andme- või varude planeerimise probleem. |

---

## Mida ma leidsin?

1. **Müümata toodete probleem on olemas, kuid piiratud mahuga.** 12 toodet on kataloogis olemas, kuid neid ei ole müügitabelis kordagi kasutatud.
2. **Jalanõud on suurima kogumüügiga kategooria.** See kategooria annab suurema käibe kui meeste riided, kuigi meeste riietel on rohkem müügikordi.
3. **TOP 10 toodetes domineerivad jalanõud ja naiste riided.** See viitab, et müügiedu ei jaotu kõigi kategooriate vahel ühtlaselt.
4. **Inventuuris on madala laoseisuga ridu.** 221 toote-asukoha rida on tellimispunktist madalamal või sellega võrdsed.
5. **Negatiivsed laoseisud vajavad eraldi tähelepanu.** Need ei ole lihtsalt “telli juurde” juhtumid, vaid võimalikud süsteemi- või protsessivead.
6. **Inventuurivasteta tooted tuleb eraldi märgistada.** Kui `LEFT JOIN` annab inventuuri veergudes `NULL`, ei tohiks seda äriloogikas lugeda korras seisuks.
7. **Lisaks puudujääkidele esineb võimalik ülevaru.** 730 rida on vähemalt 3 korda üle tellimispunkti. See ei tõenda automaatselt ülevaru, kuid on selge riskimärgis.
8. **Ekstreemsed laoseisud vajavad eraldi kontrolli.** 214 rida on vähemalt 10 korda ja 31 rida vähemalt 100 korda üle tellimispunkti.

---

## Suurim üllatus

Suurim üllatus oli see, et inventuuriprobleem ei ole ainult madal laoseis või negatiivne laoseis. Väga paljudel ridadel on laoseis tellimispunktist mitu korda kõrgem. See tähendab, et UrbanStyle võib korraga seista silmitsi kahe riskiga: müügikaotus puudujäägi tõttu ja kapitali sidumine ülevarus.

---

## Ärisoovitus Toomasele

Toomas peaks inventuuri käsitlema nelja eraldi töövoona:

1. **Andmekvaliteet:** kontrollida negatiivseid laoseise ja inventuurivasteta tooteid.
2. **Puudujääk:** vaadata üle `TELLI JUURDE` read, eriti tugeva müügiga kategooriates.
3. **Ülevaru:** analüüsida ridu, kus laoseis on vähemalt 3 korda üle tellimispunkti; ekstreemsed 10x, 20x ja 100x juhtumid tuleks kontrollida esimesena.
4. **Sortiment:** kontrollida 12 müümata toodet ja otsustada, kas need on aktiivsed, lõpetatud, hooajalised või fantoomtooted.

---

## Soovitus äripoolele

Jalanõud ja meeste riided vajavad eraldi tähelepanu, sest need on müügi seisukohalt kõige tugevamad kategooriad. Samas ei piisa ainult juurde tellimise vaatest. Varude planeerimisel tuleb kontrollida ka seda, kas osa laoseise on põhjendamatult suured ning kas need seovad kapitali ilma piisava müügikäibeta.

---

## Puuduvad andmed

Analüüsi põhjal jäi puudu järgmistest andmetest:

- toote staatus: aktiivne, lõpetatud, testtoode, hooajaline või kampaaniatoode;
- toote lisamise kuupäev;
- viimase müügi kuupäev ja müügikiirus;
- ostutellimused ja juba teel olevad kogused;
- tarnija ja tarneaeg;
- laoliikumiste ajalugu;
- omahind ja marginaal;
- miinimum- ja maksimumvaru poliitika;
- kampaania- ja allahindlusinfo.

---

## Esitluse lühitekst

Mina uurisin toodete, müügi ja inventuuri seoseid `LEFT JOIN` ja `INNER JOIN` päringutega. Leidsin, et kataloogis on 12 toodet, mida pole müüdud, ning suurima kogumüügi annab jalanõude kategooria. Inventuuris on 221 madala laoseisuga rida, 10 negatiivset laoseisu ja 12 inventuurivasteta toodet. Täiendav ülevaru kontroll näitas aga veel suuremat riski: 730 rida on vähemalt 3 korda üle tellimispunkti, sh 31 rida vähemalt 100 korda üle. Seetõttu soovitan Toomasel käsitleda inventuuri mitte ainult juurde tellimise vaatest, vaid eristada puudujäägid, andmevead ja võimalik ülevaru.

---

## Demo jaoks üks lause

Inventuurianalüüs näitas, et UrbanStyle’i varude probleem on kahesuunaline: osa tooteid vajab juurde tellimist või andmekvaliteedi kontrolli, kuid samal ajal on suur osa laoseise tellimispunktiga võrreldes ebaproportsionaalselt kõrged.
