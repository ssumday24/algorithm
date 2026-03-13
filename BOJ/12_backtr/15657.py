# BOJ 15657
# N 과 M (8) - S3
# 26.03.13
import sys

input = sys.stdin.readline
"""
중복선택가능, 비내림차순
"""


def func(depth, start):
    # M개 골랐을때
    if depth == M:
        for x in result:
            print(x, end=" ")
        print()
        return

    # idx: start~N-1
    for i in range(start, N):
        # 값 추가
        result.append(arr[i])

        # 다음깊이: start =i
        func(depth + 1, i)

        result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

start = 0  # start 초기값:0
arr.sort()
func(0, 0)
