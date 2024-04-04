# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록
# solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

# 제한사항
# 0 < polynomial에 있는 수 < 100
#
# polynomial에 변수는 'x'만 존재합니다.
#
# polynomial은 양의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.
#
# 항과 연산기호 사이에는 항상 공백이 존재합니다.
#
# 공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.
#
# 하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.
#
# " + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.
#
# 0으로 시작하는 수는 없습니다.
#
# 문자와 숫자 사이의 곱하기는 생략합니다.
#
# polynomial에는 일차 항과 상수항만 존재합니다.
#
# 계수 1은 생략합니다.
#
# 결괏값에 상수항은 마지막에 둡니다.
#
# 0 < polynomial의 길이 < 50


# 요구하는 표현식으로 모든 리턴이 성공하는데 어디서 실패하는지 파악 실패.
# 2nd try
# def solution(polynomial):
#     answer = ''
#     temp = polynomial.split()
#     temp1 = 0
#     temp2 = 0
#     # print(temp)

#     for i in temp:
#         if i[-1:] == 'x':
#             if len(i) != 1:
#                 temp1 += int(i[:-1])
#             else:
#                 temp1 += 1
#         elif i != '+':
#             temp2 += int(i)
#     if temp2 == 0:
#         answer = str(temp1)+'x'
#     elif temp[0][-1:] == 'x':
#         answer = str(temp1) + 'x + ' + str(temp2)
#     else:
#         answer = str(temp2) + ' + ' + str(temp1) + 'x'

#     return answer

# 준명님 help
def solution(polynomial):
    answer = ''
    temp = polynomial.split()
    temp1 = 0
    temp2 = 0
    for i in temp:
        if i[-1] == 'x':
            if len(i) != 1:
                temp1 += int(i[:-1])
            else:
                temp1 += 1
        elif i != '+':
            temp2 += int(i)
    if temp1 != 0:
        if temp1 > 1:
            answer = str(temp1)
        answer += 'x'
    if temp2 > 0:
        if temp1 > 0:
            answer += ' + '
        answer += str(temp2)

    return answer



# 1st try
# def solution(polynomial):
#     answer = ''
#     temp = polynomial.split()
#     temp1 = 0
#     temp2 = 0
#     print(temp)
#     for i in temp:
#         if i[-1:] == 'x':
#             if len(i) != 1:
#                 temp1 += int(i[:-1])
#             else:
#                 temp1 += 1
#         elif i != '+':
#             temp2 += int(i)
#     if temp2 == 0:
#         answer = str(temp1)+'x'
#     else:
#         answer = str(temp1)+'x + ' + str(temp2)
#
#     return answer


print(solution("3x + 3 + 7 + 3x + 2x + 20 + 45 + 3x + 2x + x"))
