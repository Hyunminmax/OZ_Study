# Python에서 SQL을 사용하도록 pymysql 임포트
import pymysql

# 1. DB에 접속
# 2. 커서 생성
# 3. SQL문 작성
# 4. SELTET면 출력
# 5. CRUD 중에서 R이면 출력 나머지는 connection단에서 commit
# 6. connection 종료

# 1. DB 접속 connection
connection = pymysql.connect(
    host = 'localhost',
    user = 'root', 
    password = 'its_secret.',
    db = 'airbnb', 
    charset = 'utf8mb4', 
    cursorclass = pymysql.cursors.DictCursor
)

# 2. 커서 생성
cursor = connection.cursor()

# 3. SQL문 작성
# 실전연습문제
# - 새로운 제품 추가
def question2_1():
    cursor = connection.cursor()
    # C SQL
    sql = '''INSERT INTO products (productID, productName, price, stockQuantity) VALUES(20, "Min's Python Book", 29.99, 30)'''
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# 고객 목록 조회
def question2_2():
    cursor = connection.cursor()
    # R SQL
    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers_data = cursor.fetchall()
    for row in customers_data:
        print('customer ID :', row['customerID'])
        print('customer Name :', row['customerName'])
        print('customer Email :', row['email'])
        print('customer Add :', row['address'])
        print('customer CreateDate :', row['createDate'])
        print('=======================================')

    cursor.close()

# 제품 재고 업데이트
def question2_3():
    cursor = connection.cursor()
    # U SQL
    sql = "UPDATE products SET stockQuantity = stockQuantity - 1 where productID = %s"
    cursor.execute(sql, 1)
    connection.commit()
    cursor.close()

# 고객별 총 주문 금액 계산
def question2_4():
    cursor = connection.cursor()
    # R SQL
    sql = "SELECT c.customerName, sum(o.totalAmount), c.customerID FROM customers c join orders o on c.customerID = o.customerID GROUP BY c.customerID"
    cursor.execute(sql)
    customersOrderData = cursor.fetchall()
    for row in customersOrderData:
        print('customerID :', row['customerID'])
        print('customerName :', row['customerName'])
        print('TotalOrderAmount :', row['sum(o.totalAmount)'])
        print('=======================================')

    cursor.close()

# 고객 이메일 업데이트
def question2_5():
    cursor = connection.cursor()
    # U SQL
    sql = "UPDATE customers SET email = %s where customerID = %s"
    customerID = input('이메일을 변경할 고객의 ID를 입력하세요.')
    customerEmail = input('새로운 이메일을 입력하세요.')
    
    cursor.execute(sql, (customerEmail, customerID))
    connection.commit()
    cursor.close()

# 주문 취소
def question2_6():
    cursor = connection.cursor()
    # D SQL
    sql = "DELETE FROM orders where orderID = %s"
    
    orderID = input('취소할 OrderID를 입력하세요.')
    cursor.execute(sql, (orderID))
    connection.commit()
    cursor.close()

# 특정 제품 검색
def question2_7():
    cursor = connection.cursor()
    # R SQL
    sql = "SELECT * FROM Products WHERE productName = %s"

    productName = input('제품 이름을 정확하게 입력하세요.')
    cursor.execute(sql, (productName))
    productsData = cursor.fetchall()
    for row in productsData:
        print('productID :', row['productID'])
        print('productName :', row['productName'])
        print('price :', row['price'])
        print('stockQuantity :', row['stockQuantity'])
        print('createDate :', row['createDate'])
        print('=======================================')
    cursor.close()

# 특정 고객의 모든 주문 조회
def question2_8():
    cursor = connection.cursor()
    # R SQL
    sql = "SELECT c.customerID, o.orderID, o.orderDate, o.totalAmount FROM customers c join orders o ON c.customerID = o.customerID WHERE c.customerID = %s"

    customerID = input('제품 이름을 정확하게 입력하세요.')
    cursor.execute(sql, (customerID))
    orderData = cursor.fetchall()
    for row in orderData:
        print('customerID :', row['customerID'])
        print('orderID :', row['orderID'])
        print('orderDate :', row['orderDate'])
        print('totalAmount :', row['totalAmount'])
        print('=======================================')
    cursor.close()

# 가장 많이 주문한 고객 찾기
def question2_9():
    cursor = connection.cursor()
    # R SQL
    sql = "SELECT customerID, customerName FROM customers WHERE customerID =(SELECT customerID FROM orders GROUP BY customerID ORDER BY count(*) DESC limit 1)"

    cursor.execute(sql)
    customerData = cursor.fetchone()
    print(customerData)
    print('customerID :', customerData['customerID'])
    print('customerName :', customerData['customerName'])
    
    cursor.close()
    

# 실전연습문제
# - 새로운 제품 추가
question2_1()
# 고객 목록 조회
question2_2()
# 제품 재고 업데이트
question2_3()
# 고객별 총 주문 금액 계산
question2_4()
# 고객 이메일 업데이트
question2_5()
# 주문 취소
question2_6()
# 특정 제품 검색
question2_7()
# 특정 고객의 모든 주문 조회
question2_8()
# 가장 많이 주문한 고객 찾기
question2_9()