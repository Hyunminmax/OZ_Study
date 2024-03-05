from    bs4         import  BeautifulSoup
from    selenium    import  webdriver
import  mysql.connector
import  time
import  yaml

#webDriver
def connectURL(URL):
    driver = webdriver.Chrome()
    driver.get(URL)
    return driver

# Level별 첫페이지 URL
def putURL(languages, level):
    siteURL = 'https://school.programmers.co.kr/learn/challenges?order=acceptance_desc'
    siteURL += '&languages=' + languages
    siteURL += '&levels=' + level
    siteURL += '&page=1'
    return siteURL

# 최대 목표 Level 설정
def maxLevel(maxLevel):
    siteURL = []
    for i in range(maxLevel+1):
        siteURL.append(putURL('python3', str(i)))
    return siteURL

# 각 문제의 링크 크롤링
def crawlingURL(siteURL, cursor, connectDB):
    for i in siteURL:
        dataSet = []
        driver = connectURL(i)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'html.parser')
        maxNum = soup1.select_one('.Statusstyle__StatusStyled-sc-tdk15-0.fefBMm > .total > .text').get_text().split()[0]
        if int(maxNum) < 20:
            maxPages = 0
        else:
            maxPages = int(int(maxNum) / 20)
        for j in range(1, maxPages+2):
            if j == 1:
                targetRows1 = soup1.select('.ChallengesTablestyle__Table-sc-wt0ety-4.jWXzEP > tbody > tr')
                for k in targetRows1:
                    link = 'https://school.programmers.co.kr/'
                    link += k.select_one('.bookmark > a')['href']
                    title = k.select_one('.bookmark > a').get_text()
                    level = k.select_one('.level').get_text().split(' ')[1]
                    ratio = k.select_one('.acceptance-rate').get_text().replace('%','')
                    dataSet.append([link, title, level, ratio])
            else:
                driver2 = connectURL(i[:-1]+str(j))
                html2 = driver2.page_source
                soup2 = BeautifulSoup(html2, 'html.parser')
                targetRows2 = soup2.select('.ChallengesTablestyle__Table-sc-wt0ety-4.jWXzEP > tbody > tr')
                for k in targetRows2:
                    link = 'https://school.programmers.co.kr/'
                    link += k.select_one('.bookmark > a')['href']
                    title = k.select_one('.bookmark > a').get_text()
                    level = k.select_one('.level').get_text().split(' ')[1]
                    ratio = k.select_one('.acceptance-rate').get_text().replace('%','')
                    dataSet.append([link, title, level, ratio])
            time.sleep(1)
        # DB에 정보전달
        insertDB(cursor, connectDB, dataSet)
    connectDB.close()

#  DB로 insert
def insertDB(cursor, connectDB, dataSet):
    insertSQL = 'insert into study_group(link, title, level, ratio) values(%s,%s,%s,%s)'
    print('=====')
    print(dataSet)
    print('=====')
    for i in dataSet:
        cursor.execute(insertSQL, (i[0], i[1], i[2], i[3]))
    connectDB.commit()

# DB접속정보 Load
db_info = yaml.load(open('H:/My Drive/InBox/000000OZ/OZ_Study/ETC/Database/db_oz.yaml'), Loader=yaml.FullLoader)

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

# 각 레벨의 첫페이지 URL 설정
siteURL = maxLevel(2)
crawlingURL(siteURL, cursor, connectDB)
