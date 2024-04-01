# 문자열 str1, str2가 매개변수로 주어집니다. 
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ str1의 길이 ≤ 100
# 1 ≤ str2의 길이 ≤ 100
# 문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.

# 1st try
def solution(str1, str2):
    answer = 1 if str2 in str1 else 2
    # answer = 0
    # if str2 in str1:
    #     answer = 1
    # else :
    #     answer = 2
    print(answer)
    return answer

solution("ppprrrogrammers","pppp")