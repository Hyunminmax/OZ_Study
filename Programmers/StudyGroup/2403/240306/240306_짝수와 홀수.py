# 문제 설명
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# 일반식
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = "Odd"
    return answer

# 람다식 삼항 연산자
# 삼항 연산자는 Python에서 다음과 같은 형식을 가집니다: A if condition else B, 
# 여기서 condition이 참이면 A를, 거짓이면 B를 반환합니다.
solution = lambda num : "Even" if num % 2 == 0 else "Odd"
