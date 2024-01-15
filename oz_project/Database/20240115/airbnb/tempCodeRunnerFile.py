 문제1 : 새로운 제품 추가
    # sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # connection.commit()
    
    # # 문제2 : 고객 목록 조회
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall():
    #     print(book)
        
    # # 문제3 : 제품 제고 업데이트
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql,(1, 1))
    # connection.co