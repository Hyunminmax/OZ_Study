import requests
from bs4 import BeautifulSoup
# request
def readySelect():
    # 접속장비를 모바일로 변경해서 모바일 접속환경을 살펴볼수도 있다. 
    header_user = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

    # 월간 리스트에서 상승한 노래만 찾기.
    # 접속하려는 주소 입력
    url = "https://www.melon.com/chart/month/index.htm"
    req = requests.get(url, headers=header_user)

    # 접속차단을 방지하기 위해 파일을 불러오는 것으로 대체 실패.
    # with open('view-source_https___www.melon.com_chart_month_index.html', 'r', encoding='utf-8') as file: 
    # html_content = file.read()
    # print(html_content)

    html = req.text
    soup = BeautifulSoup(html, "html.parser")


    # 월간 100곡 리스트
    # title = soup.select(".ellipsis.rank01 a")
    # singer = soup.select(".ellipsis.rank02 a")
    # album = soup.select(".ellipsis.rank03 a")

    # for rank, i in enumerate(zip(singer, title, album), 1):
    #     print(rank)
    #     print(f'제목 : {i[0].text}')
    #     print(f'가수 : {i[1].text}')
    #     print(f'앨범 : {i[2].text}')
    #     print("--------------------------------")

    # 월간 100곡 중 순위 상승 곡 리스트
    # 1. 100곡 전체의 리스트
    lst50 = soup.select('.lst50')
    lst100 = soup.select('.lst100')
    allList = lst50 + lst100

    # 2. 각 곡의 요소 추출
    # 현 순위, 전달대비 순위, 제목, 가수, 앨범
    nowRank     = ''#for문으로 allList에서 select_one('.rank ')로 찾아야함.
    # for i in allList:
    #     rank = i.select_one('.rank ')
    #     nowRank = rank.text
    title100    = soup.select('.ellipsis.rank01 a')
    singer100   = soup.select('.ellipsis.rank02 a')
    album100    = soup.select('.ellipsis.rank03 a')
    preRankUp   = soup.select('.bullet_icons.rank_up')      #up 이 태그로 직접 곡정보 전체를 받아오기 어려움.
    preRankDn   = soup.select('.bullet_icons.rank_down')    #down 이 태그로 직접 곡정보 전체를 받아오기 어려움.
    preRankNw   = soup.select('.bullet_icons.rank_new')     #new 이 태그로 직접 곡정보 전체를 받아오기 어려움.
    preRankSt   = soup.select('.bullet_icons.rank_static')  # 이 태그로 직접 곡정보 전체를 받아오기 어려움.
    return allList

# 1. 순위 곡 리스트
def selectAll(allList):
    Cnt = 0
    for i in allList:
        rank    = i.select_one('.rank ')
        nowRank = rank.text
        if i.select_one('.bullet_icons.rank_new') is not None:#순위 진입
            ranktype = i.select_one('.bullet_icons.rank_new')
            preRank = ranktype.text
        elif i.select_one('.bullet_icons.rank_static') is not None:#순위 유지
            ranktype = i.select_one('.bullet_icons.rank_static')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        elif i.select_one('.bullet_icons.rank_down') is not None:#순위 하락
            ranktype = i.select_one('.bullet_icons.rank_down')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        elif i.select_one('.bullet_icons.rank_up') is not None:#순위 상승
            ranktype = i.select_one('.bullet_icons.rank_up')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        title   = i.select_one('.ellipsis.rank01 a')
        singer  = i.select_one('.ellipsis.rank02 a')
        album   = i.select_one('.ellipsis.rank03 a')
        Cnt += 1
        print(f'현 순위 : {nowRank}')
        print(f'순위 변동: {preRank}')
        print(f'제    목: {title.text}')
        print(f'가    수: {singer.text}')
        print(f'앨    범: {album.text}')
        print('===========================================')
    print(f'순위 곡 총: {Cnt}곡')
    print('===========================================')
    print('제공 서비스는 총 6가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')

# 2. 순위 상승 곡 리스트
def selectUp(allList):
    upCnt = 0
    for i in allList:
        rank    = i.select_one('.rank ')
        nowRank = rank.text
        if i.select_one('.bullet_icons.rank_up') is None:
            continue
        else:
            ranktype = i.select_one('.bullet_icons.rank_up')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        title   = i.select_one('.ellipsis.rank01 a')
        singer  = i.select_one('.ellipsis.rank02 a')
        album   = i.select_one('.ellipsis.rank03 a')
        upCnt += 1
        print(f'현 순위 : {nowRank}')
        print(f'순위 변동: {preRank}')
        print(f'제    목: {title.text}')
        print(f'가    수: {singer.text}')
        print(f'앨    범: {album.text}')
        print('===========================================')
    print(f'순위 상승 곡 총: {upCnt}곡')
    print('===========================================')
    print('제공 서비스는 총 6가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')    

