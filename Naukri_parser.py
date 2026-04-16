
from bs4 import BeautifulSoup
import pandas as pd
import os

base_dir = os.path.join(os.getcwd(), "data_files")
files = os.listdir(base_dir)

data_list=[]

for file in files:
    file_path = os.path.join(base_dir, file)

    with open(file_path, 'r', encoding='utf-8') as f:
              d = f.read()
    soup=BeautifulSoup(d,'html.parser')
    data_dic={
         'name':soup.find(class_="title").text,
         'review':soup.find('div',class_="row2").text.strip(),
         'Jop_Details':soup.find('div',class_="row3").text
         }
    data_list.append(data_dic)

data=pd.DataFrame(data_list)

print(data)

file_path = os.path.join(base_dir, 'CSV_FILE.csv')

data.to_csv(file_path, index=False, encoding='utf-8')

print("csv created succesfully")