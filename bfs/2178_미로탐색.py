# BOJ 2178 미로탐색
# BFS 복습(2) - 26.09.22
# 시간:15분
# https://web.archive.org/web/20260417100401/https://www.acmicpc.net/problem/2178
"""
[문풀 피드백]

"""

from collections import deque
import sys

# (1,1)->(n,m) 지나야하는 최소 칸수=?
# n*m 행렬
N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 방문체크+거리 확인

result = 0  # 지나야하는 최소칸수

# bfs 진행
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

# 시작점 방문체크, 큐에넣기
visited[0][0] = 1
q.append((0, 0))

while q:
    cur_x, cur_y = q.popleft()

    # 상하좌우탐색
    for d in range(4):
        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if board[nx][ny] == 0:
            continue

        # 이미방문한곳 == vis값이 1이상인곳
        if visited[nx][ny] >= 1:
            continue

        # 방문체크후 큐에넣기
        visited[nx][ny] = visited[cur_x][cur_y] + 1
        q.append((nx, ny))


# 결과
result = visited[N - 1][M - 1]
print(result)
