# BOJ 7576 토마토
# BFS 복습(3) - 26.09.23
# 시간: /20분
"""
[조건]
- 1: 익음 , 0: 안익음, -1: 토마토 없음
- 모두 익을떄까지 최소 날짜=?

[문풀 노트]
- 시작점이 여러개일때

"""

from collections import deque
import sys


def bfs():

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1.bfs진행
    while q:
        cur_x, cur_y = q.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 배열벗어남
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 비어있는곳 or 이미 익은곳 이동불가
            if board[nx][ny] == -1 or board[nx][ny] >= 1:
                continue

            # 익게한후 큐에넣기
            board[nx][ny] = board[cur_x][cur_y] + 1
            q.append((nx, ny))

    return


###
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque()
flag = False  # 안익은 토마토 존재여부
result = 0  # 토마토가 전부익는 최소날짜


# 방문체크없이, 일단 원본배열 수정으로 진행
for i in range(N):
    for j in range(M):
        # 익은토마토 전부 큐에 넣기
        if board[i][j] == 1:
            q.append((i, j))

        if board[i][j] == 0:
            flag = True

# 예외1) 처음부터 모두 익었으면 0 -> 처음부터 0이 없을떄
if flag == False:
    print(0)
    sys.exit()

# 1.전체bfs진행
bfs()

# 예외2) 모두 익지 못하는상태 -> 다끝난후 0이 존재
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            sys.exit()

        # 배열에서 최댓값= 최소 날짜
        result = max(result, board[i][j])


# 결과출력
print(result - 1)

# print(*board, sep="\n")
