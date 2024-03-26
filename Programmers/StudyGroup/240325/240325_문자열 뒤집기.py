# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000

# tabnine 에서 자동완성으로 답을 봐서 그 답을 피해서 다시 작성.

def solution(my_string):
    temp = list(my_string)
    temp.reverse()
    answer = ''
    for i in temp:
        answer += i
    return answer


print(solution("jaron"))