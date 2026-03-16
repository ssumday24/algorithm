# BOJ 12865
# 평범한배낭  - G5
# 26.03.13
# 26.03.16
"""
[WIL]

dp[i][j]= i번째 짐까지 골랐을때 가치합의 최댓값,
단 j= 가방의한도.

예제를 적용하면
1. i번째 짐을 안골랐다면,
dp[4][7]=dp[3][7]

2. i번째 짐을 골랐다면,
dp[4][7]=max(dp[3][7],dp[3][7-5(W)]+12(V))


O(NK) =
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# (N+1)*(K+1), 0패딩
dp = [[0] * (K + 1) for _ in range(N + 1)]

# i:1~N
for i in range(1, N + 1):
    W, V = map(int, input().split())  # 무게w,가치v

    # j=1 ~ K 채우기
    for j in range(1, K + 1):

        # 예외처리
        # 인덱스가 음수가 될때
        # 이번 물건은 무조건 못담는게 확정이므로
        if j - W < 0:
            dp[i][j] = dp[i - 1][j]
            continue

        # i번쨰 물건을 안골랐으면 dp[i-1][j]
        # i번째 물건을 골랐다면,dp[i-1][j-W]+V 이므로
        # 둘중 큰값으로 기록
        dp[i][j] = max(dp[i - 1][j], dp[i-1][j - W] + V)


# 출력부분
# N개까지 전부골랐을때,무게한도=K일때
print(dp[N][K])
