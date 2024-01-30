from selenium                           import webdriver
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.common.by       import By
from selenium.webdriver.common.keys     import Keys
from bs4                                import BeautifulSoup
import time

# 각종 옵션 설정
options = Options()
# 유저 정보 넣기
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
options.add_argument(f'User-Agent={user}')
# 화면 자동 종료 해제 옵션
options.add_experimental_option('detach', True)
#브라우저 상단에 웹드라이버에 의해 제어되고 있다는 메세지 표시 안하는 옵션
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 옵션 적용
driver = webdriver.Chrome(options=options)

# 크롤링 시작
# 접속하고자하는 사이트 주소 입력
url = 'https://kream.co.kr'
driver.get(url)

# 사이트 접속
# 돋보기 클릭
# '슈프림' 검색
# 스크롤다운
# 후드만 스크랩 with 스크린샷

driver.find_element(By.CSS_SELECTOR, '.btn_search').click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys('슈프림')
time.sleep(0.8)
driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(0.2)
