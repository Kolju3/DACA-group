# Nädal 4 – Roll D presentatsiooni kokkuvõte

## Teema

**Turunduskanalite efektiivsus**

Eesmärk oli selgitada, millised kanalid toovad UrbanStyle’ile kõige rohkem kliente, tellimusi ja käivet ning kuidas tulemused kuude lõikes muutuvad.

## Slaidile soovitatav põhisõnum

> `google_organic` oli valideeritud tulemuses suurima käibega kanal: 582 912,57 eurot ja 1 994 tellimust. Detsembris 2024 kasvas selle kanali käive võrreldes novembriga 142,7%. Tegelikku ROI-d ei saa veel arvutada, sest kampaaniakulud puuduvad.

## 3–5 numbrilist leidu

1. **Suurima kogukäibega kanal**  
   `google_organic`: **582 912,57 €**, **1 994 tellimust**, **624 klienti**.

2. **Keskmine tellimusväärtus**  
   `google_organic` AOV oli **292,33 €**.

3. **Olulisim kuine muutus**  
   Käive kasvas 2024. aasta novembri **13 834,38 eurolt** detsembri **33 572,86 euroni**.

4. **Kasvuprotsent**  
   Novembrist detsembrini oli kasv **19 738,48 € ehk 142,7%**.

5. **Andmekvaliteet**  
   `web_logs` sisaldas **50 000 rida**, millest **18,83%** olid anonüümsed; `source` väljal oli **19 erinevat väärtust**.

## Mida suuliselt öelda

„Minu ülesanne oli hinnata turunduskanalite efektiivsust, ühendades müügi-, kliendi- ja veebilogide andmed. Esmane päring töötas tehniliselt, kuid kontroll näitas, et ühe kliendi mitmed veebilogid kordistasid samu müüke. Seetõttu kasutasin lõplikes numbrites kontrollitud lahendust, kus igale kliendile määrati üks viimane teadaolev kanal.

Valideeritud tulemuses oli suurima käibega kanal `google_organic`, mis tõi ligi 583 tuhat eurot ja 1 994 tellimust. Eriti tugev oli 2024. aasta detsember, mil käive kasvas novembriga võrreldes 142,7%.

Tulemust tuleb käsitleda kanali efektiivsuse, mitte tegeliku ROI-na. ROI arvutamiseks vajame juurde kampaaniakulusid ning enne lõplikku kanalite võrdlust tuleb ühtlustada erinevad source-kirjapildid.”

## Juhtkonnale antav soovitus

- toetada `google_organic` kanalit SEO ja sisuturundusega;
- analüüsida detsembri kasvu põhjuseid kampaania- ja hooajalisuse andmetega;
- standardiseerida turunduskanalite nimetused;
- lisada kampaaniakulud, et järgmises etapis arvutada tegelik ROI;
- arendada tehingupõhist attribution-mudelit.

## Oluline piirang esitluses

Ära ütle:

> „Google Organic oli kõige parema ROI-ga kanal.”

Ütle:

> „`google_organic` oli suurima valideeritud käibe ja tellimuste arvuga kanal.”

Põhjus: kampaaniakulud puuduvad ja seetõttu ei ole ROI-d arvutatud.

## Võimalikud küsimused ja vastused

### Miks ei kasutatud juhendi algse JOIN-i tulemusi?

Ühel kliendil oli mitu veebilogirida. Otsene ühendamine kordistas samu müüke ning suurendas käibe kunstlikult ligikaudu 2,9 miljonilt eurolt 34,5 miljonile eurole.

### Kuidas tulemus parandati?

Iga kliendi logid järjestati kuupäeva järgi ja kliendile jäeti üks viimane teadaolev kanal. Seejärel ühendati kanal müükidega ja tehti agregatsioon.

### Kas viimane kanal põhjustas kindlasti ostu?

Ei. See on lihtsustatud kliendipõhine omistamisreegel. Täpsemaks analüüsiks tuleb siduda külastus ja ost ajaliselt ning kasutada kampaania ID-d.

### Miks esineb mitu Google’i või Facebooki kanalit?

`source` väärtused ei ole standardiseeritud. Sama kanal on sisestatud erineva kirjapildi ja nimetusega.

## Slaidile sobiv visuaal

Üks selge horisontaalne tulpdiagramm:

- mõõdik: valideeritud kogukäive;
- kanalid: kaheksa suurimat standardset kanalit;
- tõsta esile `google_organic`;
- ära kuva eraldi kõiki kirjapildivariante põhigraafikul;
- lisa jalusesse märkus: „ROI arvutamiseks puuduvad kampaaniakulud.”

## Seotud materjalid

- [SQL-päringud](./W4_GT_D_HT_Turunduskampaaniate%20efektiivsus.sql)
- [Kuvatõmmised ja CSV-tulemused](./kuvat%C3%B5mmised/)
- [Detailne analüüs](./W4_GT_D_HT_DETAILNE_ANALUUS.md)
- [Grupi ühine töö](../../group/)
