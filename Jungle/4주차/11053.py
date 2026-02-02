# 11053 : 가장 긴 증가하는 부분 수열
# dp[i]: i번째 원소를 "마지막 값으로 가지는" 가장 긴 증가하는 부분수열의길이

import sys 
input=  sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp=[1]*(N) # 0~N-1번 인덱스 사용

for i in range(N):
    for j in range(0,i): # 0~ i-1번 인덱스
        if A[i]>A[j]:
            dp[i]=max(dp[i],dp[j]+1)
        

print(max(dp))

