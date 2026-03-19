# BOJ 15683
# 감시 - G3
# 26.03.01
# 26.03.18
"""
# [03.01]
- 배열 복사 ([row[:] for row in current_arr])
-원본배열 쓰지않는건 상태복원이 어려우니까 임시배열쓰고 버리기
- 시계방향으로 0,1,2,3 맞추면 회전로직짤때 편함
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

# [03.19]
- 튜플원소 순회하며 칠하기
[(0,), (1,), (2,), (3,)]
예를들어 (1) 처럼 원소가 하나에 쉼표가 없으면 일반 정수로 처리되니
쉼표 필수
- 파이썬의 기본값은 수학 괄호() 이므로 튜플이아닌, 정수로 처리되는것

"""
import sys

input = sys.stdin.readline


# 0:상 1:우 2:하 3:좌
def draw(dir, arr, ct_x, ct_y):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 각 i: 한 방향마다 전부칠하기
    # dir:(0,2)등 튜플
    for i in dir:
        nx = ct_x
        ny = ct_y

        # 한 방향 num을 정하고 전부  칠하기
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break

            # 벽을 만나면 종료
            if arr[nx][ny] == 6:
                break

            # 빈곳만 감시
            if arr[nx][ny] == 0:
                arr[nx][ny] = "#"


# 각 경우의수 구하기
def backtr(depth, arr):
    global result  # result 전역변수로 수정

    # K개 모두정하면 사각지대 계산
    if depth == K:
        area = 0
        for row in arr:
            for x in row:
                if x == 0:
                    area += 1

        # 사각지대 최소값 갱신
        result = min(result, area)

        return

    # 1. depth 번째 ct 정보 꺼내기
    ct_x, ct_y, ct_num = arr_ct[depth]

    # 2. ct 번호에 따른 방향 확정하기 ex) dir은 [(0,2),(1,3)] 순회
    for dir in arr_choice[ct_num]:

        # 3. 복사배열 만들기
        copied_arr = [row[:] for row in arr]

        # 4. 그 방향을 전부 '#' 으로 칠하기
        draw(dir, copied_arr, ct_x, ct_y)

        # 5. 다음 CCTV 고르기
        backtr(depth + 1, copied_arr)

        # 상태복구: 원본배열 수정없이 넘겼으니 필요없음


# main
# N*M 사무실
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 사각지대의 크기 result
result = 9999

# CCTV 개수 K (K<=8)
K = 0

#  cctv의  좌표+ cctv 번호 모아둔 배열
arr_ct = []

for i in range(N):
    for j in range(M):
        # cctv 좌표+ 번호만 튜플로 모아서 따로 기록
        if board[i][j] >= 1 and board[i][j] <= 5:
            arr_ct.append((i, j, board[i][j]))
            K += 1

# 각cctv의 방향 가짓수 표현
arr_choice = [
    [0],  # 제로패딩 사용x
    [(0,), (1,), (2,), (3,)],  # 1번
    [(0, 2), (1, 3)],  # 2번
    [(0, 1), (1, 2), (2, 3), (3, 0)],  # 3번
    [(0, 1, 3), (0, 1, 2), (1, 2, 3), (2, 3, 0)],  # 4번
    [(0, 1, 2, 3)],  # 5번
]


# 출력
backtr(0, board)
print(result)
