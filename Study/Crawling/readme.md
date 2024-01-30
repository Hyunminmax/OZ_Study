# Crawling 연습을 진행한 코드들 입니다.
- 24/01/26일 Requests, BeautifulSoup 설치 및 네이버 접속, 뉴스 검색

## Melon Mini Project
- 월간 차트에서 순위 상승한 곡 정보만 가져오기
  - 지속적인 리퀘스트로 차단 방지를 위해 html을 내려 받아 연습하려 했지만 실패
- request 최소화를 위한 request함수화
  - readySelect()
- 월간 차트 순위 전체 리스트
  - selectAll()
- 월간 차트 순위 상승 리스트
  - selectUp()
- 월간 차트 순위 하락 리스트
  - selectDown()
- 월간 차트 순위 유지 리스트
  - selectStatic()
- 월간 차트 순위 진입 리스트
  - selectNew()
- 메뉴 안내
  - menu()
- 시작 메뉴
  - start()


## Melon Mini Project 절차
    1. start() : 사용법 안내 및 메뉴 선택, 오류 지속시 종료
    2. menu() : readySelect()를 호출하고 메뉴를 보여줌.
                먼저 호출하고 보여주는 이유는 로딩시간을 줄이기 위해.
    3. readySelect() : request 1번으로 모든 메뉴를 이용할 수 있도록 request 결과를 저장
    4. 1~6번 메뉴를 선택
       1. 월간 Top100 전체 곡 리스트
       2. 월간 Top100 순위 상승 곡 리스트
       3. 월간 Top100 순위 하락 곡 리스트
       4. 월간 Top100 순위 유지 곡 리스트
       5. 월간 Top100 순위 진입 곡 리스트
       6. 종료
    5. 메뉴에 없는 번호를 지속 선택시 서비스 종료

## 버그
    - 한 곡의 가수가 2명 이상인 경우 가수명을 첫번째 1명만 읽어옴.

## 기능개선 예정
  - 조회 함수들을 인자값을 받아 각각의 동작을 하는 하나의 함수로 합칠예정