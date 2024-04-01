import requests
from bs4 import BeautifulSoup

# 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

#접속하려는 주소 입력
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

rank01 = soup.select(".ellipsis.rank01 a")
rank02 = soup.select(".ellipsis.rank02 a")
rank03 = soup.select(".ellipsis.rank03 a")

# count = 1
# for i in zip(rank01, rank02, rank03):
#     print(f'순위 : {count}')
#     print(f'제목 :{i[0].text}\n가수 :{i[1].text}\n앨범 :{i[2].text}')
#     print()
#     count += 1
    

for rank, i in enumerate(zip(rank01, rank02, rank03), 1):
    print(f'순위 : {rank}')
    print(f'제목 :{i[0].text}\n가수 :{i[1].text}\n앨범 :{i[2].text}')
    print()
    