# Presentatsiooni kokkuvõte — Natalia, Roll A: Müük + kliendid

## Ühe lausega kokkuvõte

Natalia analüüs näitas, et `INNER JOIN` seob müügi- ja kliendiandmed äriliselt kasulikuks kliendivaateks, kuid tõi samal ajal välja olulise andmekvaliteedi probleemi: **988 müügirida ei leia klienditabelist vastet**.

---

## Mida analüüsis tehti?

Analüüsi fookus oli ühendada `sales` ja `customers` tabelid `INNER JOIN` abil. Selle põhjal vaadati:

- millised kliendid on ostnud;
- kes on TOP 10 kliendid kogumüügi järgi;
- millistest linnadest tuleb suurim müük;
- kuidas müük jaguneb lojaalsustasemete vahel;
- kui palju müügiridu jääb klienditabeliga ühendamata;
- millised kliendid on üle keskmise kogumüügiga.

---

## Peamised arvud

| Näitaja | Tulemus |
|---|---:|
| Müügiridu `sales` tabelis | 10118 |
| `INNER JOIN` tulemusse jõudnud müügiridu | 9130 |
| JOINist välja jäänud müügiridu | 988 |
| Suurima kogumüügiga klient | Tiina Pärn |
| Tiina Pärna kogumüük | 27668.02 |
| Suurim müügilinn | Tallinn |
| Tallinna kogumüük | 1006252.88 |
| Suurim lojaalsusgrupp kogumüügi järgi | NULL |
| `NULL` lojaalsustasemega klientide kogumüük | 1071805.32 |
| Üle keskmise kogumüügiga kliente | 900 |

---

## Peamised leiud

### 1. Tallinn on suurim müügipiirkond

Tallinnas oli **1007 klienti**, **3601 ostu** ja kogumüük **1006252.88**. See kinnitab, et Tallinn on UrbanStyle'i suurim müügipiirkond.

### 2. Tartu ja Pärnu on samuti olulised

Tartu kogumüük oli **523286.64** ja Pärnu kogumüük **374005.86**. TOP 10 klientide seas on samuti mitu Tartu ja Pärnu klienti, mistõttu ei tohiks klienditurundust keskendada ainult Tallinnale.

### 3. Lojaalsustasemete andmed vajavad kontrolli

Kõige suurem kogumüük tuli klientidelt, kelle `loyalty_tier` oli **NULL**. See on äriliselt oluline, sest osa väärtuslikest klientidest ei ole lojaalsusprogrammis korrektselt liigitatud.

### 4. Kõiki müüke ei saa hetkel kliendianalüüsi kaasata

`INNER JOIN` tulemusse jõudis **9130** müügirida, kuid `sales` tabelis oli kokku **10118** rida. Seega jäi kliendianalüüsist välja **988** müügirida.

---

## Suurim üllatus

Suurim üllatus oli see, et lojaalsustaseme järgi andis suurima kogumüügi just `NULL` grupp. See tähendab, et oluline osa kliendiväärtusest võib olla lojaalsusprogrammi vaates nähtamatu või valesti liigitatud.

---

## Soovitus Annale

Enne kampaaniate ja lojaalsusprogrammi otsuste tegemist tuleks täiendada `loyalty_tier` andmeid. Praegu ei saa lojaalsustasemete põhjal teha täiesti usaldusväärseid järeldusi, sest suurima müügiga grupp on määramata lojaalsustasemega.

---

## Soovitus Toomasele

Toomas peaks laskma kontrollida, miks **988 müügirida** ei leia vastet `customers` tabelist. See võib viidata puuduvale või vigasele `customer_id` väärtusele või kliendikirjete puudumisele. Probleem mõjutab otseselt kliendipõhise aruandluse usaldusväärsust.

---

## Puuduvad andmed / piirangud

- Ei ole teada, kas JOINist välja jäänud 988 rida on seotud puuduva `customer_id`, vale `customer_id` või puuduva kliendikirjega.
- Ei ole teada, miks 1024 ostuga kliendil on `loyalty_tier` väärtus `NULL`.
- `INNER JOIN` näitab ainult neid müüke, millel on klienditabelis vaste; kogu müügi analüüsiks tuleb kasutada lisaks `LEFT JOIN` või eraldi andmekvaliteedi kontrolle.

---

## Esitluse lühitekst

Minu roll oli ühendada müügi- ja kliendiandmed `INNER JOIN` abil. Analüüs näitas, et suurim müügipiirkond on Tallinn, kuid TOP-klientide seas on olulisel kohal ka Tartu ja Pärnu kliendid. Kõrgeima kogumüügiga klient oli Tiina Pärn Tartust.

Kõige olulisem leid ei olnud aga ainult müügitulemus, vaid andmekvaliteet. `sales` tabelis oli 10118 müügirida, kuid `INNER JOIN` jõudis seostada neist 9130. See tähendab, et 988 müügirida jäi kliendianalüüsist välja. Lisaks tuli suurim kogumüük lojaalsustasemete lõikes klientidelt, kelle lojaalsustase oli `NULL`.

Soovitan enne kliendikampaaniate ja lojaalsusotsuste tegemist parandada kliendiandmete kvaliteeti: kontrollida `customer_id` vastavusi ja täiendada lojaalsustaseme infot. Vastasel juhul võivad olulised kliendid jääda analüüsis valesse gruppi või üldse välja.

