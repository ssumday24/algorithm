# BOJ 14500
# 테트로미노 -G4
# 26.03.29
"""
백트래킹/DFS/구현

# 1. 가지치기 아이디어 외우기

# 2. 차원배열 최대값 빠르게 구하기
max_board_val = max(map(max, board))

# 3. 시간복잡도
dfs 경우의수 = 4x3x3x3=36 + 마지막 도형 4가지 = 40
=> (N x M x 40) , 최대 500x500x40 = 10^7 연산
=> O(NM)

"""
import sys
from collections import deque

input = sys.stdin.readline


# total = 현재깊이까지 고른수들의 합
def backtr(depth, total, cur_x, cur_y):
    global maxval  # 외부변수 수정

    # 가지치기 아이디어 추가:
    # 남은 블록을 다 최댓값으로 먹어도 현재 maxval을 못 넘으면 가지치기
    if total + max_board_val * (4 - depth) <= maxval:
        return

    # 4개고르면 종료
    if depth == 4:
        # 최대값 갱신
        maxval = max(maxval, total)

        return

    # 상하좌우 이동가능
    for d in range(4):
        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        # 배열벗어나면 선택불가
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        # 이미 방문한곳
        if visited[nx][ny]:
            continue

        # 방문체크(숫자 고른후 ) 다음깊이
        visited[nx][ny] = True
        backtr(depth + 1, total + board[nx][ny], nx, ny)

        # 되돌아왔으면 상태복구
        visited[nx][ny] = False


# 마지막 ㅗ 도형합 계산
def calc_sum(cur_x, cur_y, skip):
    # 시작점 더하고 시작
    result = board[cur_x][cur_y]

    # 1.십자가모양
    for d in range(4):
        if d == skip:
            continue

        nx = cur_x + dx[d]
        ny = cur_y + dy[d]

        # 이 모양으로는 어차피 못만듦
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            return 0

        result += board[nx][ny]

    return result


# 메인 시작
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
maxval = 0  # 구하는값

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_board_val = max(map(max, board))


# 방문체크 배열
visited = [[False] * M for _ in range(N)]

# 각 칸마다 테트로미노 대보기
for i in range(N):
    for j in range(M):
        # 시작점 방문체크
        visited[i][j] = True

        # 백트래킹 시작
        backtr(1, board[i][j], i, j)

        # 백트래킹 끝나면 시작점도 돌려놓기
        visited[i][j] = False

        # 위에서 4가지 종류 끝났으면
        # ㅜ 모양합 계산, 십자가에서 한방향만 제외
        for skip in range(4):
            maxval = max(maxval, calc_sum(i, j, skip))


# 결과
print(maxval)
