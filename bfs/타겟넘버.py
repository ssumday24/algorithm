# 타겟넘버
# DFS/BFS - lv2
# 26.04.17 - 15분
"""
1.인자로 합 넘겨서 o(1)에 계산
2. 함수안에있는 cnt는  nonlocal
"""


def solution(numbers, target):
    cnt = 0  # 경우의수

    def backtr(depth, cur_sum):
        nonlocal cnt

        # numbers 부호 전부 고르면 계산
        if depth == len(numbers):
            # target과 같으면 +1
            if cur_sum == target:
                cnt += 1
            return

        for i in [+1, -1]:
            # 다음깊이
            backtr(depth + 1, cur_sum + i * numbers[depth])

    # 백트래킹 시작
    backtr(0, 0)

    return cnt


#
print(solution([4, 1, 2, 1], 4))
