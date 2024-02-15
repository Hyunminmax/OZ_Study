# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
# money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

# 3rd try
def solution(money):
    answer = 0
    #첫집을 터는가 안터는가로 나뉜다.
    #첫집을 털고 시작한다면

    #targetHouse
    tH = [] * len(money)
    #첫집 턴다.
    tH[0] = money[0]
    





    return answer

# 2nd try 틀린 이유는 무조건 한집 건너서 터는 것으로 가정했기때문
def solution(money):
    answer = 0
    # maxSum[0]= 1번째 집부터 턴다.
    # maxSum[1]= 2번째 집부터 턴다.
    # maxSum[2]= 3번째 집부터 마지막집까지 턴다.
    maxSum = [0, 0, 0]
    a, b, c = '', '', ''

    for i in range(len(money)):
        if i % 2 == 0:
            if i != len(money)-1:
                maxSum[0] += money[i]
                a += str(i)+','
            maxSum[2] += money[i]
            c += str(i)+','
            if i == 0:
                maxSum[2] = 0
                c += str(i)+','
        else:
            maxSum[1] += money[i]
            b += str(i)+','
        

    answer = max(maxSum)
    print(answer)
    print(a)
    print(b)
    print(c)

    return answer

# # 1st try 틀린 이유는 무조건 한집 건너서 터는 것으로 가정했기때문
# def solution(money):
#     answer = 0
#     maxSum = [0, 0, 0]
    
#     if len(money) % 2 == 0:
#         for i in range(len(money)):
#             if i % 2 == 0:
#                 maxSum[0] += money[i]
#             else:
#                 maxSum[1] += money[i]
#     else:
#         for i in range(len(money)):
#             if i % 2 == 0:
#                 if i > len(money)-2:
#                     maxSum[2] += money[i]
#                     continue
#                 maxSum[0] += money[i]
#                 maxSum[2] += money[i]
#                 if i == 0:
#                     maxSum[2] = 0
#             else:
#                 maxSum[1] += money[i]

    
#     answer = max(maxSum)
#     print(answer)

#     return answer

solution([10, 10, 500, 500, 200])

# def solution(money):
#     n = len(money)

#     dp1 = [0] * n
#     dp1[0] = money[0]
#     dp1[1] = max(money[0], money[1])
#     for i in range(2, n-1):
#         dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

#     dp2 = [0] * n
#     dp2[0] = 0
#     dp2[1] = money[1]
#     for i in range(2, n):
#         dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

#     return max(dp1[-2], dp2[-1])
# solution([10, 10, 500, 500, 200])