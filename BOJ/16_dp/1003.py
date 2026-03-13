# BOJ 1003
# 피보나치함수 - S3
# 26.03.13
import sys

input = sys.stdin.readline
"""
f(0)=0, (x,y)=(1,0)
f(1)=1, (x,y)=(0,1)
f(2)=f(1)+f(0) (1,1)
f(3)=f(2)+f(1) (1,2)

dp[i][0]=f(i) 0 출력횟수
dp[i][1]=f(i) 1 출력횟수
"""
T=int(input())


for _ in range(T):
    # 0<=N<=40
    N=int(input())
    
    #예외처리)
    if N==0: 
        print("1 0")
        continue
    
    # idx : 0~N
    dp=[[0,0] for _ in range(N+1)]
    
    #초기값 : N=0,1일때
    dp[0][0]=1
    dp[1][1]=1
    
    #점화식
    for i in range(2,N+1):
        dp[i][0]=dp[i-1][0]+dp[i-2][0]
        dp[i][1]=dp[i-1][1]+dp[i-2][1]
    
    # fibo(N) 호출시 0:x번 1:y번 출력
    print(f"{dp[N][0]} {dp[N][1]}")