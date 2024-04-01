# score 배열이 주어지면 각 인덱스별 length만큼 큰수 정렬
# 각 인덱스길이 만큼 큰수 정렬된 배열에서 k만큼 추출해서 가장 낮은 점수를 반환
# 입출력 예) 
# 입력 k= 3, score = [10, 100, 20, 150, 1, 100, 200]
# 출력 answer = [10, 10, 10, 20, 20, 100, 100]

def solution(k, score):
    # 계산용, 답안용 배열 선언
    temp = []
    answer = []
    # score의 값을 하나씩 계산용 배열에 넣으면서 오름차순 정렬
    # k의 값보다 배열의 길이가 짧거나 같다면 0번 인덱스를 answer배열에 추가
    # k의 값보다 배열이 길이가 길다면 k만큼 뺀 인덱스의 값을 answer배열에 추가
    for i in range(len(score)):
        temp.append(score[i])
        temp.sort()
        if len(temp) <= k:
            answer.append(temp[0])
        else:
            answer.append(temp[len(temp)-k])
    
    print(answer)
    return answer




solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])