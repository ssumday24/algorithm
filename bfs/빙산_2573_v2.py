# 빙산
# BOJ 2573 - G4
# 26.04.01
# 26.05.05
"""
[문풀노트]
1. 모든빙산 동시에 높이감소 업데이트 방법 (동시성 제어)
- 옆칸의 변화가 나한테 영향을 주면 안됨
- <계산>과 <업데이트> 단계 분리

2. 영역개수 세기
- 전체맵 돌면서 visited==0 인곳만 실행, cnt++

3. 다중시작점 bfs ,즉 모든 시작점 전부 큐에넣고 시작하는것과 헷갈리지 않게 주의

[문제 조건]
- 빙산 영역이 2개이상이 되는 최초의 시간=?
- 전부다 녹을때까지 분리안되면 0 출력

"""

import sys
from collections import deque

input = sys.stdin.readline


# bfs - 영역개수
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited = [[0] * M for _ in range(N)]

    area_cnt = 0  # 영역개수

    # bfs 진행
    for x, y in ice:

        # 이미 방문한곳은 스킵
        if visited[x][y]:
            continue

        # 방문체크후 큐에 넣기
        q.append((x, y))
        visited[x][y] = True

        # 영역개수 +1
        area_cnt += 1

        while q:
            cur_x, cur_y = q.popleft()

            # 상하좌우
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if visited[nx][ny]:
                    continue

                # 빈곳이면 탐색x
                if board[nx][ny] <= 0:
                    continue

                # 방문체크후 큐에 넣기
                visited[nx][ny] = True
                q.append((nx, ny))

    return area_cnt


# 빙산 높이 감소
def reduce():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 업데이트 후 ice 배열
    new_ice = []

    # 0개수 저장 배열
    temp = []

    # 각 위치마다 인접한 0의개수 저장
    for x, y in ice:
        zero_cnt = 0

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny] == 0:
                zero_cnt += 1

        # 0개수 저장
        temp.append(zero_cnt)

    # 이제 개별 높이 감소
    # ice, temp 리스트 길이 같으니 문제x
    for i in range(len(ice)):
        # 현재 빙산 좌표
        cur_x, cur_y = ice[i]

        # 감소
        board[cur_x][cur_y] -= temp[i]

        # 음수높이 보정
        if board[cur_x][cur_y] <= 0:
            board[cur_x][cur_y] = 0

        # 얼음인 부분 -> new_ice 추가
        else:
            new_ice.append((cur_x, cur_y))

    # 업데이트된 배열 리턴
    return new_ice


N, M = map(int, input().split())

# N*M
board = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 빙산 위치 정보 업데이트
ice = []

for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            ice.append((i, j))

while True:

    # 영역 개수  체크
    area = bfs()

    # 2개이상이면 종료
    if area >= 2:
        break
    # 다 녹았는데 종료안된경우
    if area == 0:
        result = 0
        break

    # 모든 빙산높이 동시에 감소 +  빙산 업데이트
    ice = reduce()

    # 1년 증가
    result += 1


# 출력
print(result)
