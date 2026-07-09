# Nädal 3: Tooted + inventuur — LEFT JOIN analüüs

## Projekti kontekst

UrbanStyle’i andmestikus analüüsiti toodete, müükide ja inventuuri seoseid. Fookus oli küsimusel, kas tootekataloogis olevad tooted tegelikult müüvad ning kas laoseis toetab ärilisi otsuseid.

Analüüs vastab eelkõige järgmistele küsimustele:

- Millised tooted on kataloogis, aga ei ole kunagi müüki tekitanud?
- Kui suur on müümata toodete probleem?
- Millised tooted ja kategooriad müüvad kõige paremini?
- Milliste toodete laoseis vajab tähelepanu?
- Kas andmetes on inventuuri kvaliteediprobleeme?

## Kasutatud tabelid

| Tabel | Roll analüüsis |
|---|---|
| `products` | Tootekataloog: tootenimi, kategooria, alamkategooria, jaehind |
| `sales` | Müügitehingud: müügi ID, toote ID, kogus, müügisumma |
| `inventory` | Laoseis: asukoht, saadaolev kogus, tellimispunkt |

## Kasutatud SQL loogika

Analüüsis kasutati järgmisi SQL võtteid:

- `LEFT JOIN` — toodete säilitamiseks ka siis, kui müüki või inventuuri vastet ei ole.
- `INNER JOIN` — ainult tegelikult müüdud toodete leidmiseks.
- `COUNT`, `COUNT(DISTINCT ...)`, `SUM`, `AVG` — mahtude ja müügitulemuste koondamiseks.
- `GROUP BY` — tulemuste koondamiseks toote ja kategooria tasemel.
- `CASE WHEN` — inventuuri staatuse määramiseks.
- `ORDER BY` ja `LIMIT` — olulisemate tulemuste esiletoomiseks.

---

## 1. Müümata tooted

Päring `products LEFT JOIN sales` tuvastas tooted, millel puudub vaste müügitabelis.

**Tulemus:** kataloogis on **12 toodet**, mida ei ole müüdud.

Need tooted on äriliselt olulised, sest nad võivad tähendada üht järgmistest olukordadest:

- toode on kataloogis, aga pole veel müügiks aktiveeritud;
- toode on vananenud või ekslikult kataloogi jäänud;
- toode on andmeimpordi käigus tekkinud fantoomkirje;
- müügitabeli ja tootetabeli seosed vajavad kontrolli.

**Järeldus:** neid 12 toodet ei tohiks kohe kustutada. Enne tuleb kontrollida, kas need on aktiivsed tooted, lõpetatud tooted, testandmed või importimisel tekkinud fantoomkirjed.

---

## 2. TOP 10 enim müüdud toodet kogumüügi järgi

Enim müüdud toodete leidmiseks kasutati `products INNER JOIN sales` loogikat, sest siin sooviti näha ainult neid tooteid, millel on tegelik müük.

| Koht | Toode | Kategooria | Alamkategooria | Müüdud kordi | Kogumüük |
|---:|---|---|---|---:|---:|
| 1 | Õhuline sünteetiline sporditossud | jalanõusid | tossud | 35 | 27 347.04 |
| 2 | Trendikas goretex oxfordid | jalanõusid | kingad | 32 | 23 376.15 |
| 3 | Praktiline viskoosne jakk | naiste_riided | jakid | 35 | 22 188.80 |
| 4 | Praktiline džersii seelik | naiste_riided | seelikud | 37 | 22 039.98 |
| 5 | Boheemlaslik puuvillane tuulejope | naiste_riided | jakid | 30 | 21 309.96 |
| 6 | Õhuline sünteetiline kõrge kontsaga kingad | jalanõusid | kontsad | 38 | 21 295.56 |
| 7 | Praktiline kangast kõrge kontsaga kingad | jalanõusid | kontsad | 37 | 21 118.68 |
| 8 | Luksuslik villane pahkluu saapad | jalanõusid | botased | 28 | 19 704.87 |
| 9 | Praktiline merino villane parka | meeste_riided | jakid | 30 | 19 620.45 |
| 10 | Õhuline linane jakk | naiste_riided | jakid | 41 | 19 393.29 |

**Järeldus:** TOP 10 toodetes domineerivad jalanõud ja naiste riided. See viitab, et need kategooriad on sortimendi müügitulu seisukohalt kõige tugevamad.

---

## 3. Müügianalüüs kategooriate kaupa

Kategooriate analüüs näitas, millised kategooriad annavad suurima kogumüügi.

| Kategooria | Tooteid | Müüke | Kogumüük |
|---|---:|---:|---:|
| jalanõusid | 73 | 2 031 | 774 034.75 |
| meeste_riided | 82 | 2 266 | 749 798.72 |
| naiste_riided | 70 | 2 022 | 686 464.24 |
| aksessuaarid | 67 | 1 772 | 393 035.82 |
| laste_riided | 70 | 2 027 | 305 844.45 |

**Peamine leid:** suurima kogumüügiga kategooria on **jalanõusid**, kuigi meeste riietel on rohkem müügikordi. See tähendab, et jalanõude keskmine müügiväärtus on tõenäoliselt kõrgem.

**Äriline tõlgendus:** UrbanStyle peaks sortimendi ja varude planeerimisel pöörama eraldi tähelepanu jalanõudele ja meeste riietele. Jalanõud toovad suurima käibe, meeste riided aga suurima tehingute mahu.

---

## 4. Inventuuri soovitused

Inventuuri päringus kasutati loogikat:

