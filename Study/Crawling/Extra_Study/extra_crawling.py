# 추가 연습: 크롤링, DB Insert

# 목표사이트 OZ코딩스쿨 지원절차의 FAQ, 선발기준(notion)

from    bs4                             import  BeautifulSoup
from    selenium                        import  webdriver
# from    selenium.webdriver.common.by    import  By
import  time
import  pymysql
import  mysql.connector

#오즈코딩스쿨 접속
def connectURL(siteUrl):
    driver = webdriver.Chrome()
    driver.get(siteUrl)
    return driver

# 셀레니움 방식
# promotion = driver.find_element(By.CLASS_NAME, 'promotion_list')
# time.sleep(2)
# item = promotion.find_elements(By.CLASS_NAME, 'promotion_item')[2]
# # 지원절차 URL 탐색
# target = item.find_elements(By.CLASS_NAME, 'link-item')[0].get_attribute('href')
# print('지원절차:', target)

# driver.get(target)
# faqLists = driver.find_element(By.ID, 'qaList')
# fLists = faqLists.find_elements(By.CLASS_NAME, 'qa_q.bottom-text-l')
# print(fLists[1].text)
# temps = faqLists.find_elements(By.CLASS_NAME, '.qa_box.bottom-text-m' > '.flex' > '.qa_a')
# print(type(temps))
# print(temps)

#BeautifulSoup 방식
def crawling(driver):
    faqs = []
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #FAQ리스트
    qLists = soup.select('#qaList > .qa_item > .flex > .qa_q.bottom-text-l')
    aLists = soup.select('#qaList > .qa_item > .qa_box.bottom-text-m > .flex > div:nth-of-type(2)')
    for i in range(len(qLists)):
        faqs.append([qLists[i].text, aLists[i].text])


    # 노션
    #선발기준 URL
    # temp = soup.select('.b_tt.text4.bold')[1]
    # recruitURL = temp.select_one('a')['href']

    #선발기준으로 이동
    # driver.get(recruitURL)
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # tableItems = soup.select('.notion-table-row')


    # category = soup.select('.notion-table-row > th > div')
    # detail = soup.select('.notion-table-row > td > div > div')
    # print(dir(category))
    # print(qLists[0].text)
    # print(aLists[0].text)
    # print(category[0])
    # print(detail[0])
    driver.close()
    return faqs


def connectDB():
    connectDB = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'its_secret.',
        database = 'oz'
    )
    cursor = connectDB.cursor()
    return cursor, connectDB

def insertDB(cursor, conn, data):
    insertSQL = 'insert into crawling_oz(category_name,category_detail) values(%s,%s)'
    print('=====')
    print(data)
    print('=====')
    for i in data:
        cursor.execute(insertSQL, (i[0], i[1]))
    conn.commit()
    

siteUrl = 'https://ozcodingschool.com/ozcoding/startupcamp'

target = connectURL(siteUrl)
data = crawling(target)

cursor, conn = connectDB()
insertDB(cursor, conn, data)