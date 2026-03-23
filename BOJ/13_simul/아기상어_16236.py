# BOJ 16236 아기상어 - G3
# 26.03.23
"""
[BOJ 16236 아기 상어]

조건
1. 상어크기<물고기 : 이동x,먹기x
2. 자신의 크기만큼 물고기 먹으면 크기 1증가.
- ex) 크기2에서 2마리먹으면 크기3

3.중요) 목적지로 가는와중에, 먹을수있는 물고기가 있는경우는 애초에 존재하지 않음
- 규칙 자체가 가장 가까운 거리의 물고기 먹는것이기 때문)
"""
"""
[WIL]
1. 빈 공간은 시뮬레이션하지 말기 (텔레포트)
    - 상어 이동 과정에 아무 이벤트가 없으면 1초씩 이동하지말고 텔레포트.

2. 탐색과 거리 계산 따로하지말기
    - 목적지 찾기 따로, 거리계산 따로하지말고 bfs 한방에 처리
    
3. 문제 꼼꼼히 읽기

4. 람다 사용한 정렬 
    - arr.sort(key=lambda x: (x[0],x[1],x[2]))
    - 회의실배정
    
5. BFS는 시작점을 절대 다시 방문X 생각
"""

import sys

input = sys.stdin.readline
from collections import deque


# 거리계산 bfs
# 먹을수있는 물고기 후보군 리턴
# 여기서 먹기로직 하면 안됨
def bfs(shark_x, shark_y, shark_size):
    new_arr = []

    dist = [[-1] * N for _ in range(N)]
    q = deque()

    # 시작점 넣기 , 거리:0 시작
    q.append((shark_x, shark_y))
    dist[shark_x][shark_y] = 0

    while q:
        cur_x, cur_y = q.popleft()

        # 상하좌우 탐색
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 범위 벗어남
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 이미 방문한곳
            if dist[nx][ny] >= 0:
                continue

            # 상어크기 < 물고기 크기 : 이동x, 먹기x
            if shark_size < board[nx][ny]:
                continue

            # 이동가능한 경우
            # 상어 크기 == 물고기 크기 : 이동o, 먹기x 므로
            # 거리계산만하기
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            q.append((nx, ny))

            # 상어크기 > 물고기 크기, 즉
            # 먹을수있는 물고기가 있으면서 이동가능할때
            if shark_size > board[nx][ny] and 1 <= board[nx][ny] <= 6:
                new_arr.append((dist[nx][ny], nx, ny))

    # 후보군 반환
    return new_arr


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 1.상어 위치
shark_x, shark_y = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x, shark_y = i, j


shark_size = 2  # 처음크기 2 시작
eaten_cnt = 0  # 먹은 물고기 수
time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:

    candidates = bfs(shark_x, shark_y, shark_size)

    # 3. 먹을수 있는 물고기 없음 ->종료
    if not candidates:
        print(time)
        break

    # 4. 거리순/위쪽순/왼쪽순 오름차순 정렬
    candidates.sort(key=lambda x: (x[0], x[1], x[2]))

    # 가장 가까운 물고기 (0번원소) 먹으러가기
    dist, fish_x, fish_y = candidates[0]

    # 기존위치 0 으로 만들고
    board[shark_x][shark_y] = 0

    # bfs에서 이동조건 검사했으니 바로 순간이동
    board[fish_x][fish_y] = 9

    # 먹은 고기 위치로 업데이트
    shark_x = fish_x
    shark_y = fish_y

    # 먹은 횟수+1
    eaten_cnt += 1

    # 크기 증가하는 경우
    if eaten_cnt == shark_size:
        shark_size += 1

        # 먹은물고기수 초기화
        eaten_cnt = 0

    # 시간 계산 : 이동거리만큼+
    time += dist
