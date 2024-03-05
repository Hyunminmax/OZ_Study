import  yaml
import  mysql.connector

# DB접속정보 Load
db_info = yaml.load(open('H:/My Drive/InBox/000000OZ/OZ_Study/ETC/Database/db_oz.yaml'), Loader=yaml.FullLoader)

# 5문제 출제를 위한 SELECT문
def selectDB(cursor, questions):
    ids = []
    results = []
    for i in range(1, questions+1):
        if i < 3:
            selectSQL = 'select id, level, title, ratio, link from study_group where solved = 0 and level = 0 '
        elif i > 2 and i < 5:
            selectSQL = 'select id, level, title, ratio, link from study_group where solved = 0 and level = 1 '
        else:
            selectSQL = 'select id, level, title, ratio, link from study_group where solved = 0 and level = 2 '
        
        if i % 2 != 0:
            selectSQL += 'order by ratio DESC limit 1'
        else:
            selectSQL += 'order by ratio ASC limit 1'
        cursor.execute(selectSQL)
        results.append(cursor.fetchall())
    
    temp = '9'
    
    for i in results:
        for j in i:
            ids.append(j[0])
            if j[1] != temp:
                print(f'==========={j[1]} 단계 문제===========')
                temp = j[1]
            print(j[2])
            print(j[4])
    
    return ids

# DB에서 SELECT했던 ROW들 UPDATE
def updateDB(cursor, connectDB, dataSet):
    
    for i in dataSet:
        updateSQL = f'update study_group set solved = 1 where id ={i}'
        cursor.execute(updateSQL)
    connectDB.commit()

# DB연결
def connectDB():
    connectDB = mysql.connector.connect(
        host = db_info['mysql_host'],
        user = db_info['mysql_user'], 
        password = db_info['mysql_password'],
        database = db_info['mysql_db']
    )
    cursor = connectDB.cursor()
    return cursor, connectDB


# DB연결
cursor, connectDB = connectDB()

# SELECT 조건 설정
questions = 5

# SELECT문 호출
updateTarget = selectDB(cursor, questions)
updateDB(cursor, connectDB, updateTarget)