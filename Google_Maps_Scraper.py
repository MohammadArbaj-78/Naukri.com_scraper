import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import sys
import os

# --- First Error Heandling code ---
def quiet_exit(exctype, value, traceback):
    if issubclass(exctype, (OSError, ImportError, AttributeError)): return
    sys.__excepthook__(exctype, value, traceback)
sys.excepthook = quiet_exit

def get_driver():
    options = uc.ChromeOptions()
    
    # 1. List of Random User-Agents (ताकि हर बार डिवाइस अलग लगे)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    ]
    options.add_argument(f'--user-agent={random.choice(user_agents)}')

    # Winsdows Specific Ficks
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')

    try:
        # Starting Brouser (आपके वर्जन 146 के हिसाब से)
        print("Start Brouser")
        driver = uc.Chrome(options=options, use_subprocess=True, version_main=146)
        
        # 2. Hide 'Automation' Flage (Navigator.webdriver)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })
        return driver
    except Exception as e:
        print(f"Driver Error: {e}")
        return None

def scrape_site(url):
    driver = get_driver()
    if not driver: return

    try:
        # 3. Random window size (पूरी तरह इंसान जैसा दिखने के लिए)
        widths = [1920, 1366, 1536, 1440]
        heights = [1080, 768, 864, 900]
        driver.set_window_size(random.choice(widths), random.choice(heights))
        
        driver.get(url)
        
        # 4. Random Dealay (4 से 9 सेकंड)
        time.sleep(random.uniform(4, 9))
        
# Scraping Actions ---------------------------------------------------------------------------------------

        elem=driver.find_element(By.NAME,'q')          # find search box
        elem.clear()                                   # clean search box
        elem.send_keys("Top 10 IT Companies In Indore")            # search title 
        elem.send_keys(Keys.RETURN)                    # press enter key
        time.sleep(5)


        scrollable_div = driver.find_element(By.CSS_SELECTOR, "div[role='feed']")
    
        # 2. अब उस खास पैनल के अंदर स्क्रॉल करें (window की जगह arguments[0] का इस्तेमाल करें)
        # 700 पिक्सेल नीचे जाने के लिए
        for i in range(20): 
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            print("Scrolling Down...")
            time.sleep(random.uniform(2, 4))

        parent_el=driver.find_elements(By.CLASS_NAME,"lI9IFe")
        count=0
        for parent in parent_el:

            name=parent.find_element(By.CLASS_NAME,"qBF1Pd")
            print(name.text)
            try:
               phone=parent.find_element(By.CLASS_NAME,"UsdlK")
               print(phone.text)
            except:
                print("Number Not Avalable....")
            el=parent.find_elements(By.CLASS_NAME,"W4Efsd")[1]
            add=el.find_elements(By.CLASS_NAME,"W4Efsd")[0]
            print(add.text)
            try:
               url=parent.find_element(By.CLASS_NAME,"lcr4fd").get_attribute("href")
               print(url,'\n')
            except:
                print('Not Found')
            count+=1

        time.sleep(5)

        print(f"Total Companies : {count}")

# ----------------------------------------------------------------------------------------

        
        # वापस 300 पिक्सेल ऊपर आने के लिए
        driver.execute_script("arguments[0].scrollTop = 300", scrollable_div)
        print("Scrolling Up...")
        print(f"Succesfull : {driver.title}")

    except Exception as e:
        print(f"Scraping Error: {e}")
    
    finally:
        try:
            driver.quit()
        except:
            pass
        print("Complete Cleanup")
        os._exit(0) # Quickly out without error

if __name__ == "__main__":
    scrape_site("https://www.google.com/maps")


