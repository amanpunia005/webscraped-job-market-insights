📊 Web Scraped Job Market Insights (Python + SQL + Power BI)
📌 Project Overview

This project scrapes and analyzes job postings from multiple sources to uncover top hiring companies, in-demand skills, and job location trends.
The end-to-end workflow covers web scraping (Python), data cleaning, SQL queries, EDA in Jupyter, and visualization with Power BI.

📂 Repository Structure
├── 📂 data/            # Raw scraped HTML + cleaned CSV datasets
├── 📂 scripts/         # Python scripts for scraping & cleaning
├── 📂 notebooks/       # Jupyter notebooks for EDA
├── 📂 visualizations/  # Charts & plots from analysis
├── 📂 summary/         # Reports & markdown summaries
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore venv, checkpoints, cache
└── README.md           # Project documentation

⚙️ Tech Stack

Languages: Python (Requests, BeautifulSoup, Pandas, Matplotlib, Seaborn), SQL
Tools: Jupyter Notebook, Power BI
Database: SQLite

🔑 Steps & Workflow

Web Scraping (Python)

Used requests + BeautifulSoup to extract job postings.

Parsed job titles, companies, skills, locations, and salaries.

Data Cleaning

Removed duplicates, standardized company names, extracted skills list.

Added features like Skill Count and City Grouping.

Exploratory Data Analysis (Python)

Analyzed hiring trends by company, skill demand, and location.

Built visualizations: top 10 hiring companies, top skills, top job cities.

SQL Queries

Queried SQLite DB for:

Top 5 companies hiring most

Skill demand distribution

Jobs per city

Power BI Dashboard

Interactive dashboard showing:

Top Hiring Companies

Most Demanded Skills

Jobs by City

Filters for skill, company, and city.

📊 Key Insights

Top Hiring Companies: Infosys, TCS, Accenture lead hiring.

Most In-Demand Skills: SQL, Python, and Excel dominate job postings.

Top Cities: Bangalore, Hyderabad, Pune are hiring hubs.

(📌 See detailed notebook analysis
)

🚀 Impact

✔️ Built an end-to-end pipeline from scraping → cleaning → SQL → Power BI
✔️ Provided job market insights useful for job seekers & recruiters
✔️ Showcased ability to combine Python + SQL + BI tools in real projects

📌 How to Run Locally

Clone this repository

git clone https://github.com/amanpunia005/webscraped-jobmarket-insights.git
cd webscraped-jobmarket-insights


Install requirements

pip install -r requirements.txt


Run the scraper

python scripts/scraper.py


Open Jupyter Notebook for EDA

jupyter notebook notebooks/job_analysis.ipynb


Explore Dashboard

Open Power BI file from /visualizations/Job_Market.pbix

Or check dashboard screenshots below 👇

📸 Dashboard Preview

(👉 Add 2–3 screenshots here of your Power BI dashboard & plots. Recruiters love visuals!)

📧 Contact

👤 Aman Puniya

LinkedIn: www.linkedin.com/in/aman-puniya

GitHub: www.github.com/amanpunia005

Email: puniyaaman0@gmail.com