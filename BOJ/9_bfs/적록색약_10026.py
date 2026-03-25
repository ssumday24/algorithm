# BOJ 10026 적록색약 - G5
# 26.03.24
import sys

input = sys.stdin.readline
from collections import deque

"""
BOJ 10026 적록색약 - G5

"""
N = int(input())
board = [list(input().strip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False] * N for _ in range(N)]
    q = deque()
    area = 0

    # 모든점에서 bfs 체크
    for a in range(N):
        for b in range(N):

            # 이미 방문한곳
            if visited[a][b]:
                continue

            # 좌표+색깔정보 넣기
            q.append((a, b, board[a][b]))
            visited[a][b] = True

            # 각 여역들의 시작점
            # print(f"({a},{b})")

            # 영역개수 +=1
            area+= 1

            while q:
                curx, cury, color = q.popleft()

                for d in range(4):
                    nx = curx + dx[d]
                    ny = cury + dy[d]

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue

                    # 이미 bfs 진행한곳
                    if visited[nx][ny]:
                        continue

                    # 다른색깔이면 못감
                    if color != board[nx][ny]:
                        continue

                    # 방문체크후 큐에넣기
                    visited[nx][ny] = True
                    q.append((nx, ny, board[nx][ny]))

    #영역개수 리턴 
    return area

# 1.색약 아닐때
result1=bfs()

# 2. 색약일때
for i in range(N):
    for j in range(N):
        # 초록색 -> 전부 빨강으로 교체
        if board[i][j]=='G  ':
            board[i][j]='R'

result2=bfs()

# 출력부분
print(f"{result1} {result2}")
