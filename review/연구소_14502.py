# BOJ 14502
# 연구소
# 26.03.21
# 26.04.04 복습 - 25분소요
"""
[문제조건]
0 빈칸 / 1 벽 / 2 바이러스
벽은 무조건 3개만 세우기
안전영역 최대로 고르기

[문풀 노트]
1.벽을 골랐으면 원본 배열1로 수정 / 상태복구 1->0
=> 치킨문제에서는 왜 이렇게하면X?

"""
import sys
from collections import deque

input = sys.stdin.readline


# visited 없이 진행
def bfs(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 모든 바이러스에서 동시에 전파
    # 큐에 전부다넣기
    q = deque()
    for x, y in virus:
        q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        # 상하좌우 퍼져나감
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽이나 바이러스면 이동불가
            if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                continue

            # 바이러스 퍼짐
            arr[nx][ny] = 2
            q.append((nx, ny))  ###추가

    # 2.안전구역 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    return cnt


# 빈칸 3개 고르기
def backtr(depth, start):
    global result

    if depth == 3:
        # 1.바이러스 전파bfs
        # 원본 오염 안되게 복사후 계산
        copy = [row[:] for row in board]
        cnt = bfs(copy)

        # 최대값이면 업데이트
        result = max(cnt, result)

        return

    # 조합, 중복되지않게 고르기
    for i in range(start, len(vacant)):
        # 빈곳 위치 꺼내기
        cur_x, cur_y = vacant[i]

        # 벽선택 : 0->1
        board[cur_x][cur_y] = 1

        # 다음깊이 , i+1 idx부터 고르기
        backtr(depth + 1, i + 1)

        # 벽선택 상태복구 : 1->0
        board[cur_x][cur_y] = 0


N, M = map(int, input().split())
# N*M 행렬
board = [list(map(int, input().split())) for _ in range(N)]
result = 0  # 결과 최댓값


vacant = []  # 빈칸 좌표 모아둔 배열
virus = []  # 바이러스 위치만

for i in range(N):
    for j in range(M):
        # 빈칸
        if board[i][j] == 0:
            vacant.append((i, j))

        # 바이러스
        elif board[i][j] == 2:
            virus.append((i, j))


# 백트래킹, 벽3개선택
# 조합 start=0 시작
backtr(0, 0)

# 결과
print(result)
