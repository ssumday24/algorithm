# N과M(9) #15663
# 26.02.12
# 26.03.31 복습
import sys

input = sys.stdin.readline
"""
1. vis가 필요?
: 숫자 중복사용 불가니까 필요

2. 같은 깊이의 for 반복문 안에서, 중복되는수자 기억방법?


"""


def func(depth):
    if depth == M:
        print(*result)
        return

    # 같은 깊이에서 방금전에 사용한 수
    memo_val = 0

    for i in range(N):
        # 숫자 선택이 가능하면, 중복된 수인지체크
        if not visited[i]:
            # 중복된 수 체크후 걸러내기
            if memo_val == arr[i]:
                continue

            # 1. 숫자 선택
            visited[i] = True
            result.append(arr[i])

            # 2.현재 선택한 수 다음 for iteration 넘기기
            memo_val = arr[i]

            # 다음깊이
            func(depth + 1)

            # 상태복구
            visited[i] = False
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * (N)

# 1.정렬
arr.sort()
result = []

# 백트래킹
func(0)
