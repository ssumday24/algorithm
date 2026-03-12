# BOJ 11659 
# 구간합 구하기4 - S3
# 26.03.09
import sys

input = sys.stdin.readline
"""
DP연습문제(6)
[WIL]

"""
N,M=map(int,input().split())
arr=[0]+list(map(int,input().split()))

"""
dp[i]=i번째 수까지의 합 (i,j>=1)
"""
#초기값
dp=[0]*(N+1) # idx:1~N 사용

#점화식
for x in range(1,N+1):
    dp[x]=dp[x-1]+arr[x]

for _ in range(M):
    i,j=map(int,input().split())
    result=dp[j]-dp[i-1]
    print(result)