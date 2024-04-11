# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers의 길이 ≤ 100

def solution(numbers):
    answer = 0
    numbers.sort()
    numbers.reverse()
    answer = numbers[0] * numbers[1]
    return answer

print(solution([0, 31, 24, 10, 1, 9]))