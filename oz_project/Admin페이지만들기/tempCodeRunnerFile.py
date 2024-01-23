
            # driver.get(cat_url)
            # soup = BeautifulSoup(driver.page_source, 'html.parser')
            # products = soup.select('div.search_result_list > div.product')
            # array_row = []
            # for product in products:
            #     url = product.find('a')['href'];
            #     brand = product.select_one('a > .product_info_area > .title > .brand').text
            #     name = product.select_one('a > .product_info_area > .title > .product_info_product_name > .translated_name').text
            #     name_en = product.select_one('a > .product_info_area > .title > .product_info_product_name > .name').text
            #     price = product.select_one('a > .price_area > .amount').text        
                    
            #     # with connection.cursor() as cursor:
            #     sql2 = "INSERT INTO products (category, brand, gender, product_name, product_name_en, price, kream_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            #     cursor.execute(sql2, (cat_no, brand, gender, name, name_en, price, url))
            #     connection.commit()