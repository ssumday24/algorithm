# 11726 - dp
# 여러개의 하위문제를 먼저 푼뒤  그 결과를 쌓아올려 주어진 문제를 해결
# 하는 알고리즘

n= int(input())
dp=[0]*(n+1) # 1~n 인덱스 사용

dp[1]=1


if n==1:
    print(dp[1])
else:
    dp[2]=2
    
    
    for i in range(3,n+1):
        dp[i]=(dp[i-2] +dp[i-1])%10007
        
        # (a+b) % c = (a%c + b%c) % c
        # %10007 은 이전에 적용돼있어서 dp[i-2],dp[i-1]에 안해도됨
        
        
    print(dp[n])