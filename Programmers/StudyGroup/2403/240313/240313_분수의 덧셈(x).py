# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 
# solution 함수를 완성해보세요.

# 제한사항
# 0 <numer1, denom1, numer2, denom2 < 1,000

def solution(numer1, denom1, numer2, denom2):
    answer = []
    cnt = 1

    if denom1 > denom2:
        big_num = [denom1, numer1]
        small_num = [denom2, numer2]
    else:
        big_num = [denom2, numer2]
        small_num = [denom1, numer1]

    while big_num[0] % small_num[0] != 0:
        big_num[0] += big_num[0]
        cnt += 1

    if cnt == 1 and big_num[0] % small_num[0] == 0:
        print(big_num[0], small_num[0])
    
    return cnt



print(solution(9,2,1,3))