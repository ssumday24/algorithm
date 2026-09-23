# BOJ 16234
# 인구이동 - G4
# 26.04.15 - 40분 타이머
"""
[문제조건]
- 인구이동 없을때까지 지속
1. L<= 인구차이<=R : 하루동안 국경선 열기
2. 국경선 열려있으면 => 오늘 하루동안 연합
3. 연합의 인구수 = (연합총 인구수) / (연합칸수) -> 소수점 버림
4.연합을 해체하고 모든 국경선  닫기

[문풀 노트]
- 전부 끝난뒤 업데이트 <-> 바로 업데이트 가능한 경우인지?
- 이문제에서는 바로 업데이트 가능
    - 연합A를 찾으면 연합B에 절대로 속하지않으니까 괜찮음

"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j):
    global moved

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐만들기
    q = deque()

    # 방문체크 + 큐에넣기
    q.append((i, j))
    visited[i][j] = True

    # 시작점 계산
    tot = board[i][j]
    country = [(i, j)]

    while q:
        cur_x, cur_y = q.popleft()

        # 상하좌우 탐색
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            # 차이가 L~R 사이면 이동가능
            # 인구이동 플래그 설정
            if L <= abs(board[cur_x][cur_y] - board[nx][ny]) <= R:

                # 플래그 -> 종료조건에 사용
                moved = True

                # 방문체크후 큐에넣기
                q.append((nx, ny))
                visited[nx][ny] = True

                # 인구수 합산
                tot += board[nx][ny]

                # 위치기록
                country.append((nx, ny))

    # 이동 없었으면 계산안하고 종료
    if len(country) <= 1:
        return

    # 연합인구 - 소수점 버림
    each_val = tot // len(country)

    # 인구 수정
    for i, j in country:
        board[i][j] = each_val

    return


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0  # 0일 초기값

while True:
    # 인구이동 플래그
    # 종료조건 : 인구이동 없을때
    moved = False

    # 방문체크
    visited = [[False] * (N) for _ in range(N)]

    # 인구이동 시작
    for i in range(N):
        for j in range(N):
            # 영역 개수세기와 같음
            if not visited[i][j]:
                # 한 영역마다 bfs 진행
                bfs(i, j)

    # 인구이동 없으면 종료
    if not moved:
        break

    # 1일++
    result += 1

# 결과출력
print(result)
