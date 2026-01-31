import time
import random
import shutil
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TARGET_URL = "http://loadtiktok.wuaze.com"

def get_driver():
    # Nyari otomatis path chromedriver & chromium bgsd!
    driver_path = shutil.which('chromedriver') or '/usr/bin/chromedriver'
    chrome_bin = shutil.which('chromium') or shutil.which('chromium-browser') or '/usr/bin/chromium-browser'
    
    chrome_options = Options()
    chrome_options.binary_location = chrome_bin
    
    # Mantra Anti-Ciduk & Anti-Signal 9
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # User Agent PC Kantoran biar GA seneng
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={ua}")

    # Irit Bandwidth & RAM
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service, options=chrome_options)

def run_bot():
    driver = None
    try:
        driver = get_driver()
        
        # Referrer Ghaib
        refs = ["https://www.google.com/", "https://t.co/", "https://www.facebook.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})

        print(f"[*] Menyerang: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Nongkrong lama (Retention Tinggi)
        time.sleep(random.randint(40, 70))
        
        # Gerakan Manusiawi
        driver.execute_script(f"window.scrollBy(0, {random.randint(300, 800)});")
        time.sleep(5)
        
        # Klik Link Internal (Biar GA nyatet bounce rate rendah)
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            target = random.choice(links)
            driver.execute_script("arguments[0].click();", target)
            print("[V] Pindah Halaman Berhasil.")
            time.sleep(15)

        print(f"[V] Sesi Clear! [{time.strftime('%H:%M:%S')}]")
        
    except Exception as e:
        print(f"[-] Gagal: {str(e)[:50]}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        jeda = random.randint(10, 25)
        print(f"[@] Cooling down {jeda}s...")
        time.sleep(jeda)
