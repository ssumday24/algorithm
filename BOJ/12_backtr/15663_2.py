# BOJ 15653
# N 과 M (8) - S3
# 26.03.18
import sys

input = sys.stdin.readline
"""
[WIL]
1.순열이니 used배열 필요
2.같은 자릿수에는 중복되는 수가 오면안됨
"""


def func(depth):
    if depth == M:
        print(*result)
        return

    before = 0  # 같은 깊이에서, 바로이전 i에서 사용한값

    for i in range(N):
        # 같은 자릿수에 중복되는 수가 온지 체크.
        if not used[i] and arr[i] != before:

            # before  업데이트(같은 깊이의 모든i)
            before = arr[i]

            # 사용체크
            used[i] = True
            result.append(arr[i])

            # 다음깊이 이동
            func(depth + 1)

            # 상태복구
            used[i] = False
            result.pop()


# main
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
used = [False] * (N)


# 정렬까먹지말기
arr.sort()
func(0)
