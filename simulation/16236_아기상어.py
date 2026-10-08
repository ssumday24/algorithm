# BOJ 16236 아기상어
# 10.08
"""
[조건]
- 처음상어 크기:2
- 크기가 같으면 -> 먹기x , 지나감
- 크기 작으면 -> 먹기o
- 자신의 크기만큼 물고기를 먹으면 ->  크기1 증가

- 이동과 동시에 물고기 먹고, 그칸은 빈칸이 됨
- 먹을수 있는 물고기 없으면 -> 도움 요청
- 1마리 -> 그거 먹으러감
- 여러마리 -> 가장 가까운 물고기 먹으러감
    - 같은 거리일시 위, 왼쪽부터


[노트]
- bfs 에서 방문체크 안하면 무한루프
- 매 1초마다 조건확인해야하지않나??
상어사이즈가 매초마다 달라질수있고 그에따라 이동가능영역도 달라질텐데


"""

import sys

input = sys.stdin.readline
from collections import deque


def bfs(start_x, start_y):

    # 최단거리 bfs로 계산

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    global shark_size  # 상어크기
    global cnt_eaten  # 먹은 물고기수

    dist = [[-1] * N for _ in range(N)]  # 거리계산용 n*n
    q = deque()

    # 시작점 방문체크, 큐에넣기
    q.append((start_x, start_y))
    dist[start_x][start_y] = 0

    while q:
        cur_x, cur_y = q.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # idx 범위 체크
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 이미 방문한곳
            if dist[nx][ny] >= 0:
                continue

            # 자기크기보다 크면 못감
            if board[nx][ny] > shark_size:
                continue

            # 이동가능할때
            q.append((nx, ny))
            dist[nx][ny] = dist[cur_x][cur_y] + 1

    return dist


# main
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            start_x = i  # 상어 현재위치x
            start_y = j  # 상어 현재위치y


cur_time = 0  # 현재 시간
shark_size = 2  # 상어 현재 크기
cnt_eaten = 0  # 먹은 물고기수 -> 크기 커질때마다 리셋


# 1칸 이동에 1초 소요
while True:
    fish = []  # (i,j,거리 )

    # 이동 가능한곳 bfs로 탐색
    dist = bfs(start_x, start_y)

    for i in range(N):
        for j in range(N):
            # 상어가 이동가능한곳 + 잡아먹을수 있는곳 필터링
            if (1 <= board[i][j] < shark_size) and dist[i][j] != -1:
                fish.append((i, j, dist[i][j]))

    # 종료조건) 먹을곳 없으면 종료
    if len(fish) == 0:
        break

    # 1. 거리순 정렬
    # 2. 거리같으면 위쪽, 왼쪽순 정렬
    # x 에 인자로 (i,j,거리) 들어가니까
    fish.sort(key=lambda x: (x[2], x[0], x[1]))

    # 최종적으로 이동할곳 선택
    target_x, target_y, target_dist = fish[0]

    # 1.잡아 먹기
    cnt_eaten += 1

    # 2.크기 커졌을시 먹은 물고기 수 리셋
    if cnt_eaten == shark_size:
        shark_size += 1
        cnt_eaten = 0

    # 3.상어 이동
    board[target_x][target_y] = 9
    board[start_x][start_y] = 0

    # 4. 좌표갱신
    start_x = target_x
    start_y = target_y

    # 5. 이동한 칸수만큼 시간경과
    cur_time += target_dist

# 출력
print(cur_time)
