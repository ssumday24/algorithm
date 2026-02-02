#2579 : 계단오르기 복습
import sys
input = sys.stdin.readline

N=int(input())
stairs=[0]

#DP[i][j]= i번째 계딴까지 올랐을때 점수의 총합의 최댓값
#단, 바로 직전에는 (1점프) or (2점프)
dp=[[0]*3 for _ in range(N+1)] 
 
for _ in range(N):
    stairs.append(int(input()))
    # 한번에 1계단 or 2계단
    # 연속된 세개의 계단 X
    # 마지막 계단 반드시

if N==1:
    print(stairs[1])
elif N==2:
    print(stairs[1]+stairs[2])    

else:
    dp[1][1]=stairs[1]
    dp[1][2]=0
    dp[2][1]=stairs[2]
    dp[2][2]=stairs[1]+stairs[2]
    
    
    for i in range(3,N+1):
        dp[i][1]= dp[i-1][2]+stairs[i]
        dp[i][2]=max(dp[i-2][1],dp[i-2][2])+stairs[i]


    print(max(dp[N][1],dp[N][2]))