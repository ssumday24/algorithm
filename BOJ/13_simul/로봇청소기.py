# BOJ 14503 로봇청소기 - G5
# 26.03.24
"""
[BOJ 14503 로봇청소기 - G5]

1. 전진 <-> 후진
전진: 현재위치에서 dx,dy 를 더하는 것
후진 : 현재위치에서 dx,dy를 빼는것
=> bx= cur_x - dx[dir]


"""
"""
r1. 맵의 테두리는 전부 1

"""

import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 청소 시작 좌표

board = [list(map(int, input().split())) for _ in range(N)]  # N*M 방
visited = [[0] * M for _ in range(N)]  # N*M 방문체크


# 청소 시작
q = deque()
q.append((r, c, d))

# 0:북 1:동 2:남 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소한 칸의 갯수
result = 0

# 만약 방문했다면 벽이아니면서 , 이미 청소한곳.
while q:
    cur_x, cur_y, dir = q.popleft()

    # 초기값 0
    flag = 0

    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[cur_x][cur_y] == 0 and not visited[cur_x][cur_y]:
        visited[cur_x][cur_y] = 1

        # 청소한 칸
        result += 1

    # 주변 4칸에 대해서
    for _ in range(4):
        # 반시계 90도 회전: 270도 시계방향 회전과 동일
        dir = (dir + 3) % 4

        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        # 쓰레기를 찾으면 바로 그곳으로 이동
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not visited[nx][ny]:

            flag = 1
            q.append((nx, ny, dir))
            break

    # 이동할곳 찾았으면 1번으로 되돌아감
    if flag:
        continue

    # 쓰레기 못찾으면
    if not flag:

        # 후진할 위치
        bx = cur_x - dx[dir]
        by = cur_y - dy[dir]

        # 후진불가 : 뒤쪽이 벽일때
        if board[bx][by] == 1:
            break

        # 후진가능 : 한칸 후진후 1번으로 돌아감
        # 이때 바라보는 방향은 유지
        q.append((bx, by, dir))
        continue

# 출력
print(result)


# print(*visited,sep='\n')
