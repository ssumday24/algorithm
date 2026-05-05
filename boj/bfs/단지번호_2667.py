# 단지번호 붙이기
# BOJ 2667 - S1
# 26.05.05 - 15분
"""
[문풀 노트]
- 공백 없는 입력 -> strip()

[문제 조건]
1.영역수
2.각 영역의 넓이, 오름차순

"""

import sys
from collections import deque

input = sys.stdin.readline


# 한 영역에 대해 넓이 구하기
def bfs(x, y):
    global N

    size = 0  # 넓이

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    # 시작점 - 방문체크후 큐에넣기
    q.append((x, y))
    visited[x][y] = True
    size += 1

    # bfs 시작
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                continue

            # 방문체크 후 큐에넣기
            visited[nx][ny] = True
            q.append((nx, ny))

            # 넓이 ++
            size += 1

    return size


N = int(input())

# N*N 배열
board = [list(map(int, input().strip())) for _ in range(N)]

# 방문체크용
visited = [[0] * N for _ in range(N)]

home = []  # 각 단지별 집의 수 저장

area_cnt = 0  # 영역개수

# print(*board, sep="\n")

for i in range(N):
    for j in range(N):
        # 집인 곳들 중 ,
        if board[i][j] == 1:
            # 이미 방문안한곳이면
            if not visited[i][j]:
                # 영역개수 +1
                area_cnt += 1

                # 각 영역의 넓이 구하기
                num = bfs(i, j)

                home.append(num)

# 오름차순 정렬
home.sort()


# 출력
print(area_cnt)

for x in home:
    print(x)
