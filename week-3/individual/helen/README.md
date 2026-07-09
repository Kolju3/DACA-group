# Nädal 3: Tooted + inventuur — LEFT JOIN analüüs

## Projekti kontekst

UrbanStyle’i andmestikus analüüsiti toodete, müükide ja inventuuri seoseid. Fookus oli küsimusel, kas tootekataloogis olevad tooted tegelikult müüvad ning kas laoseis toetab ärilisi otsuseid.

Analüüs vastab järgmistele küsimustele:

- Millised tooted on kataloogis, aga ei ole kunagi müüki tekitanud?
- Kui suur on müümata toodete probleem?
- Millised tooted ja kategooriad müüvad kõige paremini?
- Milliste toodete laoseis vajab tähelepanu?
- Kas inventuuriandmetes on andmekvaliteedi või varude planeerimise probleeme?
- Kas lisaks madalale laoseisule esineb ka võimalikku ülevaru?

---

## Kasutatud tabelid

| Tabel | Roll analüüsis |
|---|---|
| `products` | Tootekataloog: tootenimi, kategooria, alamkategooria, jaehind |
| `sales` | Müügitehingud: müügi ID, toote ID, kogus, müügisumma |
| `inventory` | Laoseis: asukoht, saadaolev kogus, tellimispunkt |

## Kasutatud SQL loogika

Analüüsis kasutati järgmisi SQL võtteid:

- `LEFT JOIN` — toodete säilitamiseks ka siis, kui müügi- või inventuurivastet ei ole.
- `INNER JOIN` — ainult tegelikult müüdud toodete leidmiseks.
- `COUNT`, `COUNT(DISTINCT ...)`, `SUM`, `AVG` — mahtude ja müügitulemuste koondamiseks.
- `GROUP BY` — tulemuste koondamiseks toote ja kategooria tasemel.
- `CASE WHEN` — inventuuri staatuse määramiseks.
- `NULLIF` — jagamisel nulliga seotud vea vältimiseks ülevaru kordaja arvutamisel.
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

## 4. Inventuuri täpsustatud staatused

Algne inventuuri päring kasutas lihtsustatud loogikat:

```sql
CASE
    WHEN i.quantity_available <= i.reorder_point THEN 'TELLI JUURDE'
    ELSE 'OK'
END AS staatus
```

See oli kasulik esmane kontroll, kuid ei eristanud piisavalt erinevaid ärilisi olukordi. Täpsustatud loogikas eraldati:

1. negatiivsed laoseisud — võimalik andmekvaliteedi või protsessiviga;
2. puuduv inventuurivaste — `LEFT JOIN` annab inventuuri veergudes `NULL`;
3. tavapärane madal laoseis — tellimispunktist madalam või sellega võrdne kogus;
4. võimalik ülevaru — kogus on vähemalt 3 korda üle tellimispunkti;
5. korras vahemik — ei ole madal, puuduv, negatiivne ega ülevaru kontrolli järgi ekstreemne.

Täpsustatud staatuseloogika:

```sql
CASE
    WHEN i.product_id IS NULL THEN 'INVENTUUR PUUDUB'
    WHEN i.quantity_available < 0 THEN 'KONTROLLI LAOSEISU'
    WHEN i.quantity_available <= i.reorder_point THEN 'TELLI JUURDE'
    WHEN i.reorder_point > 0
         AND i.quantity_available >= i.reorder_point * 3 THEN 'VÕIMALIK ÜLEVARU'
    ELSE 'OK'
END AS staatus
```

**Märkus:** `reorder_point` ei ole maksimaalne lubatud laoseis. See on tellimispunkt ehk piir, millest allapoole minnes peaks varu täiendama. Seetõttu on `VÕIMALIK ÜLEVARU` analüütiline riskimärgis, mitte lõplik tõend ülevaru kohta.

### Inventuuri koondvaade

