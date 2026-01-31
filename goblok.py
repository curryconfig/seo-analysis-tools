import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # Senjata baru bgsd!

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Pake ChromeDriverManager biar dia download sendiri driver yang cocok
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def run_bot():
    driver = None
    try:
        driver = get_driver()
        driver.get("http://loadtiktok.wuaze.com")
        print(f"[+] Serangan Berhasil! [{time.strftime('%H:%M:%S')}]")
        time.sleep(random.randint(30, 60))
    except Exception as e:
        print(f"[-] Gagal bgsd: {str(e)[:100]}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(10)
