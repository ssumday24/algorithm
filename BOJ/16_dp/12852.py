# BOJ 12852
# 1로 만들기(2) - G5
# 26.03.12
import sys

input = sys.stdin.readline

"""
DP문제(7) - 1로만들기(1) #1463 + 경로복원
[WIL]
- "경로복원": 경로복원용 테이블 필요
- trace[i] : "바로 직전에 어디에서 왔는지" 기록 

dp[i]=1이될때까지 연산수의 최솟값
"""
N = int(input())
dp = [0] * (N + 1)
trace=[0]*(N+1)

# dp[2]~dp[N] 구하기
for i in range(2, N + 1):
    dp[i] = 1 + dp[i - 1]
    trace[i]=i-1

    if i % 2 == 0 and 1+dp[i//2] < dp[i]:
        dp[i] = min(dp[i], 1 + dp[i // 2])
        trace[i]=i//2
    
    if i % 3 == 0 and 1+dp[i//3]<dp[i]:
        dp[i] = min(dp[i], 1 + dp[i // 3])
        trace[i]=i//3

#출력부분
print(dp[N])

while (N>=1):
    print(N,end=' ')
    if N==1:
        break
    N=trace[N]