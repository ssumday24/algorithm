# 9251 - LCS 
# 여러개의 하위문제를 먼저 푼뒤 / 그 결과를 쌓아올려 /주어진 문제를 해결
import sys
input = sys.stdin.readline


x = input().strip()
y = input().strip()

n = len(x)
m = len(y)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
