# BOJ 15657 N과M(8)
# 백트래킹 복습 - 26.09.30
"""
[노트]
- 중복허용 + 비내림차순
-> 중복허용: vis필요x,
-> 비내림차순: idx 넘겨주기

"""

import sys

input = sys.stdin.readline


def func(depth, start):
    if depth == M:
        print(*result)
        return

    # num : start~(N-1) 까지만 보기
    for num in range(start, N):
        # num번째 인덱스 선택
        result.append(arr[num])

        # 다음깊이부터는 num idx 부터 봐야함
        func(depth + 1, num)

        #상태복구
        result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []  # 결과 담을 배열

arr.sort()

# start idx:0시작
func(0, 0)
