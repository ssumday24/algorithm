# 로또_18870
# 26.03.30
"""
백트래킹 문제집


"""

import sys
from collections import deque

input = sys.stdin.readline


def backtr(depth, start):
    # 6개 고르면 종료
    if depth == 6:
        print(*result)
        return

    # arr[start]~arr[K]
    for i in range(start, K + 1):
        result.append(arr[i])

        # 다음 수는 i+1 부터 고르기 ->조합
        backtr(depth + 1, i + 1)

        # 상태복구
        result.pop()


while True:
    # arr[1]~arr[K]만 사용
    arr = list(map(int, input().split()))
    K = arr[0]

    if K == 0:
        break

    # kC6 계산 / arr에서 6개고르기
    result = []
    backtr(0, 1)

    print()  # Tc마다 빈줄
