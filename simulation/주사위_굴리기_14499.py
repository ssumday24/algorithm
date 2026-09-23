# 14499.주사위 굴리기
# 26.03.27
"""
[문제조건]
- 주사위 이동했을때마다 상단에 있는 값=?
- 주사위는 지도바깥 이동불가, 바깥이동 명령은 무시

[문풀 WIL]
- 배열 shift 심화
    - temp값 여러개 필요하면 temp=dice[:] 로 백업
    - 파이썬은 다중할당으로 한줄에 가능하지만 직접 연습하기
"""

import sys
from collections import deque

input = sys.stdin.readline


# 1:동 / 2:서 / 3:북 / 4:남
def move_next(x, y, dir):
    # 1~4번만 사용
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    # 다음 이동좌표
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        # 이동실패 명령무시 + 출력x
        return (False, x, y)

    # 주사위 위치재배치
    # dice = [상0/하1/좌2/우3/앞4/뒤5]

    # 배열 시프트때 값 덮어쓰기 방지 -> 복사배열 만들기
    temp = dice[:]

    # 동: 앞4뒤5 그대로
    if dir == 1:
        dice[0] = temp[2]  # 좌->상
        dice[1] = temp[3]  # 우->하
        dice[2] = temp[1]  # 바닥-좌
        dice[3] = temp[0]  # 상-우

    # 서: 앞4 뒤5 그대로
    elif dir == 2:
        dice[0] = temp[3]  # 상<-우
        dice[1] = temp[2]  # 하<-좌
        dice[2] = temp[0]  # 좌<-상
        dice[3] = temp[1]  # 우<-바닥
    # 북: 좌2 우3 그대로
    elif dir == 3:
        dice[0] = temp[4]  # 상<-앞
        dice[1] = temp[5]  # 하<-뒤
        dice[4] = temp[1]  # 앞<-아래
        dice[5] = temp[0]  # 뒤<-위

    # 남: 좌2 우3 그대로
    elif dir == 4:
        dice[0] = temp[5]  # 상<-뒤
        dice[1] = temp[4]  # 하<-앞
        dice[4] = temp[0]  # 앞<-위
        dice[5] = temp[1]  # 뒤<-아래

    # 이동한 칸에 쓰여 있는 수가 0이면,
    if board[nx][ny] == 0:
        # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        board[nx][ny] = dice[1]

    # 0이 아닌 경우
    else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
        dice[1] = board[nx][ny]

        # 칸에 쓰여 있는 수는 0이 된다.
        board[nx][ny] = 0

    # 이동성공
    return (True, nx, ny)


# main
# N*M 지도  / 주사위 좌표(x,y) / 명령개수 K
# N,M : 자연수 / x,y: 인덱스 /
N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 이동명령 모음
# 1:동 / 2:서 / 3:북 / 4:남
move_arr = list(map(int, input().split()))

# 주사위 초기값 0
# 각 상/하/좌/우/앞/뒤
dice = [0, 0, 0, 0, 0, 0]

# 현재위치 - 시작점(x,y)부터 시작
cur_x = x
cur_y = y

# 각 이동마다 주사위 윗면의 수 출력
for dir in move_arr:

    is_move, cur_x, cur_y = move_next(cur_x, cur_y, dir)

    # 못움직이면 다음명령 진행
    if not is_move:
        continue

    # 출력 - 주사위 윗면값
    print(dice[0])
