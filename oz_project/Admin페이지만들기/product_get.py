import requests
from bs4 import BeautifulSoup
import pandas as pd

resp = requests.get('https://kream.co.kr/search?tab=43')
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
products = soup.select('.search_result_list div')

cat = [] # Category
brand = [] #brand
title = [] #title
price = [] #price

for n in products:
    cat.append(n.text)
    brand.append(n['href'])
    
df = pd.DataFrame()
df['제목'] = cat
df['url'] = brand

df.to_excel('test.xlsx', index = False);
