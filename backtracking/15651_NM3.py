# BOJ 15651 N과M(3)
# 백트래킹 복습 - 26.09.29
"""
[노트]
- 중복순열
"""

import sys

input = sys.stdin.readline


def func(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1,N+1):
        result.append(i)
        func(depth+1)
        result.pop()


N, M = map(int, input().split())
result = []

func(0)
