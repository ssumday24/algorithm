# BOJ 3190_뱀 - G4
# 26.03.23 - 70분
import sys

input = sys.stdin.readline
from collections import deque

"""
1. BFS,시뮬레이션은 무조건 0-indexed, 초기값 -1 채우기
2. DP 처럼 n번째... -> 1-indexed

- X초가 끝난 직후 => 정확히 

"""
N = int(input())  # N*N
K = int(input())  # 사과 개수

# 0-indexed 로 일단 설계
arr = [[0] * (N) for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    arr[R - 1][C - 1] = "A"  # 1->0 인덱스화

L = int(input())  # 뱀 방향 변환 횟수
arr_xc = []


for _ in range(L):
    # X초가 "끝난 뒤에" 90도방향회전
    # C == L : 왼쪽   C== 'D' 오른쪽
    X, C = input().split()
    arr_xc.append((int(X), C))

# 뱀 (0,0) ,몸길이 1 시작
arr[0][0] = "S"
cur_x = 0
cur_y = 0
time = 0  # 끝나는 시간

# 뱀의 위치 저장
snake = deque()
snake.append((0, 0))

# 상/우/하/좌 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1  # 처음: ->방향

while True:
    # 어느 방향 이동인지 dir값 정하기
    for elem_x, elem_c in arr_xc:
        # 그 시간이 되면 회전
        if elem_x == time:
            # 반시계 90도
            if elem_c == "L":
                if dir == 0:
                    dir = 3
                else:
                    dir = dir - 1

            # 시계방향 90도
            if elem_c == "D":
                # 끝인덱스 도달하면 다시 처음으로
                dir = (dir + 1) % 4

    # 1.다음칸 이동
    cur_x += dx[dir]
    cur_y += dy[dir]

    # 2-2. 벽에부딪힐때 - 인덱스범위부터 검사
    if cur_x < 0 or cur_y < 0 or cur_x >= N or cur_y >= N:
        time += 1
        break

    # 2-1. 자기몸에 부딪힐때
    if arr[cur_x][cur_y] == "S":
        time += 1
        break

    # 3. 사과가 있으면
    if arr[cur_x][cur_y] == "A":
        # 사과없애고, 꼬리움직이지않음
        arr[cur_x][cur_y] = "S"
        snake.append((cur_x, cur_y))

    # 4. 사과가 없으면
    else:
        # 몸길이 줄여서 꼬리칸 비워주기
        rem_x, rem_y = snake.popleft()
        arr[rem_x][rem_y] = 0

        # 현재칸으로 이동
        arr[cur_x][cur_y] = "S"
        snake.append((cur_x, cur_y))

    # 5. 1초증가
    time += 1

    # 디버깅
    # print(f"{time}초때 배열:")
    # print(*arr, sep="\n")


# 결과출력
print(time)
