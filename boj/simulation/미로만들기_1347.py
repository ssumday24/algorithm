# 1347:미로만들기
# 26.03.28
"""
[문제조건]
시작방향남쪽
F=한칸 움직임
L,R = 왼/오 방향 전환 (위치는 그대로)

[메모]
- 바운딩 박스 연습
    - 필요한 부분만 오려내기
    - min,max 사용
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(input().strip())

# 움직인 횟수<50 이므로 최대크기 101*101
board = [["#"] * (101) for _ in range(101)]

# 시계방향순, 12-3-6-9
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 남쪽보고 시작
dir = 2

# 시작점 모르니 정중앙 시작
cur_x = 50
cur_y = 50

# 시작점 체크
board[cur_x][cur_y] = "."


min_x, min_y = 50, 50
max_x, max_y = 50, 50

# 노트내용 진행
for x in arr:
    # 오른쪽회전
    if x == "R":
        dir = (dir + 1) % 4

    # 왼쪽회전
    elif x == "L":
        dir = (dir + 3) % 4

    # 이동 진행
    elif x == "F":
        cur_x += dx[dir]
        cur_y += dy[dir]

        # 이동한곳 표시
        board[cur_x][cur_y] = "."

        # 바운딩 박스 갱신
        # 처음 가보는 곳이라면 넓히기
        min_x = min(cur_x, min_x)
        min_y = min(cur_y, min_y)

        max_x = max(cur_x, max_x)
        max_y = max(cur_y, max_y)


# 지도 출력
# 1.바운딩 박스 내부에서만,
# 2. 이동한 '.' 이 있는 행만 출력
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        print(board[i][j], end="")
    print()
