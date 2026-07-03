# Nädal 2: SQL Puhastamine — Tooteandmete Kvaliteedikontroll

## Projektikontekst
UrbanStyle.ltd müügiandmete usaldusväärse analüüsi eelduseks 
on puhtad tooteandmed. IT-direktor Toomas Kask on hoiatanud, 
et praeguseid andmeid ei saa usaldada enne põhjalikku kontrolli.

Minu ülesanne oli auditeerida `products` tabelit, tuvastada 
andmekvaliteedi probleemid ja koostada puhastamisplaan, 
järgides ranget metoodikat: **Test → Verify → Log → Commit**.

## Minu roll: Tooteandmete puhastaja (Roll C)
**Meeskond:** Operations Intelligence

Tegutsesin "detektiivina" — tuvastasin vigade ulatuse ilma 
production-andmeid muutmata. Kõik kontrollid toimusid 
eraldi testkoopiaks loodud `products_test` tabelis.

## Kasutatud tööriistad
- **SQL / PostgreSQL** — andmepäringud ja kvaliteedikontroll
- **Supabase** — andmebaas pilves
- **VS Code** — päringute kirjutamine ja salvestamine
- **GitHub** — koodi versioonihaldus ja portfoolio

## Kasutatud SQL tehnikad
- `CREATE TABLE AS` — turvalise testkeskkonna loomiseks
- `UNION ALL` — tabelite ridade arvu võrdlemiseks
- `GROUP BY` & `HAVING` — duplikaatide leidmiseks
- `FILTER (WHERE ...)` — tingimuspõhine NULL-loendamine
- `TRIM()` — tühikute eemaldamine tekstiväljadest
- `information_schema.columns` — tabelistruktuuri kontrolliks
- `COUNT`, `MIN`, `MAX` — statistiliseks ülevaateks

## Tehtud analüüs

1. **Test-koopia loomine** — `products_test` tabel 
   algandmete kaitsmiseks, kontrollisin et ridade arv 
   ühtib originaaliga (362 rida mõlemas)
2. **Tabelistruktuuri kontroll** — 9 veergu tuvastatud: 
   `product_id`, `product_name`, `category`, `subcategory`, 
   `supplier`, `cost_price`, `retail_price`, `eco_certified`, 
   `created_at`
3. **Duplikaatsete toodete tuvastamine** — korduvad 
   tootenimed `product_name` välja alusel
4. **NULL-väärtuste kontrollimine** — kriitilised väljad: 
   nimi, kategooria, omahind, jaehind
5. **Loogilised hinnavead** — negatiivsed ja äärmuslikud 
   hinnad, omahind vs jaehind võrdlus
6. **Kategooriate järjekindlus** — `category` ja 
   `subcategory` kirjaviiside kontroll
7. **Puhastamisraport** — kõik leiud koondatud 
   prioriteedi järgi

## Peamised leiud

| Näitaja | Leitud probleemid | Prioriteet | Äriline mõju |
|---------|-------------------|------------|--------------|
| Omahind > jaehind | 10 toodet | **Kriitiline** | Negatiivne brutomarginaal — tooted müüakse kahjumiga |
| Duplikaatsed tootenimed | 12 tootenime (igaüks 2 korda) | **Kõrge** | Moonutab tooteportfelli analüüsi |
| NULL kriitilised väljad | 0 | Puudub | Kõik kirjed on korras |
| Negatiivsed / äärmuslikud hinnad | 0 | Puudub | Kõik kirjed on korras |
| Kategooriate ebakõlad | 0 | Puudub | Kõik 5 kategooriat on järjekindlad |

**Tabelis kokku:** 362 toodet  
**Probleemse kirjeid:** 22 (~6,1% kõigist toodetest)

## Detailsemad leiud

**Omahind > jaehind (10 toodet):**
- 10 toote puhul on `cost_price` suurem kui `retail_price`
- See tähendab negatiivset brutomarginaali — tooted 
  müüakse odavamalt kui need maksavad
- Võimalikud põhjused: andmesisestuse viga, vale omahind, 
  kampaaniahind või teadlik kahjumlik müük
- See on kriitilisim leid, kuna mõjutab otseselt 
  kasumlikkuse ja marginaali analüüsi

**Duplikaatsed tootenimed (12 nime):**
- 12 tootenime esineb täpselt 2 korda
- Enne kustutamist tuleb kontrollida, kas kõik tunnused 
  (`product_id`, `category`, `cost_price`, `retail_price`) 
  kattuvad — kui jah, on tegemist duplikaadiga; 
  kui ei, võib olla tegemist tootevariandiga

**Positiivsed leiud:**
- Kõigil toodetel on nimi, kategooria, omahind ja jaehind
- Kategooriate register on puhas — 5 unikaalset kategooriat 
  (`aksessuaarid`, `jalanõud`, `laste_riided`, 
  `meeste_riided`, `naiste_riided`) ilma kirjaviiside 
  erinevusteta
- Alamkategooriate (`subcategory`) register on samuti puhas

## Olulisemad õppetunnid
- **Loogilised vead on ohtlikumad kui NULL-id** — 
  puuduv väärtus on nähtav, aga vale väärtus 
  (nt omahind > jaehind) võib jääda kaua märkamatuks
- **Test enne muutmist** — `CREATE TABLE AS` on 
  lihtne viis algandmete kaitsmiseks
- **Tabelistruktuuri kontroll on esimene samm** — 
  `information_schema.columns` annab kiire ülevaate 
  kõigist väljadest enne analüüsi alustamist
- **Duplikaat ei pruugi olla duplikaat** — sama nimi 
  võib tähistada erinevat tootevarianti

## Soovitatav puhastamise järjekord
1. **Omahind > jaehind** — kontrollida 10 toodet äriliselt  
   → kas andmeviga, kampaaniahind või kahjumlik müük?
2. **Duplikaatide kontroll** — võrrelda kõiki tunnuseid  
   → `product_id`, `category`, `supplier`, `cost_price`, 
   `retail_price` peavad kattuma, et kustutada
3. **Tulevikuks** — lisada sisestuskontrollid:  
   → hind ei tohi olla negatiivne, omahind ei tohi 
   ületada jaehinda, duplikaatide hoiatus

## Failid
- `week2_products_cleaning.sql` — kõik SQL päringud 
  koos kommentaaride, leidude ja järeldustega

## Järgmised sammud
Nädal 3-s õpime SQL JOIN-e — saame ühendada `products`, 
`customers` ja `sales` tabelid ning hakata vastama 
keerukamatele äriküsimustele, näiteks millised tooted 
on tegelikult kasumlikud.

---
*See projekt on osa DACA (Data Analyst Career Accelerator) 
programmist. Ettevõte UrbanStyle.ltd on fiktsioonalne, 
loodud õppeeesmärkidel.*
