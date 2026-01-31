import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TARGET_URL = "http://loadtiktok.wuaze.com"

def run_bot_cloud():
    # Path standar di Google Cloud Shell
    driver_path = '/usr/bin/chromedriver' 
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # User Agent biar dikira trafik dari PC kantoran
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"--user-agent={ua}")

    # Diet Gambar biar kenceng bgsd!
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(driver_path)
    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Referrer biar GA Gacor (Google, Twitter, Facebook)
        refs = ["https://www.google.com/", "https://t.co/", "https://www.facebook.com/", "https://www.bing.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})

        print(f"[*] Menyerang Target: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Nongkrong lama biar GA nyatet (High Retention)
        time.sleep(random.randint(30, 60))
        
        # Simulasi scroll biar dikira manusia baca
        driver.execute_script(f"window.scrollBy(0, {random.randint(400, 800)});")
        time.sleep(10)
        
        # Klik link random biar sesi valid
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            target = random.choice(links)
            driver.execute_script("arguments[0].click();", target)
            print(f"[V] Pindah Halaman Berhasil.")
            time.sleep(20)

        print(f"[V] Sesi Berhasil Diselesaikan! [{time.strftime('%H:%M:%S')}]")
        
    except Exception as e:
        print(f"[-] Error: {str(e)[:50]}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        run_bot_cloud()
        # Kasih jeda istirahat biar kaga diciduk Google
        jeda = random.randint(15, 30)
        print(f"[@] Istirahat {jeda}s...")
        time.sleep(jeda)
