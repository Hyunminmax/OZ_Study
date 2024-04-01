from selenium                           import webdriver
from selenium.webdriver.chrome.options  import Options
import time

options = Options()

# 각종 옵션 설정
# 유저 정보 넣기
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
options.add_argument(f'User-Agent={user}')

# 화면 자동 종료 해제 옵션
options.add_experimental_option('detach', True)
# 화면 크기 최대 설정
# options.add_argument('--start-maximized')
# F11과 같은 전체화면
# options.add_argument('--start-maximized')
# 화면 크기 지정
# options.add_argument('window-size=500, 500')
# 브라우저 화면이 나오지 않은 상태에서 크롤링 작업하게 만들어주는 옵션
# options.add_argument('--headLess')

#브라우저 상단에 웹드라이버에 의해 제어되고 있다는 메세지 표시 안하는 옵션
# options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 음소거 모드
# options.add_argument('--mute-audio')
# 시크릿 모드
# options.add_argument('incognito')



# 옵션 적용
driver = webdriver.Chrome(options=options)

# 접속하고자하는 사이트 주소 입력
url = 'https://naver.com'
driver.get(url)
time.sleep(1)