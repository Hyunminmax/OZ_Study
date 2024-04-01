# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10,000
# 1 ≤ numlist의 원소 ≤ 10,000
# 1 ≤ numlist의 길이 ≤ 100
# numlist는 중복된 원소를 갖지 않습니다.

# 2nd try
def solution(numlist, n):
    answer = []
    numlistDict = {}
    for i in numlist:
        numlistDict[i] =  abs(i-n)
    
    numlistDict = sorted(numlistDict.items(), key = lambda item: (item[1], -item[0]))
    for i in numlistDict:
        answer.append(i[0])



# 1st try
# def solution(numlist, n):
#     answer = []
#     numlistDict = {}
#     for i in numlist:
#         numlistDict[i] =  abs(i-n)
#     numlistDict = sorted(numlistDict.items(), key = lambda item: item[1])
#     print(numlistDict)
#     if len(numlistDict) == 1:
#         answer.append(numlistDict[0][0])
#     elif len(numlistDict) > 1:
#         for i in range(1, len(numlistDict)):
#             print('i-1:', numlistDict[i-1][0], 'i:', numlistDict[i][0])
#             if numlistDict[i-1][1] != numlistDict[i][1]:
#                 answer.append(numlistDict[i-1][0])
#                 print("a")
#             else:
#                 answer.append(numlistDict[i][0])
#                 print("B")
#                 answer.append(numlistDict[i-1][0])
#                 print("c")
    
    
    
    return answer


print(solution([10000,20,36,47,40,6,10,7000], 30))