| Staatus | Ridu | Tõlgendus |
|---|---:|---|
| `VÕIMALIK ÜLEVARU` | 730 | Laoseis on vähemalt 3 korda suurem kui tellimispunkt. Vajab käibe, hooajalisuse ja ostuplaani kontrolli. |
| `OK` | 439 | Laoseis ei ole madal, negatiivne, puuduv ega ülevaru kontrolli järgi ekstreemne. |
| `TELLI JUURDE` | 221 | Laoseis on tellimispunktist madalam või sellega võrdne. |
| `INVENTUUR PUUDUB` | 12 | Tootel puudub inventuurivaste. Seda ei tohi lugeda korras seisuks. |
| `KONTROLLI LAOSEISU` | 10 | Laoseis on negatiivne. Vajab andmekvaliteedi või protsessikontrolli. |
| **Kokku** | **1 412** | Toote-asukoha taseme inventuuriandmed. |

### Inventuuri staatused kategooriate kaupa

| Kategooria | Inventuur puudub | Kontrolli laoseisu | OK | Telli juurde | Võimalik ülevaru | Kokku |
|---|---:|---:|---:|---:|---:|---:|
| meeste_riided | 1 | 2 | 102 | 56 | 164 | 325 |
| jalanõusid | 2 | 0 | 90 | 48 | 146 | 286 |
| laste_riided | 2 | 2 | 77 | 46 | 147 | 274 |
| naiste_riided | 2 | 4 | 86 | 31 | 151 | 274 |
| aksessuaarid | 5 | 2 | 84 | 40 | 122 | 253 |

**Peamine täpsustus:** varude probleem ei ole ühepoolne. Andmetes esineb korraga nii madalat või negatiivset laoseisu kui ka väga suuri laoseise võrreldes tellimispunktiga.

---

## 5. Negatiivsed laoseisud ja puuduv inventuur

Inventuuris esineb **10 negatiivse laoseisuga rida**. Need ei ole tavalised tellimissoovitused, vaid võimalikud andmevead või protsessivead. Näiteks võivad need viidata:

- müükidele, mis on laost maha arvestatud enne tegeliku laoseisu korrigeerimist;
- inventuuri ja müügisüsteemi sünkroonimisprobleemile;
- tagastuste või korrigeerimiste puudumisele;
- laoliikumiste hilinenud sisestamisele.

Lisaks on **12 tootel inventuurivaste puudu**. `LEFT JOIN` puhul tähendab see, et toode on olemas tootetabelis, aga vastavat rida inventuuritabelis ei ole.

**Järeldus:** negatiivsed laoseisud ja inventuurivasteta tooted tuleb enne tellimisotsuseid eraldi kontrollida. Need ei tohiks minna automaatselt `OK` ega tavapärase `TELLI JUURDE` alla.

---

## 6. Võimalik ülevaru

Ülevaru kontrolliks kasutati täiendavat päringut, mis märgib toote-asukoha read, kus `quantity_available >= reorder_point * 3`.

```sql
SELECT
    p.product_name,
    p.category,
    i.location,
    i.quantity_available,
    i.reorder_point,
    i.quantity_available - i.reorder_point AS ule_tellimispunkti,
    ROUND(i.quantity_available::numeric / NULLIF(i.reorder_point, 0), 2) AS kordaja
FROM products p
INNER JOIN inventory i
    ON p.product_id = i.product_id
WHERE i.reorder_point > 0
  AND i.quantity_available >= i.reorder_point * 3
ORDER BY kordaja DESC, ule_tellimispunkti DESC;
```

### Ülevaru kontrolli koond

| Näitaja | Tulemus |
|---|---:|
| Võimaliku ülevaru ridu | 730 |
| Erinevaid tootenimesid | 331 |
| Ridu kordajaga vähemalt 5x | 455 |
| Ridu kordajaga vähemalt 10x | 214 |
| Ridu kordajaga vähemalt 20x | 79 |
| Ridu kordajaga vähemalt 100x | 31 |
| Suurim kordaja | 628.60x |

### Võimaliku ülevaru read kategooriate kaupa

