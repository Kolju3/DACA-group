📊 UrbanStyle RFM Segmentation – Week 7 Group Project
Author: Kalju Tamme
Project: DACA Programme – Week 7: RFM Customer Segmentation (Track B)

This project is a complete Jupyter Notebook that implements an RFM (Recency, Frequency, Monetary) analysis for UrbanStyle’s customer data. The analysis segments customers into groups such as VIP Champions, Loyal, Potential, At Risk, and Lost, providing actionable business insights. The notebook also includes three interactive visualisations (built with Plotly) that present the segmentation results clearly.

🚀 The Project
Objective
UrbanStyle wants to understand its customer base better to tailor marketing campaigns. The specific goals were:

Load sales and customer data from Supabase (with a CSV fallback).

Clean and merge the data.

Compute RFM scores for each customer.

Assign customers to meaningful segments.

Visualise the results and provide business recommendations.

Team Collaboration
This was a group project with defined roles:

Role	Responsibility	Team Member
Roll A – Data Loading	Fetch and merge data from Supabase/CSV.	Natalia
Roll B – Data Cleaning	Handle missing values, duplicates, and date formats.	Olga
Roll C – RFM Analysis	Compute RFM scores, segments, and export CSV.	Helen
Roll D – Visualisation	Create interactive graphs and business interpretation.	Kalju (me)
The final output is a single Jupyter notebook that integrates all contributions, followed by the visualisation and interpretation (added by me).

📈 Key Findings & Business Insights
From the RFM analysis, we discovered:

Top 10 VIP Champions account for >8.5% of total revenue.
These high‑value customers are extremely loyal and should be treated with exclusivity – early access to new collections, VIP events, or personalised services – rather than price discounts.

“At Risk” and “Potential” segments are price‑sensitive.
These customers buy regularly but are limited by price. For them, discount‑focused campaigns (e.g., “20% off”) would be effective in boosting spend and preventing churn.

Lost customers represent less than 5% of revenue.
They are not worth a dedicated (expensive) win‑back campaign. General brand advertising is sufficient to maintain minimal awareness.

Pärnu is a strongly summer‑driven market.
Although not directly part of the RFM analysis, earlier work (Week 6) confirmed that the majority of customers are tourists, and sales are concentrated in summer months. This reinforces that pricing can be more aggressive in peak season, especially for the price‑sensitive segments.

⚙️ Technical Challenges & Personal Learnings
Challenges I Faced
Virtual Environment Setup
The biggest hurdle was getting the virtual environment to work consistently. I used venv on Linux Mint, but the Jupyter kernel sometimes picked the system Python instead of the environment, causing import errors (e.g., nbformat). Eventually, I had to explicitly select the correct kernel in VSCode.

Understanding My Team’s Code
The notebook contains ~300 lines of code from three teammates. It took considerable time to read and understand each section, especially how the DataFrames (df, rfm, segment_summary) were generated and what variables were available for my visualisation work.

Jupyter vs Pure Python
I found Jupyter challenging to start with because it mixes code, output, and markdown in a non‑linear way. However, I now appreciate its power for iterative data exploration and collaboration. For a pure script (e.g., for a dashboard), I’d prefer modular .py files.

Code Monolith
I strongly dislike large, monolithic code. I prefer to break logic into small, reusable modules. However, because the task required a single working Jupyter notebook, I had to adapt and keep everything in one place – which felt messy but was necessary for the group deliverable.

What I Learned Most
Teamwork means adapting to the team’s coding style.
I couldn’t refactor the whole notebook into separate modules; I had to work with the existing structure. This taught me flexibility and the importance of clear comments and variable naming for collaboration.

Virtual environments can still be confusing.
Even after setting up venv correctly, kernel selection in VSCode is not always intuitive. I now double‑check sys.executable inside the notebook to ensure I’m using the right interpreter.

📁 Repository Structure
text
.
├── urbanstyle_operatsioonid_week7_(a_b_c_d).ipynb   # Main Jupyter notebook
├── rfm_segments.csv                                  # Exported RFM segment data (optional)
├── .env                                              # Supabase credentials (not included)
├── .gitignore                                        # Protects secrets and venv
└── README.md                                         # This file
🛠️ How to Run the Notebook
Clone the repository and navigate to the project folder.

Create a virtual environment (recommended):

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
Install dependencies:

bash
pip install -r requirements.txt
(If requirements.txt is missing, install manually: pandas, supabase, python-dotenv, plotly, matplotlib, seaborn, nbformat, ipython.)

Set up .env with your Supabase credentials (if using live data):

text
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
Otherwise, place sales.csv and customers.csv in the same folder as the notebook.

Open the notebook in VSCode or Jupyter Lab and run all cells in order.

📊 Visualisations Added (Roll D)
I created three interactive graphs using Plotly:

Bar Chart – Customer distribution across segments, with percentage and count labels.

Scatter Plot – Recency vs Monetary value, coloured by segment, with bubble size = frequency. Interactive tooltips show customer ID and frequency.

Pie Chart – Shows the share of total revenue contributed by the top 10 VIP Champions.

All graphs are fully responsive and open in your browser when run.

🙏 Credits
Natalia – Data loading & merging.

Olga – Data cleaning & preprocessing.

Helen – RFM score calculation & segmentation.

Kalju – Visualisation, business interpretation, and this README.

📝 Final Notes
This project was a valuable exercise in collaborative data analysis. Despite the challenges, we delivered a working solution that gives UrbanStyle a clear view of its customer segments and actionable marketing strategies. The RFM analysis, combined with earlier findings about Pärnu’s tourist‑driven sales, provides a solid foundation for data‑driven decision‑making.
