# 1149 - DP 연습
# 1번과 2번집의 색은 달라야 한다.
# N번과 N-1번집의 색은 달라야한다.
# i(2<= i <= N-1) 집의 색은 i-1번, i+1번 집의 색과 달라야한다.

N=int(input())
dp=[[0,0,0] for i in range (N+1)]

red=[]
green=[]
blue=[]

#dp[i][0] : i번쨰 집까지 비용의 최솟값. 단 i번째는 빨간색
#dp[i][1] : i번째 집까지 비용의 최솟값. 단 i번째는 초록색
#dp[i][2] : 단 i번째는 파란색

for i in range(N):
    rgb = list(map(int,input().split()))
    red.append(rgb[0])
    green.append(rgb[1])
    blue.append(rgb[2])

dp[1][0]=red[0]
dp[1][1]=green[0]
dp[1][2]=blue[0]

for i in range(2,N+1):
    dp[i][0]= min(dp[i-1][1],dp[i-1][2]) + red[i-1]
    dp[i][1]= min(dp[i-1][0],dp[i-1][2]) + green[i-1]
    dp[i][2]= min(dp[i-1][0],dp[i-1][1]) + blue[i-1]
    
print(min(dp[N][0],dp[N][1],dp[N][2]))
