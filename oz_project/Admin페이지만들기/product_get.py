import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

data_types = [
    ['https://kream.co.kr/search?gender=&shop_category_id=64', '64', ''], #상의
    ['https://kream.co.kr/search?gender=men&shop_category_id=64', '64', 'men'], #상의 남자
    ['https://kream.co.kr/search?gender=women&shop_category_id=64', '64', 'women'], #상의 남자
    ['https://kream.co.kr/search?gender=&shop_category_id=65', '65', ''], #하의
    ['https://kream.co.kr/search?gender=men&shop_category_id=65', '65', 'men'], #하의 남자
    ['https://kream.co.kr/search?gender=women&shop_category_id=65', '65', 'women'], #하의 여자
    ['https://kream.co.kr/search?gender=&shop_category_id=34', '34', ''], #신발
    ['https://kream.co.kr/search?gender=men&shop_category_id=34', '34', 'men'], #신발 남자
    ['https://kream.co.kr/search?gender=women&shop_category_id=34', '34', 'women'], #신발 여자
    ['https://kream.co.kr/search?gender=&shop_category_id=7', '7', ''], #패션잡화
    ['https://kream.co.kr/search?gender=men&shop_category_id=7', '7', 'men'], #패션잡화 남자
    ['https://kream.co.kr/search?gender=women&shop_category_id=7', '7', 'women'] #패션잡화 여자
]

for data_type in data_types:
    search_url = data_type[0];
    print(search_url);
    driver.get(search_url)
    # driver.get("https://kream.co.kr/search?tab=43")
    data_name ='kream_data_'+data_type[1]+'_'+data_type[2];
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    products = soup.select('div.search_result_list > div.product_card')
    array_row = []
    for product in products:
        url = product.find('a')['href'];
        brand = product.select_one('a > .product_info_area > .title > .brand').text
        name = product.select_one('a > .product_info_area > .title > .product_info_product_name > .translated_name').text
        price = product.select_one('a > .price_area > .amount').text
        if data_type[1] == '64':
            cat_name = '상의';
        elif data_type[1] == '65':
            cat_name = '하의';
        elif data_type[1] == '34':
            cat_name = '신발';
        elif data_type[1] == '7':
            cat_name = '패션잡화';
            
        if data_type[2] == 'men':
            sex_val = '남자';
        elif data_type[2] == 'women':
            sex_val = '여자';   
        else:
            sex_val = '남자/여자';         
            

        
        row = {
            'category': cat_name,
            'brand': brand,
            'sex': sex_val,
            'product': name,
            'price': price,
            'url': url,
        }
        array_row.append(row) 
    file_path = './oz_project/Admin페이지만들기/json_data/'+data_name+'.json'
    with open(file_path, 'w') as f:
        json.dump(array_row, f)
driver.quit()