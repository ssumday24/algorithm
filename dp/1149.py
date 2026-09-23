# BOJ 1149
# RGB거리 - S3
# 26.03.09
"""
DP연습문제(4) -2차원
[WIL]
-미래를 미리 걱정 XXXXXXXXX
-과거 말고, '지금 내 색깔'을 고정
- DP에서 상태(j)를 정의할 때는 "내가 과거에 뭘 했는가"보다
"지금 나의 상태가 무엇인가"
- board,DP 초기화: [0,0,0] 1차원, [[0,0,0]] 2차원 실수조심

dp[i][j]= i번째까지 칠했을때 최소비용. 단, j는 현재집의 색깔
j=0:R,1:G, 2:B
"""

import sys

input = sys.stdin.readline
N = int(input())
board = [[0, 0, 0]]  # 0번 row 사용x
dp = [[0, 0, 0]]  # 0번 row 사용x , board와 맞추기.
result = 0  # 최솟값


"""
board = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
"""
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    dp.append([0, 0, 0])
# idx 0 : 빨강R, 1: 초록G , 2:파랑B


# 초기값
dp[1][0] = board[1][0]
dp[1][1] = board[1][1]
dp[1][2] = board[1][2]

# 점화식
for i in range(2, N + 1):

    # i-1: G,B 가능
    dp[i][0] = board[i][0] + min(dp[i - 1][1], dp[i - 1][2])

    # i-1: R,B 가능
    dp[i][1] = board[i][1] + min(dp[i - 1][0], dp[i - 1][2])

    # i-1: R,G 가능
    dp[i][2] = board[i][2] + min(dp[i - 1][0], dp[i - 1][1])

# 최종 출력
result = min(dp[N][0], dp[N][1], dp[N][2])
print(result)

# print(dp)
