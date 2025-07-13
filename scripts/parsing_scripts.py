import pandas as pd
from bs4 import BeautifulSoup

data = []

for i in range(2,50):
    with open(f"raw_html/page_{i}.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')

    for job in job_cards:
        title = job.find("a",class_ = "title")
        company = job.find("a",class_ = "comp-name")
        experience = job.find("span",class_ = "exp-wrap")
        location = job.find("span",class_ = "loc-wrap")
        skills = job.find("ul",class_ = "tags-gt")
        skill_list = [li.text.strip() for li in skills.find_all("li")] if skills else []
        salary = job.find('li', class_='salary')
        
        job_data = {
            "Title": title.text.strip() if title else "N/A",
            "Company": company.text.strip() if company else "N/A",
            "Experience": experience.text.strip() if experience else "N/A",
            "Location": location.text.strip() if location else "N/A",
            "Salary": salary.text.strip() if salary else "Not Mentioned",
            "Skills": ', '.join(skill_list)
        }

        data.append(job_data)

# ✅ Convert to DataFrame
df = pd.DataFrame(data)

# ✅ Save as CSV
df.to_csv("cleaned_jobs_data.csv", index=False, encoding="utf-8-sig")

print("✅ Saved cleaned_job_data.csv with", len(df), "rows.")
