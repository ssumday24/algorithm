# N과M(2) #15650
# 26.02.12
# 26.03.31 복습
import sys

input = sys.stdin.readline


def func(depth, start):
    if depth == M:
        print(*result)
        return

    # 숫자 start~N에 대해 숫자i 고르기
    for i in range(start, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            # 다음깊이: 숫자 i+1부터 고르기
            func(depth + 1, i + 1)

            # 상태회복
            visited[i] = False
            result.pop()


N, M = map(int, input().split())
visited = [False] * (N + 1)  # 1~N 사용
result = []

# start=1 시작
func(0, 1)
