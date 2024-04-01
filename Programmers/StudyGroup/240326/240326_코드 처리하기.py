# 문자열 code가 주어집니다.
# code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. 
# mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

# mode는 0과 1이 있으며, idcodeLen를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idcodeLen]의 값에 따라 
# 다음과 같이 행동합니다.

# mode가 0일 때
# code[idcodeLen]가 "1"이 아니면 idcodeLen가 짝수일 때만 ret의 맨 뒤에 code[idcodeLen]를 추가합니다.
# code[idcodeLen]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idcodeLen]가 "1"이 아니면 idcodeLen가 홀수일 때만 ret의 맨 뒤에 code[idcodeLen]를 추가합니다.
# code[idcodeLen]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

# 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

def solution(code):
    answer = ''
    mode = 0
    codeLen = len(code)
    
    for i in range(codeLen):
        # mode가 0이면
        if mode == 0:
            # 코드 인덱스가 1이 아니고
            if code[i] != '1':
                # 인덱스의 값이 짝수면
                if i % 2 == 0:
                    # 인덱스의 값 추가
                    answer = answer + code[i]
            # 코드 인덱스가 1이면
            elif code[i] == '1':
                # 모드를 1로 변경
                mode = 1
        # mode가 1이면
        elif mode == 1:
            # 코드 인덱스가 1이 아니고
            if code[i]!= '1':
                # 인덱스의 값이 홀수면
                if i % 2 != 0:
                    # 인덱스의 값 추가
                    answer = answer + code[i]
            # 코드 인덱스가 1이면
            elif code[i] == '1':
                # 모드를 0로 변경
                mode = 0

    if answer == '':
        answer = 'EMPTY'

    return answer


print(solution("abc1abc1abc"))