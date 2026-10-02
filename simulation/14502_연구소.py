# BOJ 14502 연구소
# 26.09.30 - 복습
"""
[조건]
- 벽3개 전부 세워야함
- 1:벽 2:바이러스
- 안전영역 크기의 최댓값=?

[문풀 노트]
# 배열 복사 판단
- 판단기준
    - 변경한 상태를 쉽게 되돌릴 수 있는가?
    -> 복구 비용이 O(1) 처럼 저렴한가?
    - BFS 등 변경후 회복이 어렵다면 복사필요.

- 벽3개를 고르는건, 순서바뀌어도 똑같은 경우므로 조합 사용

# 2차원 배열을 1차원으로 피는 방법

# visited가 필요 없는 이유
 BFS 과정에서 빈칸 0을 바이러스 2로 즉시 변경하기 때문에 배열 값 자체로 이미 방문한 칸인지 구분가능
 그러니 별도의 visited 배열 없이도 각 칸은 최대 한 번만 큐에 들어감

"""

import sys

input = sys.stdin.readline
from collections import deque


def bfs(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    # 시작점 찾아서 전부 방문체크후 큐에넣기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))

    # bfs시작
    while q:
        cur_x, cur_y = q.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            # idx체크
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽 또는 바이러스 이미 있는곳은 못감
            if arr[nx][ny] != 0:
                continue

            # 큐에넣기
            q.append((nx, ny))

            # 바이러스 이동
            arr[nx][ny] = 2


def backtr(depth, start):
    global result

    # 3개선택시 계산
    if depth == 3:

        # 1.바이러스 bfs
        # bfs는 상태복구 힘드니 복사배열 사용
        copied = [row[:] for row in board]
        bfs(copied)

        # 2.안전영역 계산후 업데이트
        cnt = 0

        for row in copied:
            for elem in row:
                if elem == 0:
                    cnt += 1

        result = max(cnt, result)

        # 계산후종료
        return

    # 조합 -> start 인덱스부터 선택
    for i in range(start, len(empty)):
        # 벽 고르기
        x, y = empty[i]

        board[x][y] = 1

        # 다음깊이
        # 조합이니 empty[i+1] 칸부터 고르면 됨
        backtr(depth + 1, i + 1)

        # 상태복구
        board[x][y] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0  # 안전영역의 크기

empty = []  # 빈칸만 모아둘 배열
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))


backtr(0, 0)

print(result)


==
