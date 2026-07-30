# 📊 UrbanStyle Investor Dashboard – Final Analysis

**Author:** Kalju Tamme  
**Project:** DACA Programme – Week 5: Visualisation Design (Track B)

This project is a fully functional, interactive investor dashboard built with Python, Streamlit, and Plotly. It connects to a live Supabase database, processes sales data, and presents key performance indicators (KPIs) alongside dynamic visualisations. The final version includes advanced features such as percentage changes over comparable periods, annotated charts, and a clean modular codebase.

---

## 🚀 The Project

The dashboard was designed to give investors a real‑time overview of UrbanStyle’s sales performance with a focus on actionable insights. It features:

- 📈 **Monthly Revenue Trend** – Time‑series line chart with an average reference line and **markers for the top 3 revenue months**.
- 🏆 **Top Products** – Horizontal bar chart with **continuous, rounded labels** (e.g. €3.1k) for instant readability.
- 🏙️ **Sales by City** – Pie chart showing revenue distribution; small cities are grouped into “Other Cities” for clarity.
- 🔍 **Interactive Filters** – Filter by city, date range, and sales channel/location – all charts update instantly.
- 💰 **Live KPI Cards** – Total revenue, order count, unique customers, and average order value, each **showing the percentage change compared to the previous period of the same length** (or the longest available previous period).

---

## 📈 Key Findings & Business Insights

The dashboard reveals several important patterns about UrbanStyle’s business in Pärnu:

1. **Pärnu is a strongly summer‑focused location.**  
   The top 3 revenue months are **July, August, and September**. There is no significant year‑end sales spike.

2. **Seasonal product dominance.**  
   Four out of the top five products contain the word *"Õhuline"* (Airy), which clearly indicates summer‑oriented merchandise.

3. **Year‑over‑year growth with one warning sign.**  
   Compared to 2023, the 2024 KPIs grew between **8.7% and 13.6%** – except for the **average order value**, which **dropped by 3.8%**. This merits further investigation.

4. **End‑of‑year campaigns had little impact.**  
   Promotions in November and December did not generate the expected uplift, confirming that the business is strongly seasonal.

5. **Local customers are a minority.**  
   Only **15% of revenue** comes from local buyers – the vast majority are tourists.

**Conclusion:** Pärnu is a summer‑driven market. Marketing efforts and inventory should focus on the peak season, while year‑end campaigns may be deprioritised. Given the high share of tourist customers, there is a clear opportunity to **consider raising prices** without significantly hurting demand.

---

## ⚙️ Technical Challenges (The Real Learning) 🛠️ What I Did (Beyond the Requirements)

To make the dashboard more insightful and maintainable, I added several enhancements:

1. **Refactored the Entire Codebase**  
   - I rewrote the previous week’s code into a **modular structure**:
     - `Data_Loader.py` – Supabase connection and pagination.
     - `Filters.py` – data filtering logic.
     - `Kpi.py` – KPI calculation with delta comparisons.
     - `Charts.py` – all Plotly chart definitions.
     - `App.py` – main Streamlit application, clean and lightweight.

2. **Added Continuous Labels & Annotations**  
   - **Bar chart:** Each bar now permanently displays a **rounded revenue value** (e.g., €3.1k) – no need to hover.  
   - **Line chart:** The **three highest‑revenue months** are marked with red stars and value labels, making them stand out immediately.

3. **Renamed Pie Chart Slices**  
   - I renamed the piechart into "Kliendid asukoha järgi" because its shows from where are customers coming. I did not think of it before as valuable chart however in situation to Pärnu i found this data helped me to make decision that Pärnu is highly tourist based location.

4. **KPI Percentage Change**  
   - For each KPI, I added a **delta** that compares the current filtered period with the **previous period of exactly the same length**. If such a period doesn’t exist (e.g., at the beginning of the dataset), it compares with the longest available previous period. This gives investors a true sense of growth.

5. **Brokedown Code into Logical Modules**  
   - Each file now has a single responsibility, making the code far more readable, testable, and maintainable.

---

## 📁 Project Structure

```text
Dashboards/
├── dashboard/
│   ├── App.py                # Main Streamlit application
│   ├── Data_Loader.py        # Supabase connection & pagination
│   ├── Charts.py             # Plotly chart definitions
│   ├── Filters.py            # Filtering logic
│   └── Kpi.py                # KPI calculation with deltas
├── .env                      # Supabase credentials (ignored by Git)
├── .gitignore                # Protects .env and .venv
├── requirements.txt          # Python dependencies
└── README.md                 # This file
