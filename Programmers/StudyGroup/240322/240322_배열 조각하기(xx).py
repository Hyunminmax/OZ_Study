# 정수 배열 arr와 query가 주어집니다.

# query를 순회하면서 다음 작업을 반복합니다.

# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 
# 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 
# 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
# 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 5 ≤ arr의 길이 ≤ 100,000
# 0 ≤ arr의 원소 ≤ 100
# 1 ≤ query의 길이 < min(50, arr의 길이 / 2)
# query의 각 원소는 0보다 크거나 같고 남아있는 arr의 길이 보다 작습니다.


# ========================================
# 코드는 동작하지만 채점에서 런타임 오류 발생
# ========================================

# 복잡하게 푼 버전
def solution1(arr, query):
    answer = []
    temp = []
    for i in query:
        print('i:',i, '/ answer:', len(answer))
        if len(answer) != 0:
            if i % 2 == 0:
                # 짝수는 뒤
                for j in range(0, i+1):
                    temp.append(answer[j])
                answer = temp.copy()
                print('a1:',temp)
                temp.clear()
            else:
                # 홀수는 앞 
                for j in range(i, len(answer)):
                    temp.append(answer[j])
                # answer = temp.copy()
                answer = temp[:]
                print('b1:',temp)
                temp.clear()
        else:
            if i % 2 == 0:
                # 짝수는 뒤
                for j in range(0, i+1):
                    temp.append(arr[j])
                # answer = temp.copy()
                answer = list(temp)
                print('a2:',temp)
                print('answer:',answer)
                temp.clear()
            else:
                # 홀수는 앞 
                for j in range(i, len(arr)):
                    temp.append(arr[j])
                answer = temp.copy()
                print('b2:',temp)
                print('answer:',answer)
                temp.clear()
    return answer

# 간단하게 푼 버전
def solution2(arr, query):
    answer = []
    for i in query:
        if i % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    answer = list(arr)
    return answer

print(solution1([9,6,3,5,0, 1, 2, 3, 4, 5], [6, 4, 2]))
print(solution2([9,6,3,5,0, 1, 2, 3, 4, 5], [6, 4, 2]))