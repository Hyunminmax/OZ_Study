# 문자열 s를 받아서 알파벳 순서를 index만큼 뒤로 미룬다. 
# 그 과정에서 skip에 해당하는 알파벳은 카운트하지 않는다. 

# 2nd try
# a to z 리스트를 생성하고 그 리스트에서 skip에 해당하는 리스트를 삭제한다. 
# s의 각 글자를 atoz리스트의 자리와 비교하고 index값에 해당하는 만큼 뒤로 미룬다. 
def solution(s, skip, index):
    answer = ''
    
    # aToz리스트 생성, skip 리스트에 해당되는 알파벳 제외
    aToz = []
    # 알파벳에 해당하는 유니코드값을 만들고 다시 알파벳으로 변환하여 aToz리스트에 담는다.
    for charABC in range(ord('a'), ord('z')+1):
        if chr(charABC) not in skip:
            aToz += chr(charABC)
    # aToz 리스트 크기 확인
    aTozlen = len(aToz)
    
    # s리스트의 알파벳하나씩 새로운 인덱스 검색
    for abc in s:
        # aToz인덱스에서 s리스트의 알파벳이 해당하는 인덱스 검색 -> abcIndex
        abcIndex = aToz.index(abc)
        # abcIndex에 index만큼 뒤로 미룸, 미룬 값이 aToz리스트의 길이를 초과한다면 초과한 수는 aToz리스트의 앞에서 마저 미룬다. 
        if abcIndex + index >= aTozlen:
            newIndex = (abcIndex + index) % aTozlen
        else:
            newIndex = abcIndex + index
        # 그렇게 미뤄진 인덱스에 해당하는 알파벳을 담는다.
        answer += aToz[newIndex]
    
    return answer





# # 1st try
# # a to z 리스트를 생성하고 그 리스트에서 skip에 해당하는 리스트를 삭제한다. 
# # s의 각 글자를 atoz리스트의 자리와 비교하고 index값에 해당하는 만큼 뒤로 미룬다. 
# def solution(s, skip, index):
#     answer = ''
    
#     # aToz리스트 생성, skip 리스트에 해당되는 알파벳 제외
#     aToz = []
#     # 알파벳에 해당하는 유니코드값을 만들고 다시 알파벳으로 변환하여 aToz리스트에 담는다.
#     for charABC in range(ord('a'), ord('z')+1):
#         if chr(charABC) not in skip:
#             aToz += chr(charABC)
#     # aToz 리스트 크기 확인
#     aTozlen = len(aToz)
    
#     # s리스트의 알파벳하나씩 새로운 인덱스 검색
#     for abc in s:
#         # aToz인덱스에서 s리스트의 알파벳이 해당하는 인덱스 검색 -> abcIndex
#         abcIndex = aToz.index(abc)
#         # abcIndex에 index만큼 뒤로 미룸, 미룬 값이 aToz리스트의 길이를 초과한다면 초과한 수는 aToz리스트의 앞에서 마저 미룬다. 
#         if abcIndex + index >= aTozlen:
#             newIndex = abcIndex + index - aTozlen
#         else:
#             newIndex = abcIndex + index
#         # 그렇게 미뤄진 인덱스에 해당하는 알파벳을 담는다.
#         answer += aToz[newIndex]
    
#     return answer



solution("aukks", "wbqd", 5)