# Nädal 1: SQL Põhitõed — Müügiandmete Kvaliteedikontroll

## Kontekst
IT-juht Toomas Kask kahtlustab, et UrbanStyle.ltd müügiandmetes 
esineb kvaliteediprobleeme. Enne ärianalüüsi kasutamist tuli 
kontrollida andmestiku usaldusväärsust.

## Roll grupitöös
**Roll A: Müügiandmete uurija** — meeskond Operations Intelligence

Uurisin `sales` tabelit müügitehingute mahu, struktuuri ja 
andmekvaliteedi vaatenurgast.

## Kasutatud tööriistad
- **SQL / PostgreSQL** — andmepäringud
- **Supabase** — andmebaas pilves
- **VS Code** — päringute kirjutamine ja salvestamine
- **GitHub** — koodi versioonihaldus ja portfoolio

## Tehtud analüüs
Kirjutasin 8 SQL päringut, mis kontrollisid:

1. **Tabeli maht** — mitu tehingut on andmestikus
2. **Tabeli struktuur** — millised veerud ja andmed on olemas
3. **Suurimad tehingud** — kogu andmestik (ebarealistlike väärtuste kontroll)
4. **Suurimad tehingud** — Tallinna kauplus eraldi
5. **Väikseimad tehingud** — negatiivsete ja NULL-summade kontroll
6. **Puuduvad kliendiandmed** — mitu tehingut on ilma `customer_id`-ta
7. **Tuleviku kuupäevad** — kas esineb andmesisestuse vigu
8. **Koondülevaade** — kõik kvaliteedinäitajad ühes päringus
   *(kasutasin `CASE WHEN` konstruktsiooni, mida uurisin 
   iseseisvalt väljaspool kohustuslikku materjali)*

## Peamised leiud

| Näitaja | Tulemus |
|---------|---------|
| Tehinguid kokku | 15 234 |
| Puuduvad `customer_id` väärtused | 1 487 (~9,8%) |
| Negatiivsed summad | 305 tehingut (~2,0%) |
| Negatiivsete tehingute koguväärtus | -88 632,61 EUR |
| Tuleviku kuupäevaga tehingud | 2 |
| NULL- või 0-summaga tehingud | 0 |
| Suurim tehing | 2 170,40 EUR |

## Järeldused
Andmestik on valdavalt kasutuskõlblik — suuri struktuurseid 
probleeme ei tuvastatud.

Enne ärianalüüsi kasutamist soovitan:
- selgitada **negatiivsete tehingute** olemus 
  (tagastused, kreeditarved või andmevead?)
- kontrollida **2 tuleviku kuupäevaga** tehingu põhjuseid
- hinnata **puuduva `customer_id`** mõju kliendianalüüsile

Suurim risk ärianalüüsi kvaliteedile on negatiivsete tehingute 
koguväärtus **-88 632,61 EUR**, mille olemus vajab selgitamist.

## Failid
- `week1_sales_exploration.sql` — kõik SQL päringud koos 
  kommentaaride ja tulemustega

## Järgmised sammud
Nädal 2-s õpime andmete puhastamist — seal saame 
negatiivsete tehingute ja puuduvate kliendiandmetega 
edasi tegeleda.
