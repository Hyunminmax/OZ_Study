def solution(arr):
    answer = []
    cnt = 0
    temp = arr[0]
    if len(arr) == 1:
        return [-1]
    else: 
        # arr.pop(arr.index(min(arr))) 가능하지만 느림
        for i in range(len(arr)):
            if temp > arr[i]:
                temp = arr[i]
                cnt = i
        arr.pop(cnt)
        return arr

solution([4,3,2,1])