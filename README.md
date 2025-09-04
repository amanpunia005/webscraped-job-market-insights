# 💼 Web-Scraped Job Market Insights

This project delivers a **data-driven analysis of the Indian job market** by scraping real-time job postings and extracting actionable hiring insights.  
The end-to-end workflow covers **data collection, cleaning, exploratory data analysis (EDA), visualization, and insights reporting**.

---

## 📂 Project Structure

`WebScraped_JobMarket_Insights/
│
├── data/ # Data assets
│ ├── raw_html/48_pages.html # Raw scraped HTML pages
│ ├── scraped_jobs.xlsx # Extracted raw job postings
│ └── cleaned_jobs.csv # Final cleaned dataset
│
├── notebooks/ # Jupyter notebooks
│ ├── 01_eda.ipynb
│ ├── 02_company_level_insights.ipynb
│ ├── 03_job_category_pieplot.ipynb
│ ├── 04_job_titles_distribution.ipynb
│ ├── 05_skills_demand.ipynb
│ ├── 06_top_10_locations.ipynb
│
├── visualizations/ # Exported visuals
│ ├── hiring_companies_analysis.png
│ ├── job_category_pie.png
│ ├── top_10_cities_jobs.png
│ ├── top_10_skills_demand.png
│ └── top_job_titles_logscale.png
│
├── scripts/ # Automation scripts
│ ├── scraping_script.py
│ └── parsing_script.py
│
├── summary/ # Final business summary
│ └── final_project_summary.pdf
│
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── README.md # Project documentation`
