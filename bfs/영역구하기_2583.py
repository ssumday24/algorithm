# BOJ 2583
# 영역 구하기 - S1
# 26.03.29
"""
- x축 -> 행 N
- y축 -> 열 M  바로변환


1.분리된 영역의 개수
2. 각 분리된 영역의 넓이 (오름차순 정렬)
"""
import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

# N*M 모눈종이
board = [[0] * M for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# K개 직사각형
for _ in range(K):
    st_x, st_y, end_x, end_y = map(int, input().split())

    # 직사각형 채우기
    for i in range(st_x, end_x):
        for j in range(st_y, end_y):
            # 여러번 덮일수있으니 이전값+1
            board[i][j] += 1

visited = [[0] * M for _ in range(N)]
cnt = 0  # 영역개수
arr_area = []  # 영역의 넓이 저장할 배열

# 영역개수계산, bfs
for i in range(N):
    for j in range(M):

        # 색칠된곳 /이미 bfs 진행한곳  제외
        if board[i][j] != 0 or visited[i][j]:
            continue

        # 모든 시작점마다 BFS
        q = deque()
        area = 0  # 영역의 넓이

        # 시작점
        visited[i][j] = True
        q.append((i, j))
        cnt += 1  # 영역의 개수 +1
        area += 1  # 영역의 넓이 +1

        while q:
            cur_x, cur_y = q.popleft()

            for d in range(4):
                nx = cur_x + dx[d]
                ny = cur_y + dy[d]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                # 이미 방문한곳
                if visited[nx][ny]:
                    continue

                # 색칠된곳 제외
                if board[nx][ny] != 0:
                    continue

                # 큐에넣기
                visited[nx][ny] = 1
                q.append((nx, ny))

                # 영역의 넓이 +1
                area += 1

        # bfs 끝난후, 영역넓이 저장
        arr_area.append(area)

# 결과
print(cnt)

arr_area.sort()
for elem in arr_area:
    print(elem, end=" ")
