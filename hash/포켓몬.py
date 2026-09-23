# 포켓몬 - LV 1
# 해시
# 26.04.19
"""
[노트]
- 딕셔너리 dic["3"] <-> dic[3] 다름
-

[문제조건]
- N/2 마리 선택 + 가장 많은 종류 포켓몬 선택
"""


# 포켓몬 종류가 더 많아도  최대 N//2 이고
# 종류(len(nums)) 가 적으면 더 고를수 없으니
# 둘중 작은값이 정답
def solution(nums):

    # N = len(nums)
    # s = set()  # 선택한 포켓몬 번호 집합
    # dic = {}  # dic[번호]=포켓몬 수
    # cnt = 0  # 고른 마리수

    # for elem in nums:
    #     # 처음 본 종류일때
    #     if elem not in dic:
    #         dic[elem] = 1

    #     # 같은 종류일때
    #     else:
    #         dic[elem] += 1

    # print(dic)

    # # 이제 절반만큼 고르기
    # for elem in dic:
    #     # 선택하지 않은 번호 and 1마리이상 있으면 무조건 고르기
    #     if elem not in s and dic[elem] >= 1:
    #         s.add(elem)
    #         dic[elem] -= 1  # 선택했으니 -1
    #         cnt += 1

    #         # 절반골랐으면 바로 종료
    #         if cnt == N // 2:
    #             return cnt

    answer = min(len(nums) // 2, len(set(nums)))

    return answer


# TC
print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
