# BOJ 15649 N과M(1)
# 백트래킹 복습 - 26.09.29
"""
[노트]
- nPr 순열

"""

import sys

input = sys.stdin.readline


def backtr(depth):
    if depth == M:
        print(*result)
        return

    # 1~N 사용 체크
    for num in range(1, N + 1):
        if not visited[num]:
            # 방문체크후 다음단계
            visited[num] = True
            result.append(num)

            # 다음깊이
            backtr(depth + 1)

            # 상태복구
            visited[num] = False
            result.pop()


N, M = map(int, input().split())
result = []  # 결과 담을 배열
visited = [False] * (N + 1)  # idx:1~N

# 깊이0 시작
backtr(0)
