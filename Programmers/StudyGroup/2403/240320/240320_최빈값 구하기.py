# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000


def solution(array):
    answer = 0
    temp_dict={}
    temp_dict = temp_dict.fromkeys(array, 0)
    for i in array:
        if temp_dict[i]!= None:
            temp_dict[i]+=1
    temp_dict = sorted(temp_dict.items(), key=lambda item: item[1], reverse=True)
    if len(temp_dict) > 1:
        if temp_dict[0][1] == temp_dict[1][1]:
            answer = -1
        else:
            answer = temp_dict[0][0]
    else:
        answer = answer = temp_dict[0][0]
    
    return answer

print(solution([232,214,123,6,0,232]))