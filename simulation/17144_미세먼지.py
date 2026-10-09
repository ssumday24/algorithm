# BOJ 17144 미세먼지 -G4
# 10.09
# 시간:
"""
[노트]
- shift 연산 규칙 : 도착점부터 바꾸기
- case) 두 미세먼지가 붙어있을때? ******

[조건]
#1.먼지 확산
- 미세먼지 확산 : 1/5 씩, 소수점버림
- (R,C)에 남은량 : A - (0.2 A * 확산된방향개수)

#2.공기청정기
- 위쪽: 반시계 순환
- 아래쪽: 시계방향 순환
- 바람이 불면 한칸씩 이동
- 공기청정기로 들어간 먼지는 모두 정화

#3. T초후 남아있는 미세먼지 총합=?
"""

import sys

input = sys.stdin.readline
from collections import deque

# 1초동안 먼지 확산
"""
문제:
큐에넣고 순서대로 돌려버리면 두 미세먼지가 붙어있을때, 나중에 들어온 원소의 미세먼지값이 달라져서 결과도 달라짐 

해결:
원본 배열은 그대로 두고 복사배열에서 값 변경 

"""


def dust_move():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()  # bfs용 큐

    copied = [row[:] for row in board]  # 원본배열 복사

    # 동시시작 bfs니까 큐에 전부넣기
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                # 큐에넣기
                q.append((i, j))

    """
    확산은 시작점에서 상하좌우 1칸씩으로만 일어나니 큐에 원소를
    더넣을 필요는 없고 방문체크도 필요x
    """
    while q:
        cur_x, cur_y = q.popleft()

        # 먼지 확산될 양 미리 정해둠
        dust = board[cur_x][cur_y] // 5

        # 상하좌우탐색
        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # idx 범위체크
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            # 공기청정기 있는칸 불가
            if board[nx][ny] == -1:
                continue

            # 확산되는칸 board[nx][ny]
            copied[nx][ny] += dust  # 옆칸으로 확산
            copied[cur_x][cur_y] -= dust  # 원본칸은 그만큼 감소

    return copied


def clean_top(start):
    # 청소기 가까운 곳부터 시프트해야 값 안잃어버림

    # down 시프트
    # a[i][0],a[i-1][0] 대입
    for i in range(start - 1, 0, -1):
        board[i][0] = board[i - 1][0]

    # left 시프트 - 맨윗칸임
    for i in range(0, C - 1):
        board[0][i] = board[0][i + 1]

    # top시프트
    for i in range(0, start):
        board[i][C - 1] = board[i + 1][C - 1]

    # right 시프트
    # 공기청정기 시작점인 -1은 옮기면 안되니 i=2일때 옮기고 종료
    for i in range(C - 1, 1, -1):
        board[start][i] = board[start][i - 1]

    # 마지막으로 못옮긴값 초기화
    board[start][1] = 0

    return


# 시계방향
def clean_bot(start):
    # 1.top 시프트
    # i: (start+1) ~ (R-2)
    for i in range(start + 1, R - 1):
        board[i][0] = board[i + 1][0]

    # 2.left 시프트 - 맨아랫칸 고정
    for i in range(0, C - 1):
        board[R - 1][i] = board[R - 1][i + 1]

    # 3.down 시프트
    # i= R-1 ,R-2 , ..... (start+1)
    for i in range(R - 1, start, -1):
        board[i][C - 1] = board[i - 1][C - 1]

    # 4.right 시프트
    # 공기청정기 있는 위치인 -1은 움직이면 안됨
    # i= C-1,C-2,....2
    for i in range(C - 1, 1, -1):
        board[start][i] = board[start][i - 1]

    # a[start][2]=a[start][1]에서 끝났으니
    # 그대로인 a[start][1]값  초기화
    board[start][1] = 0

    return


def clean():
    # 청소기 위치 찾기
    for i in range(R):
        # 처음 발견한 위치가 청소기 위쪽
        if board[i][0] == -1:
            top_x = i
            bot_x = i + 1
            break

    # 위쪽:반시계 순환
    clean_top(top_x)

    # 아래쪽:시계 순환
    clean_bot(bot_x)

    return


# main
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]  # R*C
total = 0  # 미세먼지 총합

# T초 반복
for _ in range(T):

    # 1.미세먼지 확산 - 원본배열 수정
    board = dust_move()

    # 2.청정기 작동
    clean()


# 결과
# 남아있는 미세먼지 총합
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            total += board[i][j]

print(total)


# 디버깅용
print("======")
print(*board, sep="\n")
