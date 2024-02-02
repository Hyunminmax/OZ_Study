import pymysql

# db Connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'its_secret.', 
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
cursor = connection.cursor()
# sql = "SELECT * FROM customers"

# CRUD
# 1. SELECT
def get_customers():
    cursor = connection.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers.customerNumber : ", customers['customerNumber'])
    print("customers.customerName : ", customers['customerName'])
    print("customers.country : ", customers['country'])
    cursor.close()

# 2. INSERT INTO
def add_customer():    
    cursor = connection.cursor()
    name = 'hyunmin'
    lastName = 'shin'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({1000}, '{name}', '{lastName}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# 3. UPDATE SET
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_hyunmin'
    contactLastName = 'update_shin'

    sql = f"UPDATE customers SET customerNAME = '{update_name}', contactLastName = '{contactLastName}' WHERE customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
# 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    delete_customerNumber = 1000

    sql = f"DELETE FROM customers WHERE customerNumber = '{delete_customerNumber}'"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()