import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Lokasi standar di Docker/Koyeb
    chrome_options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Pake Referrer biar makin meyakinkan
        refs = ["https://www.google.com/", "https://t.co/", "https://www.bing.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})
        
        driver.get("http://loadtiktok.wuaze.com")
        print(f"[+] Koyeb Power: Ngebom Target... [{time.strftime('%H:%M:%S')}]")
        
        # Nongkrong lebih lama (High Retention)
        time.sleep(random.randint(60, 150)) 
        
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(10)
        
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        # Kasih jeda istirahat biar CPU VPS kaga teriak
        jeda_napas = random.randint(30, 60)
        print(f"[*] Istirahat {jeda_napas} detik...")
        time.sleep(jeda_napas)
        
