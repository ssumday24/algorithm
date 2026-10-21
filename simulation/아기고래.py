# 2026 상반기 오후 1번
# L12

"""
[노트]
1. 원본배열 수정이 필요할지 판단 기준?
2. 경로 기록방법
3. 방향회전 심화
4. 최단거리 이동

[조건]
- 바다:0 암초:1
- 바라보는 방향d 1:상 2:하 3:좌 4:우
"""

import sys

input = sys.stdin.readline
from collections import deque


# d=1:상 2:하 3:좌 4:우
def explore(x, y, d):
    global whale_x, whale_y, whale_dir

    # 고래방향:위 -> 상-좌-우-하 순서
    if d == 1:
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        dir = [1, 3, 4, 2]

    # 고래방향:아래 -> 하-우-좌-상
    elif d == 2:
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        dir = [2, 4, 3, 1]

    # 고래방향:좌 -> 좌-하-상-우
    elif d == 3:
        dx = [0, 1, -1, 0]
        dy = [-1, 0, 0, 1]
        dir = [3, 2, 1, 4]

    # 고래방향:우 -> 우-상-하-좌
    else:
        dx = [0, -1, 1, 0]
        dy = [1, 0, 0, -1]
        dir = [4, 1, 2, 3]

    # 인접영역 우선순위에 따라 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # idx 범위
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        # 이미 방문한곳
        if visited[nx][ny]:
            continue

        # 암초
        if board[nx][ny] == 1:
            continue

        # 인접탐험으로 이동+방향 갱신
        whale_x = nx
        whale_y = ny
        whale_dir = dir[i]

        # 방문체크
        visited[nx][ny] = True

        # 이동경로 기록
        route.append((whale_x, whale_y))

        # 이동시 바로 종료
        return True

    # 위에서 인접영역으로 이동 못했을시 false 리턴
    return False


def find_target():
    # 1. 아직 방문안한곳 중 -> 가장 가까운곳으로 이동
    # 2. 거리가 같으면 row,col 순서정렬
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[-1] * N for _ in range(N)]  # 거리계산용
    q = deque()

    # 시작점거리0, 큐에넣기
    q.append((whale_x, whale_y))
    dist[whale_x][whale_y] = 0

    # bfs 진행 -> 일단 거리만 계산
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # idx 범위
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 암초
            if board[nx][ny] == 1:
                continue

            # 이미 방문
            if dist[nx][ny] != -1:
                continue

            # 거리+1,큐에넣기
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

    # 2. 방문 안한곳중 , 거리가장 가까운곳 찾기
    arr = []  # 도착점 후보들

    for i in range(N):
        for j in range(N):
            # 방문안한곳 & 바다인곳 & 현재위치가 아닌곳
            if not visited[i][j] and board[i][j] == 0 and dist[i][j] >= 1:
                # (거리,i,j) 순 저장
                arr.append((dist[i][j], i, j))

    ######### 예외) 이동할 곳이 없으면 종료해야함
    if len(arr) == 0:
        return None

    # (거리,행,열) 순서 정렬
    arr.sort(key=lambda x: (x[0], x[1], x[2]))

    # 도착위치 선택
    (
        target_dist,
        target_x,
        target_y,
    ) = arr[0]

    return target_x, target_y


# BFS의 동작 자체가, 큐에 거리순으로 쌓이기 때문에
# 큐에 넣는 방향 우선순위만 고려하고 도착시 바로 종료하면됨
def move_to_target(target_x, target_y):
    # 목적지로 이동
    # 도착후 바라보는 방향 갱신필요

    # 문제조건: 좌-하-우-상 우선순위
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    start_x = whale_x
    start_y = whale_y

    q = deque()
    local_vis = [[False] * N for _ in range(N)]  # 방문체크, 메인의 visited와 별개

    previous = [[0] * N for _ in range(N)]  # 현재 좌표에대해, 이전에 어디서왔는지 기록

    path = []  # 이동경로 기록

    # 시작점
    q.append((start_x, start_y))
    local_vis[start_x][start_y] = True

    while q:
        cur_x, cur_y = q.popleft()

        # 목적지 도착하면 종료
        if cur_x == target_x and cur_y == target_y:
            return True

        # 좌-하-우-상 순서로 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if local_vis[nx][ny]:
                continue

            # 암초
            if board[nx][ny] == 1:
                continue

            # 방문체크+큐에넣기
            local_vis[nx][ny] = True
            q.append((nx, ny))

            # 이전경로 기록
            previous[nx][ny] = (cur_x, cur_y)

    return


# 메인
N, r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # N*N

visited = [[False] * N for _ in range(N)]  # 방문체크용
route = []  # 이동경로 기록

# 현재 위치 , 바라보는방향 , 0-idx 로 변경
whale_x = r - 1
whale_y = c - 1
whale_dir = d

# 목적지 좌표
target_x = 0
target_y = 0

# 시작점 방문체크
visited[whale_x][whale_y] = True

# 시작점 방문경로에 기록
route.append((whale_x, whale_y))

# 이동할곳 못찾을때까지 반복
while True:
    # 1. 인접칸에 방문가능한 바다가 없을때까지 explore()반복
    while True:
        moved = explore(whale_x, whale_y, whale_dir)

        # explore() 에서 이동못했으면 종료
        if not moved:
            break

    # 2.도착지 정하기
    target = find_target()

    # 못찾으면 종료
    if target is None:
        break

    target_x, target_y = target  # 튜플값 담기

    # 3.타겟으로 이동
    move_to_target(target_x, target_y)
