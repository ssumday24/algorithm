# BOJ 5427: 불 G4
# 26.03.27
"""
[문제조건]
- 불이 옮겨진칸 - 이동X
- 이제 불이 붙으려는칸 - 이동X

[문풀 WIL]
- 이 문제처럼 플래그 처리 다중으로 필요하면 BFS를 함수로 분리
    - break 는 가장 안쪽만 탈출하므로

- "도착할곳이 불이 먼저 와있으면 못지나감" 체크할때
  (dist_fire[nx][ny] >= 0) 빼먹기 쉬운데, 이를 방지하려면
- float('inf')로 초기화
    - 문자열 inf != float('inf)  다름 주의
    - dist=[[float("inf")] * W for _ in range(H)]
- 즉 불이 못오는곳은 시간이 무한대로 걸린다고 처리
"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs_fire(q):
    while q:
        cur_x, cur_y = q.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 배열 벗어남
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue

            # 이미 방문한곳
            if dist_fire[nx][ny] != float("inf"):
                continue

            # 벽은 못지나감
            if board[nx][ny] == "#":
                continue

            # 방문체크후 큐에넣기
            dist_fire[nx][ny] = dist_fire[cur_x][cur_y] + 1
            q.append((nx, ny))


def bfs_me(q_me):
    is_escape = False

    while q_me:
        cur_x, cur_y = q_me.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 배열 벗어남 => 탈출조건
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                print(dist_me[cur_x][cur_y] + 1)
                is_escape = True
                return is_escape

            # 이미 방문한곳
            if dist_me[nx][ny] != -1:
                continue

            # 벽은 못지나감
            if board[nx][ny] == "#":
                continue

            # 조건1) 도착할곳이 불이 먼저 와있으면 못지나감
            # 등호조건: 같은시간에 도착할때도 못지나감
            # 불이 와있으면 dist값은 0이상
            if dist_fire[nx][ny] <= dist_me[cur_x][cur_y] + 1:
                continue

            # 방문체크후 큐에넣기
            dist_me[nx][ny] = dist_me[cur_x][cur_y] + 1
            q_me.append((nx, ny))

    return is_escape


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    W, H = map(int, input().split())
    # HxW matrix
    board = [list(input().strip()) for _ in range(H)]
    """
    . :빈공간
    # :벽
    @ :시작위치
    * : 불
    """
    q = deque()  # 불 큐
    q_me = deque()  # 사람 큐

    dist_fire = [[float("inf")] * W for _ in range(H)]
    dist_me = [[-1] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            # 불 좌표 큐에넣기, 불은 여러개일수 있음
            if board[i][j] == "*":
                dist_fire[i][j] = 0
                q.append((i, j))

            # 내 좌표 큐에넣기 , 유일
            if board[i][j] == "@":
                dist_me[i][j] = 0
                q_me.append((i, j))

    # 1.불 BFS - O(WH)
    bfs_fire(q)

    # 2.사람BFS  - O(WH)
    # 탈출여부도 확인
    is_escape = bfs_me(q_me)

    # 탈출불가
    if not is_escape:
        print("IMPOSSIBLE")

    # 디버깅
    # print(*dist_fire, sep="\n")
    # print("========")
    # print(*dist_me, sep="\n")
