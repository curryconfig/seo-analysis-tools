import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TARGET_URL = "http://loadtiktok.wuaze.com"

def run_bot():
    driver_path = '/usr/bin/chromedriver' 
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={ua}")

    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(driver_path)
    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        refs = ["https://www.google.com/", "https://t.co/", "https://www.facebook.com/", "https://www.bing.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})

        driver.get(TARGET_URL)
        time.sleep(random.randint(20, 45))
        
        driver.execute_script(f"window.scrollBy(0, {random.randint(300, 700)});")
        time.sleep(5)
        
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            target = random.choice(links)
            driver.execute_script("arguments[0].click();", target)
            time.sleep(20)

    except Exception:
        pass
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(random.randint(10, 30))
      
