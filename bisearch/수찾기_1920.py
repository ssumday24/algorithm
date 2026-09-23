# 수 찾기 #1920
# 26.03.28
""" """

import sys
from collections import deque

input = sys.stdin.readline


def bsearch(start, end):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1

        # 타겟이 오른쪽에 위치
        elif arr[mid] < target:
            start = mid + 1

        # 타겟이 왼쪽
        elif arr[mid] > target:
            end = mid - 1

    # 못찾음
    return 0


# main
N = int(input())
arr = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

# 1. 크기순 정렬
arr.sort()

# 각 M값에 대해 arr에 존재하는지
for target in arr_m:
    # 초기값
    start = 0
    end = N - 1

    flag = bsearch(start, end)

    if flag:
        print(1)
    else:
        print(0)
