# BOJ 1012
# 유기농배추-S1
# 26.03.20
"""
BFS문제집 - 6

- #1926 그림이랑 완전히 같은문제

- i 반복문 안에서 i 또 쓰지 않도록 조심 (indexError)

- "시작점에 대해서도 조건에 맞는지 검사"
"""
import sys

input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 테스트케이스 t개
for _ in range(T):
    # 각 TC마다 지렁이 초기화
    result = 0

    # 가로M,세로N 배추밭, 배추위치 K개
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    # BFS 큐, 방문체크 배열
    visited = [[False] * M for _ in range(N)]

    # 배추밭 만들기
    for _ in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1

    # 독립적으로 분리된 영역 계산
    for i in range(N):
        for j in range(M):

            q = deque()

            # 배열의 모든 지점마다 bfs
            # 배추가있고, 방문x 인곳에서시작
            if arr[i][j] == 0 or visited[i][j]:
                continue

            # 시작점 넣기
            visited[i][j] = True
            q.append((i, j))

            # bfs 진행
            while q:
                cur_x, cur_y = q.popleft()

                # 현재 좌표기준 상하좌우 탐색
                for dir in range(4):
                    nx = cur_x + dx[dir]
                    ny = cur_y + dy[dir]

                    # 인덱스 범위
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue

                    # 이미 bfs 진행한곳
                    if visited[nx][ny]:
                        continue

                    # 배추가 없는땅
                    if arr[nx][ny] == 0:
                        continue

                    # 문제없으면 방문체크후 큐에넣기
                    visited[nx][ny] = True
                    q.append((nx, ny))

            # 문제없으면 하나의 영역으로 처리
            result += 1

    # 필요한 최소 지렁이 수 =?
    print(result)
