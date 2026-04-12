import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import random
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains

count=0

def human_behavior(driver):
    print("Human behavior (Mouse Movement) start...")
    actions = ActionChains(driver)
    
    # step 1: scrolling mouse rendomly on screen (without any element)
    for _ in range(3):
        x_offset = random.randint(100, 500)
        y_offset = random.randint(100, 500)
        actions.move_by_offset(x_offset, y_offset).perform()
        # again mouse take fix its position so that not come error
        actions.move_by_offset(-x_offset, -y_offset).perform() 
        time.sleep(random.uniform(0.5, 1.5))

    # step 2: if show any job kart place mouse over it (special to job)
    try:
        # On job, job title 'a' tag and .title' avalaible in class
        elements = driver.find_elements(uc.By.CSS_SELECTOR, "a.title, .jobTuple")
        if elements:
            target = random.choice(elements[:3])
            actions.move_to_element(target).perform()
            print(f"Took away mouse on  {target.text[:15]}... ")
    except:
        pass


# --- in starting to error heandling ---
def quiet_exit(exctype, value, traceback):
    if issubclass(exctype, (OSError, ImportError, AttributeError)): return
    sys.__excepthook__(exctype, value, traceback)
sys.excepthook = quiet_exit

def get_driver():
    options = uc.ChromeOptions()
    print('Start brouser')
    
    # 1. List of random user-agent (so that device any time different)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    ]
    options.add_argument(f'--user-agent={random.choice(user_agents)}')

    # window specific fix
    # options.add_argument("--headless=new")     # do not show window
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument("--disable-features=CalculateNativeWinOcclusion")
    options.add_argument("--disable-notifications")
    options.page_load_strategy='eager'

    # do not image loading
    p={
       "profile.managed_default_content_settings.media_stream":2,
       "profile.managed_default_content_settings.geolocation":2}
    options.add_experimental_option("prefs",p)

    try:
        # Starting Brouser (According to your version)
        driver = uc.Chrome(options=options, use_subprocess=True, version_main=146)
        
        # 2. Hide 'Automation' Flage (Navigator.webdriver)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })
        return driver
    except Exception as e:
        print(f"Driver Error: {e}")
        return None

def scrape_site():
    driver = get_driver()
    if not driver: return

    try:
        # 3. random window size (seen to proper human)
        widths = [1920, 1366, 1536, 1440]
        heights = [1080, 768, 864, 900]
        driver.set_window_size(random.choice(widths), random.choice(heights))
        print(f"Opning the target ")
        num=0
        count=0
        for i in range(1,20):
            driver.get(f"https://www.flipkart.com/search?q=apple+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=apple+mobile%7CMobiles&requestId=47815b0e-cb72-4b63-a323-8df555b6b32e&as-searchtext=apple+mobile&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.processor_brand%255B%255D%3DApple&page={i}")
        
            # 4.   Random weating(2 to 4 seconds)
            time.sleep(random.uniform(2, 4))
        
            print("Scrolling...")
            
             # --- write scrolling (so that all the data loads) ---
            for s in range(3): # going to bottom some 3 times 
                driver.execute_script(f"window.scrollBy(0, 800);")
                time.sleep(random.uniform(1,4))
    
            # human_behavior(driver)
    
            # mager data consume scrolling human behavior and undetected crome drive 10 mp

# -----------------------------------------------------------------------------------------------------------
            element=driver.find_elements(By.CLASS_NAME,'ZFwe0M')
            for el in element:
                data=el.get_attribute('outerHTML')
                count=count+1
                num=num+1
                with open(f"C:\\Emergent\\webscraping\\scrapers\\Seleniuam scrapers\\Flip_kart data\\{num}.html",'w',encoding='utf-8') as f:
                     f.write(data)

        print(f"Total Product : {count}")
        

# -----------------------------------------------------------------------------------------------------------

        print(f"Succesful Title : {driver.title}")

    except Exception as e:
        print(f"Scraping Error: {e}")
    
    finally:
        try:
            driver.quit()
        except:
            pass
        print("Complete Cleanup.")
        os._exit(0) # to exite immediatly without error

if __name__ == "__main__":
        scrape_site()

# ------------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import pandas as pd

data_list=[]
for i in range(1,264):
    with open(f"C:\\Emergent\\webscraping\\scrapers\\Seleniuam scrapers\\Flip_kart data\\{i}.html","r",encoding='utf-8') as f:
         d=f.read()  
         soup=BeautifulSoup(d,'html.parser')
    data_dic={
         'name': soup.find('div', class_="RG5Slk").text if soup.find('div', class_="RG5Slk") else "N/A",
         'price':soup.find('div',class_="hZ3P6w DeU9vF").text
         }
    data_list.append(data_dic)

data=pd.DataFrame(data_list)

print(data)

data.to_csv(r'C:\Emergent\webscraping\scrapers\Seleniuam scrapers\Flip_kart data\data.csv', index=False, encoding='utf-8')

print("csv created succesfully")

