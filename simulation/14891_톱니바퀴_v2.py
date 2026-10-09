# BOJ 14891 톱니바퀴
# 03.26 - 10.09 복습
# 14891 → 14499 → 17144
"""
[노트]
- 배열 shift
- 조건부 상태전파 연습
- 판단과 실행단계를 분리하기

[조건]
- 맞닿은 극의 방향이 다르면 ,B는 A와 반대방향으로 회전
- 초기상태 + 회전방법 -> 최종 상태=?

N극:0  S극:1
K:회전횟수
1: 시계 / -1:반시계
"""

import sys

input = sys.stdin.readline
from collections import deque


def clock(n):
    # 시계방향 회전 == 배열 오른쪽 shift
    # [1,2,3,4] -> [4,1,2,3]

    temp = board[n][7]

    for i in range(7, 0, -1):
        board[n][i] = board[n][i - 1]

    board[n][0] = temp

    return


def counter_clock(n):
    # 반시계 회전 == 배열 왼쪽 shift
    # [1,2,3,4] -> [2,3,4,1]

    temp = board[n][0]

    for i in range(0, 7, +1):
        board[n][i] = board[n][i + 1]

    board[n][7] = temp

    return


# 회전할 톱니번호 + 방향 결정
def get_dir(start, direction):
    info = [0, 0, 0, 0, 0]  # 1~4 idx 사용 , 1:시계 -1:반시계

    # 1.시작점 회전여부+방향 정하기
    info[start] = direction

    # 2. 왼쪽바퀴 회전여부+방향
    # i: start부터 시작해서 왼쪽으로 계속 전파
    # (1번,2번) 바퀴까지 탐색
    for i in range(start, 1, -1):
        # 극이 다를때만 반대로 회전
        if board[i][6] != board[i - 1][2]:
            info[i - 1] = info[i] * (-1)

        # 중요: 극이 같으면 더 비교하지 않게 끊어야함
        else:
            break

    # 3. 오른쪽바퀴 체크
    # (3번,4번) 바퀴까지 계속 탐색
    for i in range(start, 4):
        # 극이 다를때만 반대로 회전
        if board[i][2] != board[i + 1][6]:
            info[i + 1] = info[i] * (-1)

        # 중요: 극이 같으면 더 비교하지 않게 끊어야함
        else:
            break

    return info


# 메인
# 1~4번바퀴 , 1-idx 사용
board = [[0, 0, 0, 0, 0, 0, 0, 0]]
for _ in range(4):
    row = list(map(int, input().strip()))
    board.append(row)

K = int(input())


for _ in range(K):
    # ex) 3, -1 : 3톱니바퀴를 시계반대로 회전
    start, dir = map(int, input().split())

    # 회전할 톱니번호 + 방향 결정
    info = get_dir(start, dir)

    # i번째 톱니바퀴를 시계/반시계 회전
    for i in range(1, 5):
        if info[i] == 1:
            clock(i)
        elif info[i] == -1:
            counter_clock(i)


# 결과
# s극이면 값이1, 점수 가중치 그대로 곱하기
print(board[1][0] + 2 * board[2][0] + 4 * board[3][0] + 8 * board[4][0])
