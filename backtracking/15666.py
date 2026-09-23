# BOJ 15666
# N 과 M (12),시리즈 마지막 - S2
# 26.03.18
import sys

input = sys.stdin.readline
"""
[생각순서]
1. 같은수 여러번사용가능
 vis배열 필요x

2.비내림차순
 인덱스 start 넘겨주기
"""


def func(depth, start):
    if depth == M:
        print(*result)
        return

    before = 0  # 0으로초기화

    for i in range(start, N):

        if arr[i] == before:
            continue

        before = arr[i]

        # 1.
        result.append(arr[i])

        # 2. arr[i]골랐으면 다음깊이는 arr[i]부터시작 (중복선택가능)
        func(depth + 1, i)

        # 3.상태복구
        result.pop()


# main
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

#
arr.sort()
start = 0
func(0, 0)
