
def solution(players, callings):
    # players :["mumu", "soe", "poe", "kai", "mine"]
    # callings:["kai", "kai", "mine", "mine"]
    
    # 플레이어들의 순위 딕셔너리 생성 players 리스트와 인덱스 비교에 용이하도록 0부터 시작
    ranks = {player: rank for rank, player in enumerate(players)}

    # 호명되는 선수들 순서로 반복
    for i in callings:
        # 호명 된 선수의 기존 순위 추출
        oldRank = ranks[i]
        # 호명 된 선수의 순위 한 단계 상승 
        ranks[i] -= 1
        # 호출 된 선수의 앞에 있던 선수를 최초 선수리스트 players에서 찾고
        # 그 선수를 순위 딕셔너리에서 찾아 그 선수의 순위를 한 단계 낮춘다. 
        ranks[players[oldRank-1]] += 1
        # 지금의 변경 된 순위를 players 리스트에 적용한다. 
        # 아래와 같이 하면 임시저장소 없이 동시에 위치를 변경하는 것이 가능 
        players[oldRank-1], players[oldRank] = players[oldRank], players[oldRank-1]

    return players

    
    # 4th try
    # answer = []
    # # 플레이어 배열과, 플레이어의 호출 순서대로 만들어진 배열이 있다.
    # # 플레이어의 호출이 있을 때 마다 플레이어 배열에서 해당 플레이어는 인덱스가 한 칸 빨라진다.
    # # 필요한 기능
    
    # # 플레이어의 숫자로 필요한 등 수 만큼 rank 딕셔너리의 키 생성
    # # rank = dict.fromkeys(list(range(1, len(players)+1)), '')
    # ranks = {player: oldRank for oldRank, player in enumerate(players, 1)}
    # # 기존 순위 확인
    # # print('1: ',  ranks)
    # reversedRanks = {rank: player for player, rank in ranks.items()}
    # # print('변경전 ranks:',ranks)
    # # print('변경전 reversed:',reversedRanks)
    # for i in callings:
    #     print(i)
    #     temp1 = ranks[i]
    #     temp2 = reversedRanks[ranks[i]-1]
    #     reversedRanks[ranks[i]-1] = i
    #     reversedRanks[ranks[i]] = temp2
    #     ranks[temp2] = temp1
    #     # print('변경후 ranks:',ranks)
    #     # print('변경후 reversed:',reversedRanks)

    # # 새로운 순위 순서로 정렬
    # answer = sorted(ranks, key=ranks.get)

    # 3rd try
    # # 플레이어 호출을 순차적으로 진행
    # for i in callings:
    #     # 호출 된 플레이어의 기존 등수에서 1단계 상승
    #     newRank = ranks[i] - 1
    #     # 호출 된 플레이어의 새로운 등수와 기존의 순위가 같은 플레이어를 순위 딕셔너리에서 찾음
    #     for player, oldRank in ranks.items():
    #         # 1단계 상승한 순위와 기존의 순위가 같은 key:value 를 찾았다면
    #         if newRank == oldRank:
    #             # 기존 순위의 플레이어에게 호출 된 플레이어의 순위상승 전 순위를 할당
    #             ranks[player] = ranks[i]
    #             # 호출 되어 순위가 상승한 플레이어의 value에 새로운 순위 할당
    #             ranks[i] = newRank
    #             # 순위를 변경하는 반복문에서 탈출
    #             break
    # # 새로운 순위 확인
    # # print('2: ',  ranks)
    
    # # 새로운 순위 순서로 정렬
    # answer = sorted(ranks, key=ranks.get)
    # print(answer)
    
    # 2nd try
    # 각플레이어가 몇 번 호출 되었는지 계산하고 호출 수 만큼 각 해당 플레이어의 인덱스를 당긴다. 
    
        # # 반복문 안에서 index를 찾으면 느림
        # for i in callings:
        #     # 호출 된 플레이어 위치 찾기
        #     rank = players.index(i)
        #     # 호출 된 플레이어의 위치 앞에 추가하기
        #     players.insert(rank-1, i)
        #     # 호출 된 플레이어의 기존 위치 삭제하기
        #     players.pop(rank+1)
    # 위 방법으로 진행하면 players.index(i)가 또 다른 반복문으로 작동하여 속도저하가 발생
    # 딕셔너리를 활용하여 누적
    # temp = dict.fromkeys(callings, 0)
    # for i in callings:
    #     temp[i] += 1
        
    # 1st try
    # # players 배열에서 각 플레이어의 누적 호출수 만큼 인덱스 당김
    # for i in temp.keys():
    #     # 호출 된 플레이어 위치 찾기
    #     rank = players.index(i)
    #     # 호출 된 플레이어의 위치 앞에 추가하기
    #     players.insert(rank-temp[i], i)
    #     # 호출 된 플레이어의 기존 위치 삭제하기
    #     players.pop(rank+1)

    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])