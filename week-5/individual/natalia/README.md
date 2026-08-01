# 📦 ROLL C: Operations Dashboard (Liis'i vaade — Inventuur ja Tarneahea)

> **Ülesande eesmärk:** Loo operatiivne töölaua vaade Liis'ile, mis annab 30 sekundiga ülevaate laoseisude tervisest, müügi jaotusest ja hoiatab kriitiliste üle- või puudujääkide eest.

---

## 📋 Ülesande Kaardi Ülevaade

* **Roll:** Operations Manager (Liis)
* **Sisendandmed:** `inventory`, `products`, `sales` (`Supabase`)
* **Tööriist:** Power BI
* **Väljund:** 3 KPI-kaarti, 2 interaktiivset diagrammi ja äritõlgendus

---

📊 Dashboardi Arhitektuur ja Disainipõhimõtted
1. KPI Peamõõdikud (Ülemine riba)
Kogus laos kokku: 377K ühikut (Sum of quantity_available)

Lao ostuväärtus: 44.24M € (seotud kapital)

Lao müügiväärtus: 67.54M € (potentsiaalne käive)

2. Visuaalid
Müük linnade lõikes (Sõõrikdiagramm): Näitab selgelt müügikäibe proportsioone (Tallinn 37.5%, Online 34.61%, Tartu 17.93%, Pärnu 9.93%). Max 5 osa tagab ülikiire loetavuse.

Kogus laos kategooria ja asukoha kaupa (Virnastatud tulpdiagramm): Kategooriad on sorteeritud kahanevalt (meeste riided 101.2K, jalanõud 86.3K, laste riided 75.2K, naiste riided 64.0K, aksessuaarid 50.1K). Virnastus näitab selgelt, kui suur osa kaubast seisab pealaos (ladu).

3. Interaktiivsus
Lõigutid (Slicers): Asukoha (Vali asukoht) ja kategooria (Vali kategooria) rippmenüüd võimaldavad Liis'il filtreerida laoseise spetsiifiliste kaupluste või tooterühmade lõikes.

💡 Äritõlgendus ja "Punased Lipud" Liis'ile
Peamine järeldus: Aastase 2,9 miljoni eurose käibe juures seisab laos kinni lausa 44,24 miljoni euro väärtuses kapitali (müügiväärtusega 67,54 mln €). Kuna üle 72% läbimüügist tuleb Tallinnast ja Online-kanalist, viitab selline kaubavaru maht märkimisväärsele ülevarule pealaos ning vajadusele varusid kiirelt optimeerida.

🚩 Operatiivsed soovitused (Action Plan):
Pealao varude kohene optimeerimine: Pealaos (ladu) seisab kriitiliselt suur hulk meeste riideid ja jalanõusid, mis tuleb suunata kiiremini müügikanalitesse.

Logistiline ümberjaotamine: Kuna Tallinn ja Online toovad 72% müügist, tuleks pealaost kaup suunata otse nõudlusega poodidesse, mitte hoida seda seisvana laos.

✅ Kvaliteedikontroll
[x] Diagrammid vastavad Liis'i operatsioonivajadusele

[x] Kauplused ja kategooriad on selgelt eristatavad

[x] Liis saab aru, kus on "punased lipud" (kriitiline ülevaru pealaos)

--

## 🛠️ Teostus ja DAX Mõõdikud:
* **Müügikoht (Asukoha andmete puhastamine Online-kanali jaoks)

*Müügikoht = 
IF(
    ISBLANK('public sales'[store_location]) || 'public sales'[store_location] = "", 
    "Online", 
    'public sales'[store_location]
)

* **Lao Ostuväärtus (KPI)

*Lao Ostuväärtus = 
SUMX(
    'public products',
    'public products'[cost_price] * CALCULATE(SUM('public inventory'[quantity_available]))
)

* **Lao Müügiväärtus (KPI)
* Lao Müügiväärtus = 
SUMX(
    'public inventory', 
    'public inventory'[quantity_available] * RELATED('public products'[retail_price])

)
