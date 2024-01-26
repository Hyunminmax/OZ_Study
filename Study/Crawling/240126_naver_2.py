import requests
from bs4 import BeautifulSoup

# 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

#접속하려는 주소 입력
url = "https://www.naver.com"

req = requests.get(url, headers=header_user)

print(req.request)
