# 💼 Web-Scraped Job Market Insights

This project delivers a **data-driven analysis of the Indian job market** by scraping real-time job postings and extracting actionable hiring insights.  
The end-to-end workflow covers **data collection, cleaning, exploratory data analysis (EDA), visualization, and insights reporting**.

---

## 📂 Project Structure

```WebScraped_JobMarket_Insights/
│
├── data/ # Data assets
│ ├── raw_html/48_pages.html # Raw scraped HTML pages
│ ├── scraped_jobs.xlsx # Extracted raw job postings
│ └── cleaned_jobs.csv # Final cleaned dataset
│
|
├── notebooks/ # Jupyter notebooks
│ ├── 01_eda.ipynb
│ ├── 02_company_level_insights.ipynb
│ ├── 03_job_category_pieplot.ipynb
│ ├── 04_job_titles_distribution.ipynb
│ ├── 05_skills_demand.ipynb
│ ├── 06_top_10_locations.ipynb
│
|
├── visualizations/ # Exported visuals
│ ├── hiring_companies_analysis.png
│ ├── job_category_pie.png
│ ├── top_10_cities_jobs.png
│ ├── top_10_skills_demand.png
│ └── top_job_titles_logscale.png
│
|
├── scripts/ # Automation scripts
│ ├── scraping_script.py
│ └── parsing_script.py
│
|
├── summary/ # Final business summary
│ └── final_project_summary.pdf
│
|
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── README.md # Project documentation


---
```
## 🚀 Tech Stack

- **Python** (pandas, BeautifulSoup, requests, matplotlib, seaborn)
- **Excel** (intermediate cleaning & validation)
- **Jupyter Notebooks** (EDA & analysis)
- **Matplotlib & Seaborn** (visual storytelling)

---

## 🔍 Key Analyses & Insights

- **Hiring Companies Analysis**  
  Identified the most active recruiters in the dataset.

- **Job Category Distribution**  
  Showed demand concentration across technical and non-technical roles.

- **Top Job Titles (Log Scale)**  
  Highlighted demand hotspots in IT, data, and management roles.

- **Skills Demand Analysis**  
  Mapped the most sought-after technical and business skills.

- **Location Insights**  
  Top 10 Indian cities by job postings, spotlighting hiring hubs.

---

## 📊 Visual Highlights

| Hiring Companies | Job Category Pie | Top 10 Cities | Skills Demand | Job Titles |
|------------------|------------------|---------------|---------------|------------|
| [Hiring](visualizations/hiring_companies_analysis/top_5_company_hiring_by_experience.png) | ![Pie](visualizations/job_category_pie.png) | ![Cities](visualizations/top_10_cities_jobs.png) | ![Skills](visualizations/top_10_skills_demand.png) | ![Titles](visualizations/top_job_titles_logscale.png) |

---


## 📈 End-to-End Workflow

1. **Scraping** – Automated scraping of 48 HTML pages using Python.
2. **Parsing** – Extracted structured job posting data (title, company, location, skills, category).
3. **Cleaning** – Removed duplicates, standardized categories, normalized skill names.
4. **EDA** – Conducted exploratory analysis in Jupyter Notebooks.
5. **Visualization** – Generated charts for clear business storytelling.
6. **Summary Report** – Consolidated findings into a final PDF for recruiters & stakeholders.

---

## 🏆 Business Value

- Helps **job seekers** identify in-demand skills and locations.  
- Assists **companies** in understanding competitor hiring trends.  
- Provides **market intelligence** for HR and talent acquisition teams.

---

## 🔧 How to Run the Project

1. Clone this repository:  
   ```bash
   git clone https://github.com/amanpunia005/webscraped-job-market-insights.git
   cd webscraped-job-market-insights

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run scraping & parsing scripts:
   ```bash
    python scripts/scraping_script.py
    python scripts/parsing_script.py

4. Explore analysis:
   ```bash
    Open notebooks/ in JupyterLab or VSCode.

Aman Puniya

LinkedIn: www.linkedin.com/in/aman-puniya

GitHub: www.github.com/amanpunia005

Email: puniyaaman0@gmail.com

⭐ If you found this project insightful, consider giving it a star on GitHub!