| Kategooria | Võimaliku ülevaru ridu | Erinevaid tootenimesid | Laoseis kokku | Üle tellimispunkti kokku | Suurim kordaja |
|---|---:|---:|---:|---:|---:|
| meeste_riided | 164 | 78 | 93 102 | 89 092 | 527.53 |
| naiste_riided | 151 | 66 | 57 519 | 53 838 | 448.59 |
| laste_riided | 147 | 64 | 68 641 | 64 950 | 237.81 |
| jalanõusid | 146 | 65 | 78 921 | 75 397 | 628.60 |
| aksessuaarid | 122 | 58 | 43 984 | 40 869 | 231.53 |

### TOP 10 kõige suurema ülevaru kordajaga rida

| Koht | Toode | Kategooria | Asukoht | Laoseis | Tellimispunkt | Üle tellimispunkti | Kordaja |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | Minimalistlik sünteetiline saapad | jalanõusid | ladu | 9 429 | 15 | 9 414 | 628.60 |
| 2 | Õhuline sünteetiline rannasandaalid | jalanõusid | tartu | 9 479 | 17 | 9 462 | 557.59 |
| 3 | Trendikas džersii slim-fit püksid | meeste_riided | ladu | 8 968 | 17 | 8 951 | 527.53 |
| 4 | Stiilne džersii püksid | meeste_riided | ladu | 5 321 | 11 | 5 310 | 483.73 |
| 5 | Soe satiinne pluus | naiste_riided | ladu | 7 626 | 17 | 7 609 | 448.59 |
| 6 | Mugav tweed kardigan | meeste_riided | ladu | 7 029 | 16 | 7 013 | 439.31 |
| 7 | Boheemlaslik goretex kingad | jalanõusid | pärnu | 7 588 | 21 | 7 567 | 361.33 |
| 8 | Kerge satiinne jakk | naiste_riided | tartu | 9 985 | 39 | 9 946 | 256.03 |
| 9 | Õhuline sünteetiline kõrge kontsaga kingad | jalanõusid | tallinn | 6 821 | 27 | 6 794 | 252.63 |
| 10 | Luksuslik villane bleiser | laste_riided | pärnu | 7 372 | 31 | 7 341 | 237.81 |

**Järeldus:** ülevaru kontroll on sama oluline kui `TELLI JUURDE` kontroll. Mõnes reas on laoseis tellimispunktist sadu kordi kõrgem. See võib tähendada liigset sisseostu, aeglast käivet, hooajalisuse mõju, laoliikumiste sisestusviga või andmeimpordi probleemi.

---

## Peamised leiud

1. Kataloogis on **12 toodet**, millel puudub müük.
2. Suurima kogumüügiga kategooria on **jalanõusid**.
3. Meeste riided annavad kõige rohkem müügikordi, kuid jalanõud annavad suurema kogumüügi.
4. Inventuuris on **221 toote-asukoha rida**, kus kogus on tellimispunktist väiksem või sellega võrdne.
5. Inventuuris on **10 negatiivse laoseisuga rida**, mis vajavad andmekvaliteedi kontrolli.
6. **12 tootel puudub inventuurivaste**, mistõttu need ei tohiks vaikimisi saada staatust `OK`.
7. Lisaks madalale laoseisule esineb **730 võimalikku ülevaru rida**, kus laoseis on vähemalt 3 korda suurem kui tellimispunkt.
8. Ülevaru kontrollis on **214 rida**, kus laoseis on vähemalt 10 korda suurem kui tellimispunkt, ning **31 rida**, kus kordaja on vähemalt 100.

## Suurim üllatus

Suurim üllatus oli see, et inventuuri probleem on kahesuunaline. Andmetes ei ole ainult puudujäägid ja negatiivsed laoseisud, vaid ka väga suured laoseisud võrreldes tellimispunktiga. See tähendab, et UrbanStyle’i varude juhtimise risk ei ole ainult müügikaotus madala laoseisu tõttu, vaid ka kapitali sidumine võimalikus ülevarus.

## Soovitus Toomasele

Toomas peaks käsitlema inventuuri nelja eraldi töövoona:

