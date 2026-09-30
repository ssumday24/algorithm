# BOJ 15656 N과M(7)
# 백트래킹 복습 - 26.09.30
"""
[노트]
중복허용 -> vis 필요x

"""

import sys

input = sys.stdin.readline


def func(depth):
    if depth == M:
        print(*result)
        return

    # idx : 0~(N-1)
    for i in range(N):
        result.append((arr[i]))
        
        #다음깊이
        func(depth+1)

        #상태복구
        result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []  # 결과 담을 배열

arr.sort()
func(0)