# 3. 순위 하락 곡 리스트
def selectDown(allList):
    downCnt = 0
    for i in allList:
        rank    = i.select_one('.rank ')
        nowRank = rank.text
        if i.select_one('.bullet_icons.rank_down') is None:
            continue
        else:
            ranktype = i.select_one('.bullet_icons.rank_down')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        title   = i.select_one('.ellipsis.rank01 a')
        singer  = i.select_one('.ellipsis.rank02 a')
        album   = i.select_one('.ellipsis.rank03 a')
        downCnt += 1
        print(f'현 순위 : {nowRank}')
        print(f'순위 변동: {preRank}')
        print(f'제    목: {title.text}')
        print(f'가    수: {singer.text}')
        print(f'앨    범: {album.text}')
        print('===========================================')
    print(f'순위 하락 곡 총: {downCnt}곡')
    print('===========================================')
    print('제공 서비스는 총 6가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')    

# 4. 순위 유지 곡 리스트
def selectStatic(allList):
    staticCnt = 0
    for i in allList:
        rank    = i.select_one('.rank ')
        nowRank = rank.text
        if i.select_one('.bullet_icons.rank_static') is None:
            continue
        else:
            ranktype = i.select_one('.bullet_icons.rank_static')
            chnRank = ranktype.findNextSibling()
            preRank = chnRank.text + ranktype.text
        title   = i.select_one('.ellipsis.rank01 a')
        singer  = i.select_one('.ellipsis.rank02 a')
        album   = i.select_one('.ellipsis.rank03 a')
        staticCnt += 1
        print(f'현 순위 : {nowRank}')
        print(f'순위 변동: {preRank}')
        print(f'제    목: {title.text}')
        print(f'가    수: {singer.text}')
        print(f'앨    범: {album.text}')
        print('===========================================')
    print(f'순위 유지 곡 총: {staticCnt}곡')
    print('===========================================')
    print('제공 서비스는 총 6가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')    

# 5. 순위 진입 곡 리스트
def selectNew(allList):
    newCnt = 0
    for i in allList:
        rank    = i.select_one('.rank ')
        nowRank = rank.text
        if i.select_one('.bullet_icons.rank_new') is None:
            continue
        else:
            ranktype = i.select_one('.bullet_icons.rank_new')
            preRank = ranktype.text
        title   = i.select_one('.ellipsis.rank01 a')
        singer  = i.select_one('.ellipsis.rank02 a')
        album   = i.select_one('.ellipsis.rank03 a')
        newCnt += 1
        print(f'현 순위 : {nowRank}')
        print(f'순위 변동: {preRank}')
        print(f'제    목: {title.text}')
        print(f'가    수: {singer.text}')
        print(f'앨    범: {album.text}')
        print('===========================================')
    print(f'순위 진입 곡 총: {newCnt}곡')
    print('===========================================')
    print('제공 서비스는 총 6가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')    


# 메뉴 안내    
def menu():
    # 곡전체의 정보 인풋하는 동안 로딩이 되도록 인풋 위에 위치
    allList = readySelect()

    errorCnt = 0
    while errorCnt <= 1:
        orderType = input('선택 메뉴 : ')
        if int(orderType) >= 7 or int(orderType) <= 0:
            errorCnt += 1
            print(f'고르신 메뉴는 {orderType}번으로 메뉴를 잘못 선택하셨습니다. 1~6번 메뉴를 입력해주세요.')
            print('제공 서비스는 총 6가지 입니다.')
            print('1. 월간 Top100 리스트')
            print('2. 순위 상승 곡 리스트')
            print('3. 순위 하락 곡 리스트')
            print('4. 순위 유지 곡 리스트')
            print('5. 순위 진입 곡 리스트')
            print('6. 종료')
            print('메뉴를 입력해주세요.')
        else:
            print(f'고르신 메뉴는 {orderType}번 입니다.')
            if int(orderType) == 1:
                selectAll(allList)
            elif int(orderType) == 2:
                selectUp(allList)
            elif int(orderType) == 3:
                selectDown(allList)
            elif int(orderType) == 4:
                selectStatic(allList)   
            elif int(orderType) == 5:
                selectNew(allList)
            elif int(orderType) == 6:
                print('사용해주셔서 감사합니다.')
                return
    if errorCnt >= 1:
        print('사용법을 다시 확인하시고 이용해주시기 바랍니다.')
    

# 시작 메뉴
def start():
    print('멜론 월간 Top100 서비스에 오신 것을 환영합니다.')
    print('제공 서비스는 총 4가지 입니다.')
    print('1. 월간 Top100 리스트')
    print('2. 순위 상승 곡 리스트')
    print('3. 순위 하락 곡 리스트')
    print('4. 순위 유지 곡 리스트')
    print('5. 순위 진입 곡 리스트')
    print('6. 종료')
    print('메뉴를 입력해주세요.')    
    menu()

        


start()







