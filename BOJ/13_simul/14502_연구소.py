# BOJ 14502
# 연구소-G4
# 26.03.21
"""
시뮬레이선 문제집
[WIL]
- 감시CCTV 문제와 비슷한점
- BFS 방향볼때 i말고 d로 쓰기
    - (다중반복문 안에서 충돌 #1012 유기농배추 참조 )
- 시간복잡도 O(N^4 M^4)

생각1.
- 벽 만드는건상태복구가 엄청 간단하니까 배열복사x
- BFS에 의해 바이러스가 퍼진건 복구 어려우니 배열복사
- 순열->조합 으로 중복탐색 줄이기

2. n과m(10)다시 생각
arr=배열복사(1)
for i in range(N):
        for j in range(M):
            arr=배열복사(2)
반복문 밖인 1번위치에서 복사하면 문제생기나?


3. visited배열안쓰고 이문제에서는 arr[nx][ny]=2 로해도 되나?
- 유기농 배추 문제처럼 바이러스가 빈칸을 오염시키면서 퍼져나가기때문에
if arr[nx][ny]==0 조건 체크면 vis 따로 필요없음.

- 반면에 #5427 불 문제처럼 "여러 종류가 동시에" 움직일때는
데이터가 충돌하니 배열 따로 만들어서 관리필요
"""
"""
설계 순서
r1. 벽은 무조건3개사용
r2. 안정영역 (0의개수) 최대=> bfs+백트래킹 

p1. 벽 3개 세우기 (백트래킹 깊이3)
p2. 바이러스 bfs 돌리기
p3. 안전영역 계산후 업데이트

"""
import sys

input = sys.stdin.readline
from collections import deque


# 벽 3개 세우기
def backtr(depth, start_i, start_j):
    global result  # 함수안에서 result값 수정

    if depth == 3:
        # 바이러스만 bfs
        # 바이러스 퍼진건 복구 어려우니 배열복사 nm
        new_arr = [row[:] for row in board]
        bfs(new_arr)

        # 안전영역 계산
        # 최댓값이면 업데이트
        tempval = calc(new_arr)

        if tempval > result:
            result = tempval

            # # 디버깅
            # print("=========")
            # print(*new_arr,sep="\n")

        return

    # 순열x->조합, 중복탐색줄이기
    for i in range(start_i, N):
        """
        2차원배열로 조합 로직 구현:
        줄바꿈이 생기면 j=0 으로 돌아가야하니 start_j부터
        무작정 시작하면 안됨
        """
        # 줄바꿈 일어나기전 첫 줄에서만 start_j부터 시작
        if i == start_i:
            start_col = start_j

        # 다음줄부터는 처음부터시작
        else:
            start_col = 0

        for j in range(start_col, M):

            # 벽,바이러스인곳은 못세움
            if board[i][j] == 1 or board[i][j] == 2:
                continue

            # 벽 세우기
            board[i][j] = 1

            # 백트래킹 다음깊이
            backtr(depth + 1, i, j)

            # 상태복구- 벽 없애기
            board[i][j] = 0


# 바이러스 bfs
# 최대 O(NM)
def bfs(arr):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()

    # N*M 방문체크 =>이문제 필요x  이유생각
    # visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 바이러스 좌표 큐에 넣기 - 모든 시작점
            if arr[i][j] == 2:
                q.append((i, j))

    while q:
        cur_x, cur_y = q.popleft()

        # 상하좌우
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 배열벗어날때
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽이 있는곳,바이러스 이미퍼진곳 못감
            if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                continue

            # 큐에넣기 + 바이러스 퍼진것 적용
            q.append((nx, ny))

            # 2로하는게 최선? 아니면 다른수로하는게좋을까
            arr[nx][ny] = 2


# 안전영역 계산
# o(NM)
def calc(arr):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    return cnt


# N*M
N, M = map(int, input().split())

# 0-indexed
board = [list(map(int, input().split())) for _ in range(N)]

# 안전영역
result = 0

# 백트래킹 시작
# start_x,y :(0,0) 시작
backtr(0, 0, 0)

# 결과 출력
print(result)
