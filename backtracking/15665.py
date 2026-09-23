# BOJ 15665
# N 과 M (11) - S2
# 26.03.18
import sys

input = sys.stdin.readline
"""
같은수 여러번사용가능-> vis필요x

같은수 여러번고르는 조건이 추가되어도 그냥 
before만 알면됨

"""


def func(depth):
    if depth == M:
        print(*result)
        return

    before = 0  # 0으로초기화

    for i in range(N):

        if arr[i] == before:
            continue

        before = arr[i]

        # 1.
        result.append(arr[i])

        # 2.
        func(depth + 1)

        # 3.상태복구
        result.pop()


# main
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

#
arr.sort()
func(0)
