#2579: 계단 오르기

N=int(input())

s=[0] # 1~N 인덱스만 사용
for i in range(N):
    s.append(int(input()))

# 한번에 1계단 or 2계단 오를 수 있음.
# 연속된 세개를 모두 밟으면 안됨 (시작점은 포함x)
# 마지막 계단은 반드시 밟아야 함

# dp[i][1]= max(dp[i-2][1],dp[i-2][2]) + s[i]
# dp[i][2]= dp[i-1][1]+s[i]

if N==1:
    print(s[1])

else:
    dp=[[0]*3 for _ in range(N+1)]


    dp[1][1]=s[1]
    dp[1][2]=0
    dp[2][1]=s[2]
    dp[2][2]=s[1]+s[2]

    for i in range(3,N+1):
        dp[i][1]=max(dp[i-2][1],dp[i-2][2])+s[i]
        dp[i][2]=dp[i-1][1]+s[i]

    #둘중 최대값 출력
    print(max(dp[N][1],dp[N][2]))






