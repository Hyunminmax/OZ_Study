# 카카오 성격유형은 RT, CF, JM, AN의 4쌍을 이루는 각 원소의 조합으로 총 16가지 (2*2*2*2)가 나올수 있다. 
# RFMA, TFJN과 같은 형식으로 나올수 있다. 
# 질문 survey는 1~1000개 사이이고 질문 원소는 'RT', 'TR', 'FC', 'CF', 'MJ', 'JM', 'AN', 'NA' 중에 하나이다. 
# survey[i]의 첫 케릭터는 질문의 비동의, 두번째 케릭터는 동의를 해야 점수를 받는다. 
# survey = ['RT', 'FC'] 라면 첫 질문의 답변이 1 매우 비동의(3점), 두번째 질문의 답변이 6 동의(2점)이라면 
# 'R'은 3점, 'C'는 2점을 받은 상황이다. 
# 각 답변의 점수는 비동의 = 1(3점), 2(2점), 3(1점) / 모르겠음(점수 없음) / 동의 4(1점), 5(2점), 6(3점)
# 각 점수를 누적해
# R : 3 // T : 4
# C : 3 // F : 2
# J : 5 // M : 5
# A : 7 // N : 7
# 위와 같은 경우 성격 유형은 "TCJA"이다. 점수가 동점인 경우 알파뱃 우선으로 선택한다.

# 도전 : survey와 choices를 zip으로 묶어 세트로 구성한다. survey 요소 하나에 choices 하나씩 세트로 구성하여 
# 각 질문에 대한 점수를 구성한다.




# 1st try
def solution(survey, choices):
    answer = ''
    # 성격유형 판정을 위한 순서
    kind = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    #각 성격 유형의 채점용 딕셔너리 생성
    score = {}
    for i in survey:
        print(i)
        score[i[0]] = 0
        score[i[1]] = 0

    # print(score)
    # {'A': '', 'N': '', 'C': '', 'F': '', 'M': '', 'J': '', 'R': '', 'T': ''}            
    # for문 한번에 처리하기 위한 리스트 병합       
    data = list(zip(survey, choices))
    # print(data)
    # [('AN', 5), ('CF', 3), ('MJ', 2), ('RT', 7), ('NA', 5)]
    
    # 채점 진행
    for i in data:
        if i[1] == 1:
            score[i[0][:1]] += 3
        elif i[1] == 2:
            score[i[0][:1]] += 2
        elif i[1] == 3:
            score[i[0][:1]] += 1
        elif i[1] == 5:
            score[i[0][1:]] += 1
        elif i[1] == 6:
            score[i[0][1:]] += 2
        elif i[1] == 7:
            score[i[0][1:]] += 3
    
    # print(score)
    # {'A': 1, 'N': 1, 'C': 1, 'F': 0, 'M': 2, 'J': 0, 'R': 0, 'T': 3}

    # 성격분석
    for i in kind:
    # 질문이 없으면 성격 종류중에 앞 성향 선택
        if i[0] not in score:
            answer += i[0]
            # 점수가 같으면 성격 종류중에 앞 성향 선택
        elif score[i[0]] == score[i[1]]:
            answer += i[0]
        else:
            # 점수가 뒷 성향이 높으면 뒷 성향 선택
            if score[i[0]] < score[i[1]]:
                answer += i[1]
                # 점수가 뒷 성향이 높지 않으면 앞 성향 선택
            else:
                answer += i[0]
            
    print(answer)

    return answer

solution(["TR", "RT", "TR"], 	[7, 1, 3])