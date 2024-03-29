from selenium                           import webdriver
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.common.by       import By
from selenium.webdriver.common.keys     import Keys
from bs4                                import BeautifulSoup
import time

# 각종 옵션 설정
options = Options()
# 유저 정보 넣기
# 데스크탑 정보 넣기
# user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
# 모바일 정보 넣기
user = "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"
options.add_argument(f'user-agent={user}')

# 화면 자동 종료 해제 옵션
options.add_experimental_option('detach', True)
#브라우저 상단에 웹드라이버에 의해 제어되고 있다는 메세지 표시 안하는 옵션
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 옵션 적용
driver = webdriver.Chrome(options=options)

# 크롤링 시작
# 접속하고자하는 사이트 주소 입력
url = 'https://m2.melon.com/index.htm'
driver.get(url)
time.sleep(1)

if driver.current_url != url:
    driver.get(url)

driver.find_element(By.LINK_TEXT,'닫기').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,'멜론차트').click()

#2번째 작은 더보기 버튼 누르기
more_btn = driver.find_elements(By.CSS_SELECTOR, '#moreBtn')[1].click()
#아래 슬립시간이 짧으면 추가 50곡의 정보를 불러오지 못함. 
time.sleep(1)
# 과제 목표
# 노래순위
# 노래제목
# 가수이름
# 추가정보

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

allItems = soup.select('.service_list.list_music > .list_item')

for i in allItems:
    rank = i.select_one('.ranking_num').text
    title = i.select_one('.title.ellipsis').text.strip()
    name = i.select_one('.name.ellipsis').text.strip()
    print()
    print(f'순위 :{rank}')
    print(f'제목 :{title}')
    print(f'가수 :{name}')
    print('===========================================')

# 크롬드라이버 종료
driver.quit()