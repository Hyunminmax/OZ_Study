import requests
from bs4 import BeautifulSoup

# 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

#접속하려는 주소 입력
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
serch_url = input("검색어를 입력해주세요 : ")
url = base_url + serch_url

req = requests.get(url, headers=header_user)

html = req.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".keyword_box_wrap.type_color")

for i in titles:
    name = i.select_one(".name.elss")
    category = i.select_one(".etc_area")
    title = i.select_one(".title_link._cross_trigger._foryou_trigger")
    print(f"블로그 작성자는 :{name.text}")
    print(f"블로그 카테고리는 :{category.text}")
    print(f"글 제목 :{title.text}")
    print()