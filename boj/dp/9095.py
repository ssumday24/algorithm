# BOJ 9095
# 1,2,3 더하기 - S3
# 26.03.07
import sys

input = sys.stdin.readline
"""
DP연습문제(2)
DP: 테이블 정의 -> 점화식 찾기 -> 초기값 설정 
"""
def func(N):
    """
    dp[i]: 정수i를 1,2,3의 합으로 나타내는 경우의수 (순서고려)
    
    1로 시작하는 경우+dp[i-1]
    2로 시작하는 경우 + dp[i-2]
    3으로 시작하는 경우+dp[i-3]
    위 세가지는 겹치는경우 없이 고유하므로 
    dp[2]=dp[i-1]+dp[i-2]+dp[i-3]
    """
    for i in range(4,N+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


#main
T= int(input())
dp=[0]*(11) # idx : 1~N 사용,  1<= n <=10
dp[1]=1
dp[2]=2
dp[3]=4

func(10)

for _ in range(T):
    N=int(input()) 
    print(dp[N])