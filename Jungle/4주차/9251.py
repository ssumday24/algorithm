#9251 : LCS
#풀이 날짜 : 2025.06.11

"""
DP[i][j]: 위에서 i번째 글자까지 봤을때, 
아래에서 j번째 글자까지 봤을때,
공통 부분 수열의 "최대 길이"
"""




import sys
sys.stdin.readline

x=input()
y=input()

dp=[[0]*(len(y)+1) for _ in range(len(x)+1)]

for i in range(1,len(x)+1): # 1~x 까지 보기
    for j in range(1,len(y)+1) : #1~y 까지 보기
        
        # 1.두 문자열의 마지막 글자가 일치하는경우
        if x[i-1] == y[j-1] : 
            dp[i][j]=dp[i-1][j-1]+1 
        
        # 2.두 문자열의 마지막 글자가 다른경우
        #2-1. 첫번째 문자열의 마지막 글자가 lcs에 포함 x
        #dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
            
        #2-2. 두번째 문자열의 마지막 글자가 lcs에 포함 x
        #dp[i][j]=dp[i][j-1]
        
        #2-3. 두 문자열의 마지막 글자가 "모두" lcs에 포함 x
        #dp[i][j]=dp[i-1][j-1]
        #이 경우 항상 2-1 과 2-2 보다 작음
        
        
print(dp[len(x)][len(y)])