# BOJ 15652 N과M(4)
# 백트래킹 복습 - 26.09.29
"""
[노트]
- 중복조합
- visited 가 필요한경우:
<탐색 경로에서, 어떤 원소를 다시 쓰면 안될때>

- start 가 필요한 경우:
-> 순서 중복 제거 (조합)
근데 start 로 중복 금지하면, 자연스럽게 visited도필요x
"""

import sys

input = sys.stdin.readline


def func(depth, start):
    if depth == M:
        print(*result)
        return

    # 숫자 i를 골랐으니 다음깊이는 i부터 (중복허용)
    for i in range(start, N + 1):
        # 숫자i선택
        result.append(i)

        # 다음깊이
        func(depth + 1, i)

        # 복구
        result.pop()


N, M = map(int, input().split())
result = []

func(0, 1)
