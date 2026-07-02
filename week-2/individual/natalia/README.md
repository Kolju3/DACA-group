# Andmebaasi kvaliteedianalüüs

## 📝 Ülesande kirjeldus
Projekti eesmärk oli kontrollida müügiandmebaasi andmete terviklikkust. Analüüsi käigus tuvastati puuduvad seosed andmetes (orvud ja vaimkirjed) ning võrreldi müügitehingute hindu tootekataloogi hindadega, et tuvastada finantsilisi ebakõlasid.

---

## 🛠️ Teostatud tegevused ja kasutatud funktsioonid
Analüüsiks kasutati SQL-i päringuid. Peamised kasutatud meetodid:

* **`LEFT JOIN` / `RIGHT JOIN`**: Tabelite vaheliste seoste valideerimiseks[cite: 1].
* **`COUNT()`**: Probleemsete kirjete arvu kokkulugemiseks[cite: 1].
* **`IS NULL`**: "Vaimkirjete" (kliendid/tooted, mida pole kasutatud) tuvastamiseks[cite: 1].
* **`AVG()` / `ABS()`**: Müügihinna ja tootehinna erinevuste analüüsimiseks[cite: 2].
* **`HAVING` / `ORDER BY`**: Ebakõlade filtreerimiseks ja järjestamiseks[cite: 2].

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
| **Suurimad hinnaerinevused** | 10 (TOP) | Tooted suurima hinnaerinevusega | [Pilt](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Tooted%20suurima%20hinnaerinevusega.png) |
| **KOKKU** | **1268** | **Koondtulemused** | [Vaata pilti](https://github.com/Kolju3/DACA-group/blob/main/week-2/individual/natalia/Tulemused.png) |

---

## 💡 Järeldus ja ettepanekud

**Milline probleem on Toomase jaoks kõige kriitilisem?**

Toomase jaoks on kõige kriitilisemaks probleemiks **hinna ebakõlad**. Kuna need viitavad otsesele finantskahjule, on see kõige prioriteetsem teema, millega tuleb viivitamatult tegeleda[cite: 2].

### Edasised ettepanekud:

1. **Hinna ebakõlade parandamine:** See on prioriteet nr 1. Tuleb süsteemselt üle kontrollida müügihinna ja tootehinnakirja vastavus, eriti nende toodete puhul, kus erinevus on suurim[cite: 2].
2. **Vaimtoodete analüüs:** Tooted, mida pole kunagi müüdud, tuleb üle vaadata. Kui tegemist on C-kategooria kaubaga, on soovitatav need müügilt maha võtta või suunata sooduskampaaniasse[cite: 2].
3. **Vaimklientide aktiveerimine:** Tuleb analüüsida, miks 592 klienti pole kunagi ostu sooritanud ning käivitada nende aktiveerimiseks suunatud turunduskampaania[cite: 2].
