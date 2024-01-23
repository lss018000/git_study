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
with connection.cursor() as cursor:
    # # 문제8 : 특정 고객의 주문 데이터 조회
    sql1 = "SELECT cat_no FROM product_cat "
    cursor.execute(sql1)
    datas = cursor.fetchall()

    for data in datas:
        # print('a')
        genders = ['kids','men','women'];
        # data_types = [];
        for gender in genders:
            # print(gender);
            cat_no = data['cat_no'];
            cat_url = 'https://kream.co.kr/search?gender=' + gender + '&tab=' + cat_no;
            # print(cat_url)

            driver.get(cat_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = soup.select('div.search_result_list > div.search_result_item')
            # print(products);
            # array_row = []
            if products:
                for product in products:
                    url = product.find('a')['href']
                    brand = product.select_one('div.product_card > a > .product_info_area > .title > .brand').text
                    name = product.select_one('div.product_card > a > .product_info_area > .title > .product_info_product_name > .translated_name').text
                    name_en = product.select_one('div.product_card > a > .product_info_area > .title > .product_info_product_name > .name').text
                    price = product.select_one('div.product_card > a > .price_area > .amount').text  
                    # print(url)      
                        
                    # # with connection.cursor() as cursor:
                    sql2 = "INSERT INTO products (category, brand, gender, product_name, product_name_en, price, kream_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql2, (cat_no, brand, gender, name, name_en, price, url))
                    connection.commit()
cursor.close()
driver.quit()