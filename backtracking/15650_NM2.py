# BOJ 15650 N과M(2)
# 백트래킹 복습 - 26.09.29
"""
[노트]
- nCr 조합
- 오름차순이니 num을 골랐다면 다음숫자는 num+1부터 선택
- start 부터 보니 visit 필요 X
"""

import sys

input = sys.stdin.readline


def backtr(depth, start):
    if depth == M:
        print(*result)
        return

    # (1~N)숫자 선택 - 오름차순
    for num in range(start, N + 1):
        result.append(num)

        # 다음 깊이
        # num을 골랐으니 다음숫자는 num+1부터만 선택
        backtr(depth + 1, num + 1)

        # 상태 복구
        result.pop()


N, M = map(int, input().split())
result = []

# 깊이0 시작
backtr(0, 1)
