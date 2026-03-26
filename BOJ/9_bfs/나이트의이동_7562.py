# BOJ 7562: 나이트의 이동 S1
# 26.03.26
"""
생각1.
방문할 곳 x가 이미 다른 경로에서 방문한곳(이동값=3)이고
나는 그 장소x에 2번의 이동으로 갈수있다면, 왜 다시 방문하면 안되는거?
- 큐에 쌓이는 순서는 무조건 거리순
- BFS에서 어떤칸을 최초로 밟았다면, 그게 무조건 가장 짧은 최단경로
    (단, 모든 가중치가 같을때만)


"""

import sys

input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    # 한변의 길이
    L = int(input())
    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())

    # 이동횟수마다 ++
    board = [[0] * L for _ in range(L)]
    dist = [[-1] * L for _ in range(L)]
    q = deque()

    # 8방향 이동
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    # 시작점 큐에넣기
    q.append((cur_x, cur_y))
    dist[cur_x][cur_y] = 0

    # bfs
    while q:
        cx, cy = q.popleft()

        # 도착하면 조기종료
        if cx == tar_x and cy == tar_y:
            break

        # 다음이동방향 탐색
        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]

            # 체스판 벗어남
            if nx < 0 or ny < 0 or nx >= L or ny >= L:
                continue

            # 이미 방문한곳
            if dist[nx][ny] > -1:
                continue

            # 방문처리후 큐에넣기
            # 이동횟수++
            dist[nx][ny] = dist[cx][cy] + 1

            q.append((nx, ny))

    # 각 TC마다 출력
    result = dist[tar_x][tar_y]
    print(result)
