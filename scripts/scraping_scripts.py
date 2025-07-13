from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


os.makedirs("raw_html",exist_ok=True)

driver = webdriver.Chrome()

try:
    for i in range(2,50):
        print(f"Scraping page {i}...")
        driver.get(f"https://www.naukri.com/data-analyst-jobs-{i}?k=data+analyst&wfhType=0")
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "srp-jobtuple-wrapper"))
            )
        time.sleep(4)

        html = driver.page_source
        with open(f"raw_html/page_{i}.html", "w", encoding="utf-8") as f:
                f.write(html)

        print(f"Saved page_{i}.html")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()