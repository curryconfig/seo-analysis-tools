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
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    chrome_options.binary_location = "/usr/bin/chromium"
    service = Service("/usr/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Pake Referrer Gacor
        refs = ["https://www.google.com/", "https://t.co/", "https://www.bing.com/"]
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'Referer': random.choice(refs)}})
        
        driver.get("http://loadtiktok.wuaze.com")
        print(f"[+] HuggingFace Power: Menyerang... [{time.strftime('%H:%M:%S')}]")
        
        # Nongkrong lama (Anti Signal 9 karena RAM Gede)
        time.sleep(random.randint(60, 180)) 
        driver.execute_script("window.scrollBy(0, 500);")
        
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(10)
