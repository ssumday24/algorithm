# BOJ 11660
# 구간합 구하기5 - S1
# 26.03.12
import sys

input = sys.stdin.readline
"""
N*N (x1,y1)~(x2,y2)

[WIL]
- "2차원" 누적합: 사각형 넓이 오려내기 
- dp[i][j]= (1,1)~(i,j)까지 직사각형 영역 전체의 수의 합
- 이제부터는 0-index 아닌 padding 붙여서 1-index로 풀기

"""
N, M = map(int, input().split())
board = [[0] * (N + 1)]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    board.append(row)

# 사용 idx : 1~N
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S1 = dp[i - 1][j]  # 위쪾 직사각형
        S2 = dp[i][j - 1]  # 왼쪽 직사각형
        S3 = dp[i - 1][j - 1]  # 겹치게 더해진 영역
        dp[i][j] = S1 + S2 - S3 + board[i][j]


# M번시행
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    S1 = dp[x1 - 1][y2]
    S2 = dp[x2][y1 - 1]
    S3 = dp[x1 - 1][y1 - 1]
    result = dp[x2][y2] - S1 - S2 + S3
    print(result)
