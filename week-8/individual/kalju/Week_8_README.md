# 📦 Week 8: Data Extraction Pipeline – Supabase + CSV Fallback

**Author:** Kalju Tamme  
**Project:** DACA Programme – Week 8: Building a Robust Data Loading Module for UrbanStyle

This project implements a reusable Python module (`data_fetcher.py`) that fetches customer, product, and sales data from a Supabase database with automatic pagination (handling the 1000‑row limit) and graceful fallback to local CSV files. The module is designed to be imported into a larger data‑processing pipeline (`pipeline.py`) that performs cleaning, transformation, and analysis.

---

## 🚀 The Project

### Objective
UrbanStyle’s analytics workflow requires reliable data ingestion. The goals of this week’s work were:

- Build a robust data‑loading function that connects to Supabase using environment variables.
- Implement pagination to retrieve all rows (Supabase limits responses to 1000 rows per request).
- Provide date‑filtering for the sales table (`start_date`, `end_date`) with an option to fetch the full table.
- Add try‑except blocks for each table so that if Supabase is unavailable, the code automatically reads from local CSV files (stored in a `Data/` folder).
- Ensure the module integrates seamlessly with the existing `pipeline.py` and `transform.py` components.

### My Contribution (Roll A – Data Loading)
I wrote the entire extraction module `data_fetcher.py`, which contains three core functions:

- `fetch_sales(start_date=None, end_date=None)`  
- `fetch_customers()`  
- `fetch_products()`

Each function:
- Uses the Supabase Python client with pagination (offset/limit).
- Includes date filtering for sales (adjustable to the actual column name).
- Catches any exception (connection errors, timeouts, etc.) and falls back to `pd.read_csv()` from the `Data/` directory.
- Returns a pandas DataFrame ready for downstream processing.

The code is fully documented and designed to be dropped into any project that needs reliable data ingestion from Supabase.

### Team Collaboration
This week’s work is part of a larger pipeline. Other teammates are responsible for:

- **Roll B – Data Cleaning:** Handling missing values, duplicates, and type conversions.  
- **Roll C – Transformation:** Calculating weekly aggregates, KPIs, and merging datasets.  
- **Roll D – Visualisation & Reporting:** Creating dashboards or summaries from the final data.

My extraction module provides the foundation that all subsequent steps rely on.

---

## 📈 Key Features & Benefits

- **Pagination:** Automatically loops through all records, so you never miss a row.
- **Date filtering:** Fetch only a specific time window for sales (e.g., last month, year‑to‑date) or the entire table.
- **Resilience:** If Supabase is down or the network fails, the code falls back to local CSV files without crashing the pipeline.
- **Modular design:** Easily import into any script or notebook; no hard‑coded paths (uses `os.path.join`).
- **Environment variables:** Credentials are stored securely in `.env` and loaded via `python‑dotenv`.

---

## ⚙️ Technical Challenges & Personal Learnings

### Challenges I Faced

- **Virtual environment confusion:**  
  Even though I used `venv`, VS Code sometimes selected the wrong kernel. I resolved it by explicitly setting the interpreter and verifying with `import sys; print(sys.executable)`.

- **Pagination implementation:**  
  I had to carefully manage the offset and break condition (when the response returns fewer than 1000 rows). Testing with large tables helped me confirm the loop works correctly.

- **Date‑filtering flexibility:**  
  The sales table in Supabase uses a column named `"date"`; I made the function parameters generic so that future adjustments are easy.

- **Fallback CSV paths:**  
  I wanted the CSVs to reside in a separate `Data/` folder for tidiness. Using `os.path.join("Data", "sales.csv")` ensures cross‑platform compatibility.

### What I Learned Most

- **Error handling is essential:**  
  Writing try‑except for each fetch gave me confidence that the pipeline won’t break unexpectedly in production.

- **Pagination is a common pain point:**  
  Many APIs limit response size – now I have a reusable pattern that I can apply to other REST APIs.

- **Modular code pays off:**  
  Keeping the data loading logic separate from cleaning and analysis made the code easier to test and debug.

- **Collaboration requires clear interfaces:**  
  I made sure my functions return standard DataFrames and accept well‑defined parameters so that my teammates could plug their code in without friction.

---

## 📁 Repository Structure

