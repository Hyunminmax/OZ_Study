import random
import mysql.connector
from faker import Faker

# (1)MySQL 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'its_secret.',
    database = 'OZ'
)

# (2) MySQL 연결
cursor = db_connection.cursor()
faker = Faker()

# # users table에 100개의 user 데이터 생성
# for _ in range(100):
#     username = faker.user_name()
#     email = faker.email()

#     sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
#     values = (username, email)
    
#     cursor.execute(sql, values)

# user_id 불러오기
cursor.execute("SELECT user_id from users")
valid_user_id = [row[0] for row in cursor.fetchall()]

# orders table에 100개의  데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)
        
        cursor.execute(sql, values)
    except:
        print("aa")
        pass


db_connection.commit()
cursor.close()
db_connection.close()