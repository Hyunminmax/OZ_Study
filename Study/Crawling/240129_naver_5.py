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

areas = soup.select(".view_wrap")

for i in areas:
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else:
        title = i.select_one(".title_link._cross_trigger")
        author = i.select_one(".user_info > a")
        print(f'제목: {title.text}')
        print(f'작성자: {author.text}')
        print(f'링크: {title["href"]}\n')