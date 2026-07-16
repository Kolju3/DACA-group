# Nädal 4 – SQL agregatsioon: turunduskanalite efektiivsus

**Autor:** Helen Tanner  
**Roll:** D – turunduskampaaniate efektiivsus  
**Keskkond:** Supabase / PostgreSQL  
**Põhitabelid:** `sales`, `customers`, `web_logs`

## Ülesanne

Analüüsi eesmärk oli koondada UrbanStyle’i turunduskanalite tulemused CEO Kristi Tamme juhatuse koosoleku jaoks. Kanalite kaupa arvutati klientide ja tellimuste arv, kogukäive, keskmine tellimusväärtus ning müük kliendi kohta. Lisaks analüüsiti kuiseid trende.

Töös rakendati Nädal 4 õpiväljundeid: `GROUP BY`, agregaatfunktsioonid, `HAVING`, CTE-d ning window function’e.

## Mida tegin

- importisin ja kontrollisin 50 000 reaga `web_logs` tabeli;
- koostasin juhendi kolm põhipäringut;
- kontrollisin kolme tabeli ühendamise mõju müüginumbritele;
- tuvastasin, et otsene ühendamine `customer_id` alusel kordistas müügiridu;
- koostasin valideeritud alternatiivi, mis määrab kliendile ühe viimase teadaoleva turunduskanali;
- valmistasin juhtkonna esitluse jaoks koondnumbrid ja piirangud.

## Peamised leiud

- Valideeritud tulemuses oli suurima kogukäibega kanal **`google_organic`**: **582 912,57 €**, **1 994 tellimust** ja **624 klienti**.
- Kanali keskmine tellimusväärtus oli **292,33 €**.
- `google_organic` käive kasvas 2024. aasta novembrist detsembrini **13 834,38 eurolt 33 572,86 euroni**, ehk **142,7%**.
- Turunduskanalite nimetused ei ole standardiseeritud: sama kanal esineb mitme kirjapildiga.
- Tegelikku ROI-d ei saa arvutada, sest andmestikus puuduvad kampaaniate kulud.

## Failid

| Fail | Kirjeldus |
|---|---|
| [SQL-päringud](./W4_GT_D_HT_Turunduskampaaniate%20efektiivsus.sql) | Juhendi põhipäringud, kontrollid ja valideeritud lisapäringud |
| [Kuvatõmmised ja CSV-tulemused](./kuvat%C3%B5mmised/) | Supabase’i päringutulemused ja kontrollmaterjal |
| [Detailne analüüs](./W4_GT_D_HT_DETAILNE_ANALUUS.md) | Meetod, kvaliteedikontroll, tulemused ja piirangud |
| [Presentatsiooni kokkuvõte](./W4_GT_D_HT_PRESENTATSIOONI_KOKKUVOTE.md) | Roll C-le üleantav juhtkonna esitluse alus |
| [Grupi ühine töö](../../group/) | Meeskonna koondtöö ja ühine README |

## Oluline metoodiline piirang

`web_logs` sisaldab ühe kliendi kohta mitut külastust. Seetõttu kordistas otsene `sales`–`customers`–`web_logs` ühendamine samu müüke. Lõplikud juhtimisnumbrid põhinevad kontrollitud päringul, kus igale kliendile määrati tema viimane teadaolev kanal.

See on lihtsustatud kliendipõhine omistamisreegel, mitte tehingupõhine turunduse attribution-mudel.

