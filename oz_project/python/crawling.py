from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import pymysql

# 데이터 베이스 연결
# conn = pymysql.connect(
#     host = 'localhost',
#     user='root',
#     password = '0000',
#     db='kream',
#     charset = 'utf8mb4',
#     # cursorclass = pymysql.cursors.DictCursor
# )

# conn.cursor()

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach",True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])
options_.add_argument("--window-size=1000,4500")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options_)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

# #인기수 클릭 및 발매일수 클릭 함수
# def click_p_r():
#     #인기순 클릭
#     driver.find_element(By.CSS_SELECTOR,".sorting_title").click()
#     time.sleep(0.5)
#     #발매일순 클릭
#     driver.find_elements(By.CSS_SELECTOR,".sorting_list")[0].find_elements(By.CSS_SELECTOR,".sorting_item")[9].click()

# # 쿼리문 실행 함수
# def execute_query(conn,query,args=None):
#     with conn.cursor() as cursor:
#         cursor.execute(query,args or ())
#         if query.strip().upper().startswith('SELECT'):
#             return cursor.fetchall()
#         else:
#             conn.commit()            

# #페이지 다운 함수
# def key_down_reload():
#     for i in range(20):
#         driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.5)

# #클래스명이 바뀌어있는지 체크 함수
# def class_c(items):
#     if items:
#         info_items = items
#     else:
#         print("클래스명 확인해주세여")

driver.find_elements(By.CSS_SELECTOR,".gnb_list")[0].find_elements(By.CSS_SELECTOR,".gnb_item")[2].click()
# time.sleep(0.5)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

items = soup.select(".ul_tab > .li_tab")
# for item in items:
#     url = item.select('a.tab');
#     # url = item.select_one('a.tab')['href'];
#     driver.find_elements().click()
#     print(url);
# items = [3,4,5]
for item in items:
    link_c = driver.find_element(By.CLASS_NAME, 'tab').click();
    print(link_c);
    # link_c.click()
    # driver.find_elements(By.CSS_SELECTOR,".ul_tab.ul_search_tab.inline.has_button")[0].find_elements(By.CSS_SELECTOR,".tab_name")[item].click()
    
# driver.quit()
#shop 클릭

# #인기순 클릭 및 발매일순 클릭
# click_p_r()

# #스크롤
# key_down_reload()

# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# items = soup.select(".item_inner")



# #클래스명 체크
# class_c(items)

# #발매일 전체 크롤링
# product_list=[]
# for i in items:
#     #미발매는 크롤링 제외
#     Unsold = i.select_one(".status_value.sale")
#     if Unsold:
#         continue
#     category = "전체"
#     product_brand = i.select_one(".product_info_brand.brand").text #str형
#     product_name = i.select_one(".translated_name").text #str형
#     product_price = i.select_one(".amount").text.split(" ")[1] #str형 공백 제거
    
    
    
#     item = [category,product_brand,product_name,product_price]
#     product_list.append(item)
    
#     for i in product_list:
#         execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))



# #신발 카테고리 선택
# driver.find_elements(By.CSS_SELECTOR,".ul_tab.ul_search_tab.inline.has_button")[0].find_elements(By.CSS_SELECTOR,".tab_name")[3].click()
# time.sleep(0.5)
# #인기순 클릭 및 발매일순 클릭
# click_p_r()

# #스크롤
# key_down_reload()
# time.sleep(2)
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# items = soup.select(".item_inner")


# #클래스명 체크
# class_c(items)


# #발매일 신발 크롤링
# product_Shoes=[]
# for i in items:
#     #미발매는 크롤링 제외
#     Unsold = i.select_one(".status_value.sale")
#     if Unsold:
#         continue
#     category = "신발"
#     product_brand = i.select_one(".product_info_brand.brand").text #str형
#     product_name = i.select_one(".translated_name").text #str형
#     product_price = i.select_one(".amount").text.split(" ")[1] #str형 공백 제거
    
    
    
#     item = [category,product_brand,product_name,product_price]
#     product_Shoes.append(item)

#     for i in product_Shoes:
#         execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))



# #상의 카테고리 선택
# driver.find_elements(By.CSS_SELECTOR,".ul_tab.ul_search_tab.inline.has_button")[0].find_elements(By.CSS_SELECTOR,".tab_name")[4].click()
# time.sleep(0.5)
# #인기순 클릭 및 발매일순 클릭
# click_p_r()

# #스크롤
# key_down_reload()
# time.sleep(2)

# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# items = soup.select(".item_inner")


# #클래스명 체크
# class_c(items)


# #발매일 상의 크롤링
# product_clothes=[]
# for i in items:
#     #미발매는 크롤링 제외
#     Unsold = i.select_one(".status_value.sale")
#     if Unsold:
#         continue
#     category = "상의"
#     product_brand = i.select_one(".product_info_brand.brand").text #str형
#     product_name = i.select_one(".translated_name").text #str형
#     product_price = i.select_one(".amount").text.split(" ")[1] #str형 공백 제거
    
    
    
#     item = [category,product_brand,product_name,product_price]
#     product_clothes.append(item)

#     for i in product_clothes:
#         execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))



# #하의 카테고리 선택
# driver.find_elements(By.CSS_SELECTOR,".ul_tab.ul_search_tab.inline.has_button")[0].find_elements(By.CSS_SELECTOR,".tab_name")[5].click()
# time.sleep(0.5)
# #인기순 클릭 및 발매일순 클릭
# click_p_r()

# #스크롤
# key_down_reload()
# time.sleep(2)
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# items = soup.select(".item_inner")


# #클래스명 체크
# class_c(items)


# #발매일 하의 크롤링
# product_pants=[]
# for i in items:
#     #미발매는 크롤링 제외
#     Unsold = i.select_one(".status_value.sale")
#     if Unsold:
#         continue
#     category = "하의"
#     product_brand = i.select_one(".product_info_brand.brand").text #str형
#     product_name = i.select_one(".translated_name").text #str형
#     product_price = i.select_one(".amount").text.split(" ")[1] #str형 공백 제거
    
    
    
#     item = [category,product_brand,product_name,product_price]
#     product_pants.append(item)

#     for i in product_pants:
#         execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))

# #패션잡화 카테고리 선택
# driver.find_elements(By.CSS_SELECTOR,".ul_tab.ul_search_tab.inline.has_button")[0].find_elements(By.CSS_SELECTOR,".tab_name")[9].click()
# time.sleep(0.5)
# #인기순 클릭 및 발매일순 클릭
# click_p_r()

# #스크롤
# key_down_reload()
# time.sleep(2)
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# items = soup.select(".item_inner")


# #클래스명 체크
# class_c(items)


# #발매일 패션잡화 크롤링
# product_fashion=[]
# for i in items:
#     #미발매는 크롤링 제외
#     Unsold = i.select_one(".status_value.sale")
#     if Unsold:
#         continue
#     category = "패션잡화"
#     product_brand = i.select_one(".product_info_brand.brand").text #str형
#     product_name = i.select_one(".translated_name").text #str형
#     product_price = i.select_one(".amount").text.split(" ")[1] #str형 공백 제거
    
    
    
#     item = [category,product_brand,product_name,product_price]
#     product_fashion.append(item)

#     for i in product_fashion:
#         execute_query(conn,"INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0],i[1],i[2],i[3]))

# driver.quit()
    


