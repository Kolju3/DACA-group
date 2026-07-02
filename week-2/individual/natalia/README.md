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

| Kategooria | Leitud probleeme | Kirjeldus | Tõendusmaterjal (Pildid) |
| :--- | :---: | :--- | :--- |
| **Orbid kliendid** | 0 | Müük viitab olematule kliendile | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Orbid%20mu%CC%88u%CC%88gid.png) |
| **Orbid tooted** | 0 | Müük viitab olematule tootele | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Orbid%20product.png) |
| **Vaimkliendid** | 592 | Klient ei ole kunagi ostnud | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Kliendid%20kes%20pole%20kunagi%20ostud.png) |
| **Vaimtooted** | 12 | Toodet pole kunagi müüdud | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Tooted%20mida%20ei%20ole%20mu%CC%88u%CC%88dud.png) |
| **Hinna ebakõlad** | 664 | Müügihind ei klapi tootehinnaga | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Mu%CC%88u%CC%88gihinna%20vs%20tootehina%20erinevus.png) |
| **KOKKU** | **1268** | - | [Kõik tulemused](https://github.com/Kolju3/DACA-group/tree/main/week-2/individual/natalia) |

---

## 💡 Järeldus ja kriitiline analüüs

**Milline probleem on Toomase jaoks kõige kriitilisem?**

Toomase jaoks on kõige kriitilisemaks probleemiks **hinna ebakõlad**. Kuna need viitavad otsesele finantskahjule (müük toimub vale hinnaga võrreldes tootekataloogiga), on see kõige prioriteetsem teema, millega tuleb viivitamatult tegeleda, et vältida ettevõtte edasist raha kaotust.
