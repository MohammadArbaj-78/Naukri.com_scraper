
from bs4 import BeautifulSoup
import pandas as pd

data_list=[]
for i in range(1,100):
    with open(f"C:\\Emergent\\webscraping\\scrapers\\githab_puch_scrapers\\Naukri.com_scraper\\Data_files\\{i}.html","r",encoding='utf-8') as f:
         d=f.read()  
         soup=BeautifulSoup(d,'html.parser')
    data_dic={
         'name':soup.find(class_="title").text,
         'review':soup.find('div',class_="row2").text.strip(),
         'Jop_Details':soup.find('div',class_="row3").text
         }
    data_list.append(data_dic)

data=pd.DataFrame(data_list)

print(data)

data.to_csv(r'C:\Emergent\webscraping\scrapers\githab_puch_scrapers\Naukri.com_scraper\CSV_FILE.csv', index=False, encoding='utf-8')

print("csv created succesfully")