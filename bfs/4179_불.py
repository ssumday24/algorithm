# BOJ 4179 불
# BFS 복습(4) - 26.09.23
"""
[조건]
1. 탈출여부
2. 가장빠른 탈출시간

[문풀 노트]
1.시작점이 여러개(멀티소스)bfs 유형
- 모든 시작점 한번에 큐에 넣기

2.엣지케이스 생각
4 4
####
#J.#
#..#
##.#

3. 이중 반복문 완전 탈출 방법
- 지금처럼 flag 방식보다는, 함수안에서 return 

"""

from collections import deque
import sys

input = sys.stdin.readline

###
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

q_fire = deque()  # 불
q_j = deque()  # 지훈

dist_fire = [[-1] * C for _ in range(R)]
dist_j = [[-1] * C for _ in range(R)]

answer = -1  # 탈출시간

# 시작점 각 큐에넣기
# 불은 어디든 이동가능하니, 불부터 bfs 진행
for i in range(R):
    for j in range(C):
        if board[i][j] == "F":
            # 모든 시작점 큐에넣기
            q_fire.append((i, j))
            dist_fire[i][j] = 0

        elif board[i][j] == "J":
            # 모든 시작점 큐에넣기
            q_j.append((i, j))
            dist_j[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

found = False  # 탈출 플래그

# 1.불bfs
while q_fire:
    cur_x, cur_y = q_fire.popleft()
    for d in range(4):
        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        # 범위체크
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue

        # 벽인곳 , 이미 방문한곳
        if board[nx][ny] == "#" or dist_fire[nx][ny] != -1:
            continue

        # 방문체크,큐에넣기
        dist_fire[nx][ny] = dist_fire[cur_x][cur_y] + 1  # 거리1증가
        q_fire.append((nx, ny))


# 2.지훈 bfs - 불이있는곳 못지나감
# found=true 로 찾으면 바로 종료
while q_j and not found:

    cur_x, cur_y = q_j.popleft()
    for d in range(4):
        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        # 범위체크
        # 가장자리를 벗어나면 +1번 이동후 탈출 , 종료
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            answer = dist_j[cur_x][cur_y] + 1
            found = True
            break

        # 벽인곳 , 이미 방문한곳
        if board[nx][ny] == "#" or dist_j[nx][ny] != -1:
            continue

        # 이미 불이 퍼진곳 ,즉
        # 불이 동시 or 먼저 도착했다면
        if dist_fire[nx][ny] != -1 and dist_j[cur_x][cur_y] + 1 >= dist_fire[nx][ny]:
            continue

        # 방문체크,큐에넣기
        dist_j[nx][ny] = dist_j[cur_x][cur_y] + 1  # 거리1증가
        q_j.append((nx, ny))

# 탈출불가
if not found:
    print("IMPOSSIBLE")
# 탈출가능
else:
    print(answer)


# 디버깅용
# print(*dist_j, sep="\n")
# print("========")
# print(*dist_fire, sep="\n")
