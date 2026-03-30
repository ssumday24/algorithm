# N과M(1) #15649
# 26.02.12
# 26.03.31
import sys

input = sys.stdin.readline


def func(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            # 사용하지 않은 숫자 선택
            visited[i] = True
            result.append(arr[i])

            # 다음깊이
            func(depth + 1)

            # 상태복구
            visited[i] = False
            result.pop()


N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]  # [1,2,3,4]

# print(arr)

visited = [0] * (N)  # idx: 0~n-1
result = []
# 백트래킹
func(0)
