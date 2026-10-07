# BOJ 15683 감시
# 10.02
# 시뮬레이선 복습
"""
[조건]
- 0:빈칸 1~5:cctv 6:벽 #:감시영역
- 사각지대 최소크기=?

[문풀 노트]
- 한방향 계속 칠하기,
- x,y,cctv_num = cctv[depth] 연습

"""

import sys

input = sys.stdin.readline


# 감시 영역 전부 적용
# arr=[(x,y,[0,1])]
def apply(arr):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 원본배열 복사
    copied = [row[:] for row in board]

    # (x,y,방향정보[0,1,2]) 에 대해
    for x, y, d_arr in arr:
        # 한방향 쭉 칠하기
        for d in d_arr:
            nx, ny = x, y

            while True:
                nx += dx[d]
                ny += dy[d]

                # 1. 인덱스 벗어나면 종료
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    break

                # 2. 벽만나면 종료
                if copied[nx][ny] == 6:
                    break

                # 감시영역으로 변경
                # 다른cctv 만나도 덮이지 않게 빈칸일때만
                if copied[nx][ny] == 0:
                    copied[nx][ny] = "#"

    return copied


# 안전영역 계산
def calc(arr):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


# 백트래킹
def backtr(depth):
    global result

    # 다 골랐으면 계산
    if depth == len(cctv):
        # 1. 감시영역 전부 방향대로 적용
        copied = apply(selected)

        # 2. 안전영역 계산후 업데이트
        result = min(calc(copied), result)

        return

    # 현재cctv 좌표,번호 꺼내기
    x, y, cctv_num = cctv[depth]

    # cctv 방향 선택
    # dir[cctv_num] =[[0],[1],[2],[3]] 이므로  i값 자체가 [0] 형태
    for i in dir[cctv_num]:

        # 좌표+방향 정보
        selected.append((x, y, i))

        # 다음깊이
        backtr(depth + 1)

        # 상태복구
        selected.pop()

    return


# 메인
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = N * M  # 사각지대 최소크기

# cctv 모아둔 배열 (i,j,번호)
cctv = []

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv.append((i, j, board[i][j]))

# 0:상 1:우 2:하 3:좌
dir = [
    [0],  # 0번- 사용x
    [[0], [1], [2], [3]],  # 1번
    [[0, 2], [1, 3]],  # 2번
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 4번
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번
    [[0, 1, 2, 3]],
]

# 방향선택까지 완료한 cctv 정보
selected = []

#
backtr(0)
print(result)
