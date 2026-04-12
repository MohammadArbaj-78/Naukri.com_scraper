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
    
    # 1. List of random user-agent (so that device any time different
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    ]
    options.add_argument(f'--user-agent={random.choice(user_agents)}')

    # window specific fix
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument("--disable-features=CalculateNativeWinOcclusion")
    options.add_argument("--disable-notifications")
    options.page_load_strategy='eager'

    # do not image loading
    p={"profile.managed_default_content_settings.images":2,
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
        
        global count
        num=0
        for i in range(1):
            url=f"https://www.naukri.com/jobs-in-india-{i}?clusters=wfhType%2CfunctionalAreaGid&wfhType=2&functionAreaIdGid=14"

            print(f"Opning the target : {url}")
            driver.get(url)
            
            # 4.   Random weating(2 to 4 seconds)
            time.sleep(random.uniform(4, 9))
    
            
             # --- write scrolling (so that be all data load) ---
            for s in range(5): # going to bottom some 5 times 
                driver.execute_script(f"window.scrollBy(0, 800);")
                time.sleep(random.uniform(1,4))

            # human_behavior(driver)

            elem=driver.find_elements(By.CLASS_NAME,'cust-job-tuple')
            for el in elem:
                data=el.get_attribute('outerHTML')
                count+=1

                num=num+1
                with open(f"C:\\Emergent\\webscraping\\scrapers\\Seleniuam scrapers\\Naukri_data\\{num}.html","w",encoding='utf-8') as f:
                     f.write(data)
    
            print(f"Succesful Title : {driver.title}")

        print(f'Total Jobs : {count}')
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
                
# ----------------------------------------------------------------------------------------------------------------------------------------


from bs4 import BeautifulSoup
import pandas as pd

data_list=[]
for i in range(1,20):
    with open(f"C:\\Emergent\\webscraping\\scrapers\\Seleniuam scrapers\\Naukri_data\\{i}.html","r",encoding='utf-8') as f:
         d=f.read()  
         soup=BeautifulSoup(d,'html.parser')
    data_dic={
         'name':soup.find(class_="title").text,
         'review':soup.find('div',class_="row2").text.strip()
         }
    data_list.append(data_dic)

data=pd.DataFrame(data_list)

print(data)

data.to_csv(r'C:\Emergent\webscraping\scrapers\Seleniuam scrapers\\Naukri_data\data.csv', index=False, encoding='utf-8')

print("csv created succesfully")