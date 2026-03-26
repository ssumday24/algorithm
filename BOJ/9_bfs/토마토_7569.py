# BOJ 7569: 토마토 - G5
# 26.03.27
"""
1. 3차원 bfs
2. 다중 출발점 -> 큐에 한번에 다 넣기 (노트참고)
3. 뿌요뿌요, 테트리스 등 원본이 물리적으로 변하면 원본도 수정.
4. 이 문제처럼 탐색으로만 답 낼수있으면, vis로만 조작

"""

import sys

input = sys.stdin.readline
from collections import deque

# NxM , 높이 H
M, N, H = map(int, input().split())

arr = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    arr.append(box)

# 6방향중 한번에 한곳으로만 이동가능
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# BFS용 큐
q = deque()

# 거리체크 배열 H*(N*M)
dist = [[[-1] * M for _ in range(N)] for _ in range(H)]

# 시작시 0 갯수
zero_cnt = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                # 모든 토마토 큐에 넣기 , 거리0
                q.append((k, i, j))
                dist[k][i][j] = 0

            if arr[k][i][j] == 0:
                zero_cnt += 1

# 처음부터 모두 익어있는 상황
# 0일만에 다익음
if zero_cnt == 0:
    print(0)
    sys.exit()


# 익을떄까지 걸리는 일수
result = 0

# BFS 진행
while q:
    cz, cx, cy = q.popleft()

    for d in range(6):
        nz = cz + dz[d]
        nx = cx + dx[d]
        ny = cy + dy[d]

        if nz < 0 or nx < 0 or ny < 0:
            continue
        if nz >= H or nx >= N or ny >= M:
            continue

        # 이미 방문한곳, 즉 이미 토마토인 곳 제외
        if dist[nz][nx][ny] > -1:
            continue

        # 익지 않은곳만 방문
        if arr[nz][nx][ny] == 0:
            q.append((nz, nx, ny))
            dist[nz][nx][ny] = dist[cz][cx][cy] + 1

            # 최대값 갱신
            result = max(result, dist[nz][nx][ny])


# 최종 계산
for k in range(H):
    for i in range(N):
        for j in range(M):
            # 모두 익지는 못하는 상황
            # 처음 안익은 토마토 + 방문못했을때
            if arr[k][i][j] == 0 and dist[k][i][j] == -1:
                print(-1)
                sys.exit()


# 모두다 익어서 여기까지 왔으면
print(result)


# 디버깅용
# for box in arr:
#     print(box)
