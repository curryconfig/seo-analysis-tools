import time
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Path khusus buat di Docker/Railway
    chrome_options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get("http://loadtiktok.wuaze.com")
        print("[+] Ngebom via Railway...")
        time.sleep(random.randint(30, 60))
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(10)
        
