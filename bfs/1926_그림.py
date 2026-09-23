# BOJ 1926 : 그림
# BFS 복습(1) - 26.09.22
# https://web.archive.org/web/20260417100401/https://www.acmicpc.net/problem/1926
"""
[문풀 피드백]
1. 큐-> bfs 내부에서 만들기

2. 함수 전역 상태를 어디까지 바꾸는지 명료화
-> 지금 bfs 처럼 리턴값으로 빼기
"""

from collections import deque
import sys

N, M = map(int, input().split())
board = []
visited = [[False] * M for _ in range(N)]  # 방문체크
max_area = 0  # 가장 넓은 영역
cnt = 0  # 그림 개수

# N*M
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs함수
def bfs(i, j):
    # 시작점 방문체크후 큐에넣기
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    area = 1  # bfs출발점 넓이1로 시작

    while q:
        cur_x, cur_y = q.popleft()

        # 상하좌우탐색
        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            # 1.영역밖
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 2. 이미방문한곳
            if visited[nx][ny]:
                continue

            # 3. 0인곳
            if board[nx][ny] == 0:
                continue

            # 방문체크후 큐에넣기
            visited[nx][ny] = True
            q.append((nx, ny))

            # 넓이증가 +1
            area += 1

    return area


# 모든 좌표마다 bfs
for i in range(N):
    for j in range(M):
        # 그림이고, 방문안했을때 출발점 가능
        if board[i][j] == 1 and not visited[i][j]:
            # 그림개수 +1
            cnt += 1
            # 그 시작점에 대해 bfs 진행
            max_area = max(max_area, bfs(i, j))

###출력
print(cnt)
print(max_area)
