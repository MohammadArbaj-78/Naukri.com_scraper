from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {
  "http": "http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:{PORT}",
  "https": "http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:{PORT}"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r = requests.get(f'https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANIC1TVhgOZ2Sp-TyqcZhb53t8XnsuIOR2cJiBqUC6SqDB5U0fExAy9hW9e6zlZeQz8RqohuoYT5tl5406JBSlsSrkhre2PRRDVK470kJYEczCBBY4JuQd8EBAb5h1kGF1UkCwdGuOxFgU9g-_jtcrZd4hN193m8jMf6Rl9AfQdn', proxies=proxies, headers=headers, verify=False)

soup=BeautifulSoup(r.text,'html.parser')


symbole=set()

for symbol in soup.find_all('fin-streamer'):
    sm=symbol.get('data-symbol')
    symbole.add(sm)

list_data=list(symbole)

for url in list_data:
    link=f'https://finance.yahoo.com/quote/{url}/history/'

    r = requests.get(link, proxies=proxies, headers=headers, verify=False)

    break

soup=BeautifulSoup(r.text,'html.parser')

t=soup.find('table')
i=t.find_all('tr')

first_row = i[1].find_all('td')

date = first_row[0].text
open_price = first_row[1].text
close_price = first_row[4].text
volume = first_row[6].text

print(f"Date: {date} | Open: {open_price} | Close: {close_price} | Vol: {volume}")
