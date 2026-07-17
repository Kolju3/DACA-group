# Nädal 4 – kalju individuaalne töö

UrbanStyle müügi ja kliendijaotuse dünaamiline analüüs
Autor: Analüütik
Roll: Müügiandmete ja tootekategooriate strateegiline analüüs
Töökeskkond: SQL / PostgreSQL

📋 Ülesanne
UrbanStyle.ltd soovis põhjalikumat vaadet oma müügitrendidele aastatel 2023–2026. Minu ülesandeks oli luua dünaamiline analüüsikeskkond, mis võimaldaks:

✅ Võrrelda müügitulemusi erinevate asukohtade vahel (Tallinn, Tartu, Pärnu, Online)

✅ Analüüsida tootekategooriate osakaalu ja käivet (meeste-, naiste-, lasterõivad, jalanõud, aksessuaarid)

✅ Tuvastada müügi sesoonsust ja kasvutrende erineva ajasammuga (päev, nädal, kuu)

✅ Luua dünaamiline koodibaas, kus sisendväärtuste muutmine võimaldab kohest andmete võrdlust ilma koodi ümber kirjutamata

🛠️ Kasutatud SQL-võtted
Võte	Kirjeldus
WITH (CTE-d)	Kasutasin CTE-sid koodi loetavuse parandamiseks ja keerukate andmetöötlusetappide liigendamiseks
SUM()	Peamine funktsioon kogumüükide ja tehingute arvu kokkuarvutamiseks
HAVING	Filtreerimine ja sorteerimine grupeeritud andmete tasandil
Dünaamilised parameetrid	Kood võimaldab muuta perioode ja andmete täpsusastet (päev, nädal, kuu)
Erinevad skriptid	Töö jaotati kaheks põhikoodiks – üks keskendus asukohtadele ja teine tootekategooriatele
ℹ️ Märkus: Analüüsis ei kasutatud AVG ega LAG funktsioone, kuna perioodid olid koodis täpselt defineeritud ja võrdlused ehitati üles teisel meetodil.

📊 Peamised tulemused
Näitaja	Tulemus (2023–2024)
Üldine kasv	Umbes 50% kasvuperioodil 2023–2024
Kiireima kasvuga kanalid	Online ja Tartu
Suurima käibega grupid	Meeste rõivad, naiste rõivad ja jalanõud
Sesoonsus	Suvekuudel (juuni–august) on müük u 20% kõrgem
2025. aasta trend	Müük on võrreldes eelnevate aastatega drastiliselt kukkunud
📌 Lisatähelepanekud
Kõik viis tootekategooriat järgivad sarnast sesoonset mustrit: suvel on müügi tipp ning kevadel ja sügisel madalpunkt.

Aastalõpu kampaaniad on olnud edukad, tuues kaasa ühekuulise müügikasvu aasta lõpus.

Alates 2025. aastast on märgatav tugev müügi langus.

💡 Soovitused
Keskenduda kasvukanalitele
Suurendada investeeringuid Online-poodi ja Tartu esindusse, mis on näidanud kiireimat kasvu.

Varude planeerimine
Arvestada suvise 20%-lise müügitõusuga ja planeerida laovarusid vastavalt.

Kriisianalüüs
Uurida süvitsi 2025. aasta müügi kokkukukkumise põhjuseid.

Tootevaliku optimeerimine
Kuna aksessuaarid ja lasterõivad on väiksema käibega, kaaluda nende kategooriate turunduse või valiku korrigeerimist.

📁 Failid
📄 Andmefailid:
2023_Monthly_sales_analyze.csv
2024_Monthly_sales_analyze.csv jne

📈 Visualiseeringud:
Logaritmilisel skaalal müügigraafikud asukohtade ja kategooriate kaupa

📝 Järeldused:
Järeldused.md

🧠 Õpikogemus
Selle projekti keskne õppetund oli dünaamilise SQL-koodi loomise väärtus. Võime muuta analüüsi täpsusastet (päevast kuuni) ühe parameetri muutmisega andis märgatava eelise suurte andmemahtude kiireks töötlemiseks ja trendide leidmiseks ilma koodi korduva muutmiseta.

Samuti näitas analüüs, et keerulisi ajalisi võrdlusi saab edukalt teostada ka ilma LAG funktsioonita, kui perioodid on korrektselt defineeritud.
