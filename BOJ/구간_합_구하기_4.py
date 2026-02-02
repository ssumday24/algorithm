# 11659 dp
# 여러개의 하위문제를 먼저 푼뒤  그 결과를 쌓아올려 주어진 문제를 해결
# 하는 알고리즘
import sys
input= sys.stdin.readline

N,M = map(int,input().split())
arr= list(map(int,input().split()))
dp=[0]*(len(arr)+1)
for x in range(1,len(arr)+1):
    dp[x]=arr[x-1]+dp[x-1]
    #DP[1] = ARR[0] + DP[0] = 5
    #DP[2] = ARR[1] + DP[1] = 9
    #DP[5] = ARR[4] + DP [4] = 15
    
for _ in range(M): #TC M번 반복
    i,j = map(int,input().split())
    print(dp[j]-dp[i-1])
    