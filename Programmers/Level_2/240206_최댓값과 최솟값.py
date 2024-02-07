

# 1st try
def solution(s):
    answer = []
    temp = s.split()
    for i in temp:
        answer.append(int(i))
    answer.sort()
    
    answer = str(answer[0]) + ' ' + str(answer[len(answer)-1])
    
    
    return answer


solution("-1 -1")