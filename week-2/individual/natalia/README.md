# Andmebaasi kvaliteedianalüüs

## 📝 Ülesande kirjeldus
Projekti eesmärk oli kontrollida müügiandmebaasi andmete terviklikkust. Analüüsi käigus tuvastati puuduvad seosed andmetes (orvud ja vaimkirjed) ning võrreldi müügitehingute hindu tootekataloogi hindadega, et tuvastada finantsilisi ebakõlasid.

---

## 🛠️ Teostatud tegevused ja kasutatud funktsioonid
Analüüsiks kasutati SQL-i päringuid. Peamised kasutatud meetodid:

* **`LEFT JOIN` / `RIGHT JOIN`**: Tabelite vaheliste seoste valideerimiseks.
* **`COUNT()`**: Probleemsete kirjete arvu kokkulugemiseks.
* **`IS NULL`**: "Vaimkirjete" (kliendid/tooted, mida pole kasutatud) tuvastamiseks.
* **Võrdlusoperaatorid (`<>`)**: Müügihinna ja tootehinna vastavuse kontrollimiseks.

---

## 💾 SQL päringud
Kõik analüüsiks kasutatud SQL päringud on leitavad siit:
👉 [**Vaata analüüsi SQL faili (GitHub)**](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/WEEK%202_GT_SQL%20puhastamine.sql)

---

## 📊 Analüüsi tulemused

| Kategooria | Leitud probleeme | Kirjeldus |
| :--- | :---: | :--- |
| **Orbid kliendid** | 0 | Müük viitab olematule kliendile |
| **Orbid tooted** | 0 | Müük viitab olematule tootele |
| **Vaimkliendid** | 592 | Klient ei ole kunagi ostnud |
| **Vaimtooted** | 12 | Toodet pole kunagi müüdud |
| **Hinna ebakõlad** | 664 | Müügihind ei klapi tootehinnaga |
| **KOKKU** | **1268** | |

---

## 💡 Järeldus ja kriitiline analüüs

**Milline probleem on Toomase jaoks kõige kriitilisem?**

Toomase jaoks on kõige kriitilisemaks probleemiks **hinna ebakõlad**. Kuna need viitavad otsesele finantskahjule (müük toimub vale hinnaga võrreldes tootekataloogiga), on see kõige prioriteetsem teema, millega tuleb viivitamatult tegeleda, et vältida ettevõtte edasist raha kaotust.