```sql
CASE
    WHEN i.quantity_available <= i.reorder_point THEN 'TELLI JUURDE'
    ELSE 'OK'
END AS staatus
```

Päring tagastas **1 412 toote-asukoha rida**.

| Näitaja | Tulemus |
|---|---:|
| Inventuuri ridu kokku | 1 412 |
| `TELLI JUURDE` staatuses ridu | 231 |
| `OK` staatuses ridu | 1 181 |
| Negatiivse laoseisuga ridu | 10 |
| Null-laoseisuga ridu | 7 |
| Inventuurivasteta tooteridu | 12 |

### Inventuuri tähelepanekud kategooriate kaupa

| Kategooria | Inventuuri ridu | `TELLI JUURDE` ridu | Negatiivse laoseisuga ridu | Inventuurivasteta ridu |
|---|---:|---:|---:|---:|
| meeste_riided | 325 | 58 | 2 | 1 |
| jalanõusid | 286 | 48 | 0 | 2 |
| laste_riided | 274 | 48 | 2 | 2 |
| aksessuaarid | 253 | 42 | 2 | 5 |
| naiste_riided | 274 | 35 | 4 | 2 |

### Oluline andmekvaliteedi tähelepanek

Inventuuris esineb **negatiivseid laoseise**. Need ei ole tavalised tellimissoovitused, vaid võimalikud andmevead või protsessivead. Näiteks võivad need viidata:

- müükidele, mis on laost maha arvestatud enne tegeliku laoseisu korrigeerimist;
- inventuuri ja müügisüsteemi sünkroonimisprobleemile;
- tagastuste või korrigeerimiste puudumisele;
- laoliikumiste hilinenud sisestamisele.

**Järeldus:** negatiivsed laoseisud tuleb enne tellimisotsuseid eraldi kontrollida.

---

## 5. Tähelepanek SQL loogika kohta

Praegune inventuuri `CASE` loogika märgib `quantity_available <= reorder_point` read staatusega `TELLI JUURDE`, kuid `NULL` inventuuriväärtused liiguvad `ELSE 'OK'` alla. See võib olla eksitav, sest inventuurivasteta toode ei tähenda automaatselt, et kõik on korras.

Täpsustatum loogika oleks:

```sql
CASE
    WHEN i.product_id IS NULL THEN 'INVENTUUR PUUDUB'
    WHEN i.quantity_available < 0 THEN 'KONTROLLI LAOSEISU'
    WHEN i.quantity_available <= i.reorder_point THEN 'TELLI JUURDE'
    ELSE 'OK'
END AS staatus
```

See eristab kolm äriliselt erinevat olukorda:

1. inventuuri vaste puudub;
2. laoseis on negatiivne;
3. laoseis on madal ja vajab täiendamist.

---

## Peamised leiud

1. Kataloogis on **12 toodet**, millel puudub müük.
2. Suurima kogumüügiga kategooria on **jalanõusid**.
3. Meeste riided annavad kõige rohkem müügikordi, kuid jalanõud annavad suurema kogumüügi.
4. Inventuuris on **231 toote-asukoha rida**, kus kogus on tellimispunktist väiksem või sellega võrdne.
5. Inventuuris on **10 negatiivse laoseisuga rida**, mis vajavad andmekvaliteedi kontrolli.
6. **12 tootel puudub inventuurivaste**, mistõttu need ei tohiks vaikimisi saada staatust `OK`.

## Suurim üllatus

Suurim üllatus oli see, et inventuuris leidus negatiivseid laoseise. See ei ole ainult varude täiendamise küsimus, vaid viitab võimalikule andmete või protsessi probleemile.

## Soovitus Toomasele

Toomas peaks enne varude täiendamise või sortimendi muutmise otsuseid eraldama kolm juhtumit: müümata tooted, madala laoseisuga tooted ja vigase/puuduva inventuuriandmega tooted. Eriti tuleks kontrollida negatiivseid laoseise ja 12 toodet, millel puudub müügi- või inventuuriseos.

## Puuduvad andmed

Analüüsi täpsustamiseks oleks vaja järgmisi andmeid:

- kas toode on aktiivne, lõpetatud või testtoode;
- millal toode kataloogi lisati;
- ostutellimused ja saabuvad kogused;
- toote omahind ja tegelik marginaal;
- laoliikumiste ajalugu;
- tarnija ja tarneaeg;
- kampaaniate või allahindluste info.

## Failid

- `W3_GT_C_HT_Tooted + Inventuur (LEFT JOIN).sql` — SQL päringud toodete, müügi ja inventuuri analüüsiks.
- `1. LEFT JOIN_ tooted, mida pole kunagi müüdud.png` — müümata toodete päringu tulemus.
- `2. Müümata toodete arv.png` — müümata toodete arvu kontroll.
- `--3.1 Enim müüdud tooted (10).png` — TOP 10 toodete tulemus.
- `4. Müügianalüüs kategooriate kaupa.png` — kategooriate müügianalüüs.
- `5. Inventuuri soovitused.png` — inventuuri staatuse päringu tulemus.
- `inventuuri soovitused.md` — inventuuri detailtabel.

## Kokkuvõte

Toote- ja inventuuriandmed annavad UrbanStyle’ile hea aluse sortimendi ja varude juhtimiseks, kuid enne otsuste tegemist tuleb korrastada andmekvaliteedi probleemid. Müügianalüüs näitab tugevaid kategooriaid, eriti jalanõusid ja meeste riideid, kuid inventuurianalüüs näitab, et osa laoseisudest on negatiivsed või inventuurivasteta. Seetõttu peaks järgmine samm olema andmekvaliteedi kontroll, mitte automaatne tellimisotsus.

