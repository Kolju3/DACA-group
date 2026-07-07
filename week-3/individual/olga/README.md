# Nädal 3 – olga individuaalne töö

## Ülesanne
LEFT JOIN: millised kliendid pole kunagi midagi ostnud? Koosta Anna jaoks "kadunud klientide" nimekiri koos soovitustega.

## Mida tegin
Roll B: "Kadunud klientide" tuvastamine

## SQL päringud / failid

https://supabase.com/dashboard/project/jrkmbzgrdxffhdmbtvey/sql/a2166533-504f-40e4-89e0-a2f4405aaf8f

SELECT        c.first_name,        c.last_name,        c.email,        c.city,        c.registration_date,        s.sale_id    
 FROM customers c    LEFT JOIN sales s ON c.customer_id = s.customer_id    
 WHERE s.sale_id IS NULL;

 SELECT COUNT(*) AS kadunud_kliente    
 FROM customers c    LEFT JOIN sales s ON c.customer_id = s.customer_id    
 WHERE s.sale_id IS NULL;

 SELECT        c.city,        COUNT(*) AS kadunud_kliente    
 FROM customers c    LEFT JOIN sales s ON c.customer_id = s.customer_id   
 WHERE s.sale_id IS NULL    
 GROUP BY c.city    
 ORDER BY kadunud_kliente DESC;

 SELECT        c.first_name || ' ' || c.last_name AS klient,        c.registration_date,        c.city,        c.loyalty_tier    
 FROM customers c    LEFT JOIN sales s ON c.customer_id = s.customer_id    
 WHERE s.sale_id IS NULL    
 ORDER BY c.registration_date DESC;

 SELECT        CASE            WHEN s.sale_id IS NULL THEN 'Kadunud (pole ostnud)'            ELSE 'Aktiivne (on ostnud)'        END AS staatus,        COUNT(DISTINCT c.customer_id) AS kliente    
 FROM customers c    LEFT JOIN sales s ON c.customer_id = s.customer_id    GROUP BY        CASE            
 WHEN s.sale_id IS NULL THEN 'Kadunud (pole ostnud)'            
 ELSE 'Aktiivne (on ostnud)'        END;

 Raport Annale – Kadunud kliendid

Analüüsi tulemused näitavad, et UrbanStyle andmebaasis on 599 klienti, kes on registreerunud, kuid pole veel ühtegi ostu sooritanud. Kõige rohkem selliseid kliente on Tallinnas (231), Tartus (133) ja Pärnus (70). Kadunud kliendid registreerusid peamiselt 2025. aasta jaanuaris ja veebruaris, kuid ei ole pärast registreerumist ostu teinud. Võrdluseks on aktiivseid kliente 2551, seega moodustavad ostuta kliendid märkimisväärse sihtrühma. Soovitan neile saata personaalse tervituskampaania koos esmaostu sooduskoodi või tasuta tarne pakkumisega, et motiveerida neid tegema esimene ost ja suurendada aktiivsete klientide arvu.

 <img width="1831" height="868" alt="week3_roll_b_kadunud_kliendid sql" src="https://github.com/user-attachments/assets/8df46a05-0f45-4d35-a625-b4fba6e25c91" />

