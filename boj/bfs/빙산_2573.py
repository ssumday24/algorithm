# 빙산_2573 -G4
# 26.04.01
"""
bfs 문제집
[문풀노트]
1. 모든빙산 동시에 높이감소 업데이트 방법 (동시성 제어)
- 옆칸의 변화가 나한테 영향을 주면 안됨
- <계산>과 <업데이트> 단계 분리

2. 영역개수 세기
- 전체맵 돌면서 visited==0 인곳만 실행, cnt++

3. 다중시작점 bfs ,즉 모든 시작점 전부 큐에넣고 시작하는것과 헷갈리지 않게 주의


"""
import sys
from collections import deque


# 빙산높이 감소
# 모든지점 동시에 높이감소해야함
# 1.감소시킬 값들만 구해두고
# 2.그다음에 업데이트
def reduce_height():
    temp = []

    # 1. 상하좌우 인접0 개수부터 세고 저장
    for cur_x, cur_y in arr_ice:
        # 매 빙산마다 0초기화
        cnt_zero = 0

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if arr[nx][ny] == 0:
                cnt_zero += 1

        # 새로운 temp에저장
        temp.append((cur_x, cur_y, cnt_zero))

    # 2. 모든지점 동시에 높이감소
    for x, y, cnt in temp:
        arr[x][y] -= cnt

        # 높이 음수면 0으로 보정
        if arr[x][y] < 0:
            arr[x][y] = 0


# 모든 빙산지점에서 bfs
# 리턴값: 영역개수
def bfs():
    area = 0  # 빙산 영역 개수
    visited = [[False] * M for _ in range(N)]  # 방문체크용

    # 전체가 아니라 빙산 영역들에서만 탐색해서 영역줄이기
    for i, j in arr_ice:
        # 방문하지 않았을때만
        if visited[i][j]:
            continue

        # 방문체크후 bfs 시작
        q = deque()
        visited[i][j] = True
        q.append((i, j))
        area += 1  # 영역개수 +1

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

                # 바다인곳은 방문x
                if arr[nx][ny] <= 0:
                    continue

                # 방문체크후 큐에넣기
                visited[nx][ny] = True
                q.append((nx, ny))

    return area  # 영역개수 리턴


# 첫 빙산좌표들중에서, 녹은것들 제외하고 다시 업데이트
def find_ice():
    new_arr = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                new_arr.append((i, j))

    return new_arr


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0  # 초기시간 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 첫 시작 : 모든 빙산 위치찾아서 배열에 저장 o(nm)
arr_ice = find_ice()

# 1년마다 매번 bfs 진행
while True:
    year += 1  # 1년증가

    # 빙산높이 감소 o(nm)
    reduce_height()

    # 중요: 빙산높이 감소됐으니 빙산위치도 다시 업데이트
    arr_ice = find_ice()

    # 구역의 개수 bfs로 체크 o(nm)
    area = bfs()

    # 빙산이 다 녹은상황: 영역 0개
    if area == 0:
        print(0)
        break

    # 2개이상으로 분리되면 종료
    elif area >= 2:
        print(year)
        break
