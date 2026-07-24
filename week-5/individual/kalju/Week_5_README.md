# 📊 UrbanStyle Investor Dashboard

**Author:** Kalju Tamme  
**Project:** DACA Programme – Week 5: Visualisation Design (Track B)

An interactive, fully functional investor dashboard built with Python, Streamlit, and Plotly. This project connects to a live Supabase database, processes sales data, and presents key performance indicators (KPIs) alongside dynamic visualisations.

---

## 🚀 The Project

This dashboard was designed to give investors a clear, real-time overview of UrbanStyle's sales performance. It features:

- 📈 **Monthly Revenue Trend** – Time-series line chart with an average reference line.
- 🏆 **Top Products** – Horizontal bar chart ranking the best-selling items.
- 🏙️ **Sales by City** – Pie chart showing revenue distribution across locations.
- 🔍 **Interactive Filters** – Filter by city, date range, and sales channel/location.
- 💰 **Live KPI Cards** – Total revenue, order count, unique customers, and average order value.

---

## 🧠 My Learning Journey & Challenges Overcome

While the weekly instructions asked us to *plan* the dashboard layout and select appropriate charts, I decided to go a step further and **build the entire fully functional application**. Here is how I tackled the core tasks and the real-world problems I solved along the way.

### 📝 Weekly Tasks (Completed)

1. **Selecting the Right Graph Types**
   - **Sales per Month:** A line chart was the obvious choice to display trends over time.
   - **Top Products:** I chose a bar chart. Initially, I tried a vertical orientation, but I determined it was **ugly and hard to read** due to long product names. Switching to a **horizontal bar chart** was a massive improvement in readability.

2. **Determining the Dashboard Layout**
   - I agreed with the proposed layout structure. I placed KPI cards at the top, the revenue trend as the main focus, and the product/city charts side-by-side.
   - **Color Adjustments:** At first, I was annoyed by the light colors of the bar chart (e.g., using `"Reds"`). They blended into the white background. However, I realized that on a dark browser theme, these colors look perfectly fine. For versatility, I switched to `"Viridis"` for better contrast.

3. **Selecting Filters and Their Logic**
   - I followed the instructions and implemented filters for **City**, **Date Range**, and **Sales Channel/Location**. The logic ensures that all charts update simultaneously, providing a truly interactive investor experience.

---

### ⚙️ Technical Challenges (The Real Learning)

1. **Setting up a Virtual Python Environment**
   - I learned how to set up a localized virtual environment (`.venv`). This kept my laptop clean and isolated the project dependencies, preventing conflicts with other Python projects.

2. **The Supabase 1,000-Row Limit (Pagination)**
   - **The Problem:** Supabase restricts API calls to 1,000 rows by default. Initially, my timeline graph showed a huge gap in data (missing all of 2024) because it only loaded the first 1,000 rows.
   - **The Struggle:** Using `.limit()` or `.range()` did not bypass the server-side limit.
   - **The Solution:** I implemented a **looped pagination** system. My code now asks for 1,000 rows at a time in a `while` loop until all data is fetched. This gave me a complete timeline from 2023 to 2026.

3. **Adapting Code to My Personal Data Schema**
   - The tutorial assumed separate columns for `channel` (online/store) and `store_location`. However, I had previously merged these into a single `location` column in my database.
   - I successfully modified the data loader and filter logic to work with my `location` column, ensuring the app fit my unique dataset.

4. **Detecting the Missing Data Problem**
   - The missing data issue was **discovered directly from the timeseries chart**. When I saw the massive gap from April 2023 to December 2025, I realized the data wasn't loading properly. This visual clue was the key to diagnosing the pagination problem.

5. **Design Tweaks (Pie Chart Grouping)**
   - I changed the pie chart grouping limit from **3% to 5%**. At 3%, too many tiny towns cluttered the chart (4 small towns). Setting it to 5% grouped all the small outliers into a single "Muud linnad" (Other Cities) slice, making the chart much cleaner.

---

## 📁 Project Structure

```text
Dashboards/
├── dashboard/
│   ├── app.py                 # Main Streamlit application
│   ├── data_loader.py         # Supabase connection & pagination logic
│   └── charts.py              # Plotly chart definitions
├── .env                       # Supabase credentials (ignored by Git)
├── .gitignore                 # Protects .env and .venv
├── requirements.txt           # Python dependencies
└── README.md                  # This file
