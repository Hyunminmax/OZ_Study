import requests
from bs4 import BeautifulSoup

# 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

#접속하려는 주소 입력
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
serch_url = input("검색어를 입력해주세요 : ")

url = base_url + serch_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

title = soup.select(".title_area")
user_box = soup.select(".user_box_inner")
author = soup.select(".user_info > a")
link = soup.select(".title_area > a")

for i in zip(title, author):
    print(f'Title: {i[0].text}\nAuthor: {i[1].text}\nLink: {i[0].a["href"]}')
    print()
