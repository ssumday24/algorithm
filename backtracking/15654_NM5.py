# BOJ 15654 N과M(5)
# 백트래킹 복습 - 26.09.29
"""
[노트]
- 사전 순으로 증가하는 순서

- 중복허용x -> used 필요
- 조합x -> idx 넘겨주기 필요x
"""

import sys

input = sys.stdin.readline


def func(depth):

    if depth == M:
        print(*result)
        return

    # arr[i]를 선택할지   결정
    # i : 0~N-1
    for i in range(0, N):
        if not used[i]:
            used[i] = True
            result.append(arr[i])

            # 다음깊이
            func(depth + 1)

            # 상태복구
            result.pop()
            used[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))  # idx : 0~N-1
result = []

# idx: i번째 인덱스
used = [False] * (N)

arr.sort()
func(0)
