import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='lss018000',
    db='kream',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://kream.co.kr/search")
soup = BeautifulSoup(driver.page_source, 'html.parser')
cat_list = soup.select('nav.pc_shop_tab > div.tabs > ul.ul_search_tab > li.li_search_tab')
print(cat_list)
for cat in cat_list:
    url = cat.select_one('a.tab')['href'];
    cat_no = url.replace('/search?tab=', '')
    name = cat.select_one('a.tab > span.tab_name').text

    
    print(url);
    if url != '/search':
        if cat_no != '43':
            with connection.cursor() as cursor:
                print(name);
                # # 문제1 : 새로운 제품 추가
                sql = "INSERT INTO product_cat (cat_no, cat_name) VALUES (%s, %s)"
                # print(cat_name)
                cursor.execute(sql, (cat_no, name))
                connection.commit()
            cursor.close()

driver.quit()