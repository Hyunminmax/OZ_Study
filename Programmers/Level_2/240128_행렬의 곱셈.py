# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
#   arr1	                            arr2	                            return
#   [[2, 3, 2], [4, 2, 4], [3, 1, 4]]   [[5, 4, 3], [2, 4, 1], [3, 1, 1]]   [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
# 배열의 곱셈은 arr1의 1행의 각 열을 순차적으로 사용하고 arr2의 각행의 arr1의 열과 같은 인덱스의 열을 곱한다. 
# 배열의 곱셈은 두 행렬의 곱은 행렬의 크기가 같아야만 가능하다. 
#   [2, 3, 2] * [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# = [2, 3, 2] * [[5, 4, 3]
#                [2, 4, 1]
#                [3, 1, 1]]
# = 2 * 5
# = 3 * 2
# = 2 * 3
# =     2 * 4
# =     3 * 4
# =     2 * 1
# =         2 * 3
# =         3 * 1
# =         2 * 1
# = [22, 22, 11]

def solution(arr1, arr2):
    # 결과를 받을 배열 선언
    answer = []
    temp = []
    temp1 = []
    # 연산을 위한 반복문
    for k in range(len(arr1)):
        for i in range(len(arr1)):
            for j in range(len(arr1)):
                temp.append(arr1[k][i] * arr2[i][j])
            answer.append(temp)
            temp = []
        temp1.append(answer)
        answer = []

    temp2 = []
    for i in range(len(temp1)):
        sum = 0
        for j in range(len(temp1)):
            print(temp1[j][i])
        # temp2.append(sum)
    

    
            
        
            

    print(temp2)
    return answer

solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],	[[5, 4, 3], [2, 4, 1], [3, 1, 1]])