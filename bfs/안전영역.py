# 안전영역
# BOJ 2468 - S1
# 26.05.05
"""
[문풀 노트]
- 배열복사 필요없이, board[i][j] > h 로 안잠기는지 바로 확인

[조건]

"""

import sys
from collections import deque

input = sys.stdin.readline


# 비온후 안잠기는 영역개수 확인
def check(board, h):
    global N

    # 영역개수 cnt
    cnt = 0

    # 원본배열 복사
    new_board = [row[:] for row in board]

    # 모든지점 h 만큼 감소
    for i in range(N):
        for j in range(N):
            new_board[i][j] -= h

            # 음수일때 보정
            if new_board[i][j] < 0:
                new_board[i][j] = 0

    # 영역 개수 체크
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 높이가 자연수고 방문하지 않은곳만 시작점 가능
            if new_board[i][j] > 0 and not visited[i][j]:
                # 방문체크후 큐에넣기
                visited[i][j] = True
                q.append((i, j))
                cnt += 1  # 영역개수 ++

                # bfs 시작
                while q:
                    cx, cy = q.popleft()

                    for dir in range(4):
                        nx = cx + dx[dir]
                        ny = cy + dy[dir]

                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue

                        if visited[nx][ny]:
                            continue

                        if new_board[nx][ny] <= 0:
                            continue

                        # 방문체크,큐에넣기
                        visited[nx][ny] = True
                        q.append((nx, ny))

    return cnt


# N*N matrix
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 안전 영역의 최대 개수
result = 0

# 최대높이
maxval = 0

# 입력의 최대높이 구하기
for row in board:
    for elem in row:
        if elem > maxval:
            maxval = elem


# 각  비의높이가 (0 ~ 최댓값-1) 마다 영역개수 확인
# 비의 높이가 최댓값 만큼 오면 모든값 0, 계산필요x

for height in range(maxval):
    cnt = check(board, height)

    result = max(cnt, result)


# 영역개수 최댓값 출력
print(result)
