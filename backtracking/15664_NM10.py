# BOJ 15664 N과M(10)
# 백트래킹 복습 - 26.09.30
"""
[노트]
- 비내림차순 + 사전순으로 증가하는 순서
- 인덱스 넘겨줄때 start+1 가 아닌 i+1. 실수 체크
"""

import sys

input = sys.stdin.readline


def func(depth, start):
    if depth == M:
        print(*result)
        return

    # 이번 자릿수에대해, 이전 iteration 에서 선택한 수
    before = None

    # idx : start ~ (N-1)
    # 비내림차순이니 현재인덱스+1 부터 봐도됨
    for i in range(start, N):
        # 전에 등장한 숫자만 아니라면 선택가능
        if before != arr[i]:
            result.append(arr[i])
            # 숫자를 선택하면 before 도 갱신 ->
            # 같은 깊이의 다음 iteration 에서 체크
            before = arr[i]

            # i번쨰 인덱스 선택하니, 다음깊이는 i+1부터 확인
            func(depth + 1, i + 1)

            # 상태복구
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

arr.sort()
# start:0 시작
func(0, 0)