1. **Andmekvaliteet:** kontrollida negatiivseid laoseise ja inventuurivasteta tooteid.
2. **Puudujääk:** vaadata üle `TELLI JUURDE` read, eriti tugeva müügiga kategooriates.
3. **Ülevaru:** analüüsida ridu, kus laoseis on vähemalt 3 korda üle tellimispunkti, ning eraldi kontrollida ekstreemseid 10x, 20x ja 100x juhtumeid.
4. **Sortiment:** kontrollida 12 müümata toodet ja otsustada, kas need on aktiivsed, lõpetatud või fantoomtooted.

## Puuduvad andmed

Analüüsi täpsustamiseks oleks vaja järgmisi andmeid:

- kas toode on aktiivne, lõpetatud, hooajaline või testtoode;
- millal toode kataloogi lisati;
- ostutellimused ja juba teel olevad kogused;
- toote omahind ja tegelik marginaal;
- toote müügikiirus ja viimase müügi kuupäev;
- laoliikumiste ajalugu;
- tarnija ja tarneaeg;
- miinimum- ja maksimumvaru poliitika;
- kampaaniate või allahindluste info.

## Failid

- `W3_GT_C_HT_Tooted + Inventuur (LEFT JOIN).sql` — SQL päringud toodete, müügi ja inventuuri analüüsiks. [Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/W3_GT_C_HT_Tooted%20%2B%20Inventuur%20(LEFT%20JOIN).sql)
- `1. LEFT JOIN_ tooted, mida pole kunagi müüdud.png` — müümata toodete päringu tulemus.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/1.%20LEFT%20JOIN_%20tooted%2C%20mida%20pole%20kunagi%20m%C3%BC%C3%BCdud.png)
- `2. Müümata toodete arv.png` — müümata toodete arvu kontroll.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/2.%20M%C3%BC%C3%BCmata%20toodete%20arv.png)
- `3. Enim müüdud tooted (10).png` — TOP 10 toodete tulemus.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/3.%20Enim%20m%C3%BC%C3%BCdud%20tooted%20(10).png)
- `4. Müügianalüüs kategooriate kaupa.png` — kategooriate müügianalüüs.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/4.%20M%C3%BC%C3%BCgianal%C3%BC%C3%BCs%20kategooriate%20kaupa.png)
- `5.1 Inventuuri soovitused.png` — esialgse inventuuripäringu tulemus.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/5.1.%20Inventuuri%20soovitused.png)
- `5.1. Inventuuri soovitused.md` — esialgne inventuuri detailtabel.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/5.1%20Inventuuri%20soovitused.md)
- `5.2 Inventuuri soovitused_täpsustatud.png` — täpsustatud inventuuripäringu tulemus.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/5.%202.Inventuuri%20soovitused_t%C3%A4psustatud.png)
- `5.2. Inventuuri soovitused_täpsustatud.md` — täpsustatud inventuuri staatuste tabel.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/5.2.%20Invetuuri%20soovitused_t%C3%A4psustatud.md)
- `6A. Ülevaru kontroll_laoseis oluliselt üle tellimispunkti.md` — ülevaru kontrolli detailtabel.[Link](https://github.com/Kolju3/DACA-group/blob/main/week-3/individual/helen/kuvat%C3%B5mmised/6A.%20%C3%9Clevaru%20kontroll_laoseis%20oluliselt%20%C3%BCle%20tellimispunkti.md)

## Kokkuvõte

Toote- ja inventuuriandmed annavad UrbanStyle’ile hea aluse sortimendi ja varude juhtimiseks, kuid enne otsuste tegemist tuleb korrastada andmekvaliteedi ja varude planeerimise probleemid. Müügianalüüs näitab tugevaid kategooriaid, eriti jalanõusid ja meeste riideid, kuid inventuurianalüüs näitab, et osa laoseisudest on negatiivsed või inventuurivasteta ning suur osa ridu on võimalikud ülevaru juhtumid. Seetõttu peaks järgmine samm olema varude ja andmekvaliteedi kontroll, mitte automaatne tellimisotsus
