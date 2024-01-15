import pymysql

# (1) db connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='lss018000',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# (2) CRUD

## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()
    
# get_customers()

## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()
    
    name = 'inseoup'
    family_name = 'kim'
    first_name = 'ss'
    phone = '01012341234'
    address1 = 'address1'
    city = 'city1'
    country = 'country1'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country) VALUES({1000}, '{name}', '{family_name}','{first_name}','{phone}', '{address1}', '{city}', '{country}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    
# add_customer()

## 3.UPDATE INTO
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_inseop'
    contactLastName = 'update_kim'
    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    
# update_customer()

## 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    
# delete_customer()