# A반 학생들은 시험이 끝난 뒤 성적이 나오기 전 자기 시험지를 가채점해 보았습니다. 이후에 선생님이 실제 성적을 불러 줄 때 가채점한 점수와 실제 성적이 다른 학생들이 있어 선생님께 문의를 하려고 합니다.

# 성적을 문의하려는 학생들의 번호가 담긴 정수 리스트 numbers와 가채점한 점수가 성적을 문의하려는 학생 순서대로 담긴 정수 리스트 our_score, 실제 성적이 번호 순서대로 담긴 정수 리스트 score_list가 주어집니다. 주어진 solution 함수는 가채점한 점수가 실제 성적과 동일하다면 "Same"을, 다르다면 "Different"를 순서대로 리스트에 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요.

# 제한사항
# 1 ≤ numbers의 길이 = our_score의 길이 ≤ 10
# 1 ≤ numbers의 원소 ≤ 31
# 0 ≤ our_score의 원소 ≤ 100
# our_score[i]는 numbers[i]번 학생이 가채점한 점수입니다.
# numbers는 중복된 원소를 가지지 않습니다.
# 2 ≤ score_list의 길이 ≤ 31
# 0 ≤ score_list의 원소 ≤ 100
# score_list에는 실제 성적이 [1번 학생 성적, 2번 학생 성적, 3번 학생 성적 …] 순서로 들어있습니다.


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer