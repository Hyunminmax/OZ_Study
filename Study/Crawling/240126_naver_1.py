import requests
from bs4 import BeautifulSoup

#접속하려는 주소 입력
url = "https://www.naver.com"

# get 방식으로 서버에게 Resource(자원=html,css,js)을 보내도록 요청한다. 데이터 수신이 가능하게 된다.
# requests는 거의 처음에만 사용되고 이우에는 잘 사용되지 않음, 이유는 정적인 사이트에서는 html 코드가 변하지 않기 때문이다.
# requests로 넘어오는 내용은 예를 들어 네이버의 화면에서 페이지 소스보기를 한 내용과 같다.
req = requests.get(url)

# get 방식을 통해서 가져온 많은 데이터 중 우리가 필요한건 텍스트 형태의 자료다(가장 중요한 html이 포함되어있다.)
html = req.text

# BeautifulSoup이라는 함수에는 2가지 파라미터를 넣는데. html, html.parser를 넣는다. 넣으면 파서(컴퓨터가 html을 이해하도록)가 진행된다.
soup = BeautifulSoup(html, "html.parser")

# select_one 원하는 태그를 찾을 수 있는데 기준은 클래스명, id, 태그도 가능하다. 앞에다 클레스는 '.', id는 '#'을 붙인다.
query = soup.select_one("#query")
print(query)