# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 
# 암호의 규칙은 다음과 같습니다.

# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
# skip에 있는 알파벳은 제외하고 건너뜁니다.
# 예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 
# 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 
# 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 
# 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

# 두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 
# return하도록 solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ s의 길이 ≤ 50
# 1 ≤ skip의 길이 ≤ 10
# s와 skip은 알파벳 소문자로만 이루어져 있습니다.
# skip에 포함되는 알파벳은 s에 포함되지 않습니다.
# 1 ≤ index ≤ 20



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