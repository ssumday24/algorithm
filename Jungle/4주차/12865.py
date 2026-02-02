# 12865 : 평범한 배낭
import sys
input =sys.stdin.readline

N,K = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(tuple(map(int,input().split())))

#dp[i][j]: i번째 물건까지 고려했을 때, 무게 j로 만들수있는 최대 가치
#예제는 dp[4][7]    
dp=[[0]*(K+1) for _ in range(N+1)]

##arr[][0] = W(무게) , arr[][1] = V(가치)

for i in range(1,N+1):
    W,V=arr[i-1] # i번째 수를 보는거라면, 배열의 i-1 index를 보는것
    
    for j in range(1,K+1): 

            if j-W>=0 : # 인덱스가 범위 벗어나지 않을때만
                dp[i][j]=max(dp[i - 1][j - W] + V, dp[i - 1][j])
            else: #벗어나면(물건넣기불가능) 그냥 이전상태 유지
                dp[i][j] = dp[i-1][j]

#print(dp)
print(dp[N][K])

"""
고민점 :  물건을 넣을 수 없는 경우 왜 dp[i][j]=dp[i-1][j]지?
답변 : 이전까지 가치가 10이었는데
"물건 하나 못 넣는다고 무조건 0으로 리셋?" → 말이 안 됨!

"""