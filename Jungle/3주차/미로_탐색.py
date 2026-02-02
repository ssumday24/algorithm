from collections import deque

# 입력
N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

# 상하좌우 이동 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽이면 무시
            if maze[nx][ny] == 0:
                continue
            # 처음 방문한 곳이면 거리 갱신
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]  # 도착점 값 리턴

# 실행
print(bfs(0, 0))
