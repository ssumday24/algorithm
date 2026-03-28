# 벽부수고 이동하기 #2206
# 26.03.28
"""
1. 3차원 방문배열에 벽을 부순 여부 저장
    - 각 평행우주 시뮬레이션

2. 왜 목적지에 도착하자마자 최단거리 보장?
- 큐에 쌓이는 순서는 무조건 거리순
- 큐에서 뽑았는데 그곳이 도착점이면 뒤에 남아있는 모든 데이터는
무조건 나보다 시간이 오래걸림

3.벽을 부수는 게 최단 거리인지 모르는게 맞고,
그렇기 때문에 '부순 놈'도 큐에 넣고, '안 부순 놈'도 계속 큐에 넣어서 경주
-> 그 경주에서 1등으로 들어온 놈이 정답

"""


# main
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]  # N*M 배열

# N차원, M*2 배열로 설계해야 인덱스 매핑 가능
# 즉 N*M*2
# [N][M][0]: 벽안부숨
# [N][M][1]: 벽부숨
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [-0, 0, -1, 1]

q = deque()

# 시작점 방문,큐에넣기
# 시작점 포함이니 1로시작
visited[0][0][0] = 1
q.append((0, 0, 0))  # x,y,벽 부순 개수

# BFS 시작
while q:
    cur_x, cur_y, wall_cnt = q.popleft()

    # 도착하면 최단거리이므로 바로 종료
    if cur_x == N - 1 and cur_y == M - 1:

        # # -----------------디버깅-----------------
        # print("\n=== [0] 벽 아직 안부숨")
        # for i in range(N):
        #     print([visited[i][j][0] for j in range(M)])

        # print("\n=== [1] 벽 부숨 ")
        # for i in range(N):

        #     print([visited[i][j][1] for j in range(M)])
        # # ---------------------------------------------

        print(visited[cur_x][cur_y][wall_cnt])
        sys.exit()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 인덱스 oor
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        # 벽이 있는곳일때
        if board[nx][ny] == 1:
            # 벽 부술수있고 / 벽을 부쉈을때 방문한적이 없으면
            if wall_cnt == 0 and visited[nx][ny][1] == -1:
                # 벽을 부순 우주에 방문
                visited[nx][ny][1] = visited[cur_x][cur_y][0] + 1
                q.append((nx, ny, 1))

        # 벽이 없는곳일때
        else:
            # 이미방문한곳 -> 최단거리 아님
            if visited[nx][ny][wall_cnt] != -1:
                continue

            # 거리계산후 큐에넣기
            visited[nx][ny][wall_cnt] = visited[cur_x][cur_y][wall_cnt] + 1
            q.append((nx, ny, wall_cnt))

# 도착못하면 -1
print(-1)
