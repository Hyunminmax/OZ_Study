# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

solution3 = lambda arr: sum(arr) / len(arr)


def solution1(arr):
    answer = 0
    for i in arr:
        answer += int(i)
    answer = answer / len(arr)
    return answer

def solution2(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    print(answer)
    return answer

solution3([1,2,3,4])