import requests
from bs4 import BeautifulSoup

# 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

# 월간 리스트에서 상승한 노래만 찾기.
# 접속하려는 주소 입력
url = "https://www.melon.com/chart/month/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 월간 100곡 리스트
# singer = soup.select(".ellipsis.rank01 a")
# title = soup.select(".ellipsis.rank02 a")
# album = soup.select(".ellipsis.rank03 a")

# for rank, i in enumerate(zip(singer, title, album), 1):
#     print(rank)
#     print(f'가수 : {i[0].text}')
#     print(f'제목 : {i[1].text}')
#     print(f'앨범 : {i[2].text}')
#     print("--------------------------------")
