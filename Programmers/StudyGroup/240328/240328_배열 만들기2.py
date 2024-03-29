# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를
# 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
#
# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.
#
# 제한사항
# 1 ≤ l ≤ r ≤ 1,000,000



def solution(l, r):
    answer = []
    for i in range(l, r+1):
        temp = True
        if i % 5 == 0:
            if len(str(i)) == 1:
                answer.append(i)
            else:
                for j in range(len(str(i))):
                    if str(i)[j] not in ['5','0']:
                        temp = False
                if temp:
                    answer.append(i)
    if len(answer) == 0:
        answer.append(-1)

    return answer


print(solution(10, 20))
