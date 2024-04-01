# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 
# 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.


#첫 아이디어는 가장 큰 수를 모든 다른 값으로 나눌수 있는지 확인하고 
# 안된다면 가장 큰수를 한번씩 더 한 수로 계속 시도한다.
def solution(arr):
    answer = 0
    # 배열 요소 중에서 가장 큰 수 확인
    tempmax = max(arr)
    # 증가시킬 temp에 첫번째 시도를 위해 가장 큰 요소 대입
    temp = tempmax
    # 반복문을 위한 불리언 값으로 하나라도 False면 계속 반복한다.
    whileIf = False
    while whileIf == False:
        # 배열의 요소로 반복문 실행
        for i in arr:
            # temp를 배열 요소 i로 나눈 나머지가 0이 맞으면 다음 요소 진행
            if temp % i== 0:
                whileIf = True
                continue
            # 요소 중 하나라도 나눈 나머지가 0이 아니면 whileIf에 Flase를 대입하고 for문 중단
            else:
                whileIf = False
                break
        # whileIf가 False라면 arr요소중 가장 큰 요소의 배수를 temp에 대입
        if whileIf == False:
            temp += tempmax
        # for문에서 모든 arr 요소로 temp를 나머지 0으로 나눴다면 마지막 테스트가 이뤄진 temp 값을 반환
        else:
            answer = temp
            
    return answer



print(solution([1,2,3]))