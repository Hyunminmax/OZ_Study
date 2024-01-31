# 명함의 크기, 가로 세로의 각 값을 가지는 2차원 배열이 있다. 가장 작은 명함지갑을 만들 수 있는 가로와 세로의 조합을 찾아 그 곱을 리턴하라. 
# sizes : [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	 /  retrun : 120


# 3rd try
def solution(sizes):
    answer = 0
    # 1차원 배열의 인덱스 0번을 큰 수 1번을 작은 수로 재 정렬하여 각 인덱스의 가장 큰 값으로 명함을 만들면 됨
    widthMax = 0
    heightMax = 0
    
    # 2차원배열에서 1차원의 요소 수 만큼 for문에 인자값으로 주면 자동으로 가지고 옴
    for width, height in (sizes):
        widthMax  = max(widthMax, max(width, height))
        heightMax = max(heightMax, min(width, height))

    answer = widthMax * heightMax
    
    return answer

# # 2dn try : 성공한 3rd와 똑같은 방식이나 다른 점은 42~43의 max값의 초기값을 0으로 하지 않은 것.
#            + 초기값을 0으로 준다면 28번의 if문 때문에 결과값이 0이 나옴
# def solution(sizes):
#     answer = 0
#     # 1차원 배열의 인덱스 0번을 큰 수 1번을 작은 수로 재 정렬하여 각 인덱스의 가장 큰 값으로 명함을 만들면 됨
#     widthMax = sizes[0][0]
#     heightMax = sizes[0][1]
#     if len(sizes) > 1:
#         # 2차원배열에서 1차원의 요소 수 만큼 for문에 인자값으로 주면 자동으로 가지고 옴
#         for width, height in (sizes):
#             widthMax  = max(widthMax, max(width, height))
#             heightMax = max(heightMax, min(width, height))
    
#     answer = widthMax * heightMax
#     print(answer)
#     return answer


# 1st try : 성공한 3rd와 똑같은 방식이나 다른 점은 42~43의 max값의 초기값을 0으로 하지 않은 것. 
def solution(sizes):
    answer = 0
    # 1차원 배열의 인덱스 0번을 큰 수 1번을 작은 수로 재 정렬하여 각 인덱스의 가장 큰 값으로 명함을 만들면 됨
    widthMax = sizes[0][0]
    heightMax = sizes[0][1]
    if len(sizes) > 1:
        for i in range(len(sizes)):
            if sizes[i][1] > sizes[i][0]:
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            if sizes[i][0] > widthMax:
                widthMax = sizes[i][0]
            if sizes[i][1] > heightMax:
                heightMax = sizes[i][1]
    
    answer = widthMax * heightMax
    print(answer)
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])