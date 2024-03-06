# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.
# 2st try
def solution(s):
    answer = ''
    # s 전체를 소문자로 변경하고 ' '으로 잘라 temp에 리스트로 넣는다. 
    temp = s.lower().split(' ')
    print(temp)
    # temp의 인덱스를 반복하며 각 인덱스 값의 첫글자를 대문자로 변경하고 뒤에 공백추가해서 answer에 누적
    for i in range(len(temp)):
        answer += temp[i].capitalize() + ' '
    # 누적 된 answer의 시작부터 마지막 공백전까지의 값을 다시 answer에 넣는다.
    answer = answer[:-1]
    print(answer)
    return answer

solution("3people   unFollowed     me")