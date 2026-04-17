# 완주하지못한선수
# 해시-lv1
# 26.04.17 - 15분
"""
[문풀노트]
1. 동명이인 있으면 집합 set()로 풀이불가 -> 딕셔너리로 인원수 저장필요
2. 딕셔너리의 초기값=?

"""


# 완주못한 선수 이름 리턴
def solution(participant, completion):
    # 1.딕셔너리
    dic = {}

    for name in participant:
        # 같은 이름 있는경우
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1

    # 완주시 -1
    for c_name in completion:
        dic[c_name] -= 1

    for x in dic:
        # 값이 남아있으면 완주못한상태
        if dic[x] != 0:
            return x

    return


# 출력
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
