# BOJ 2579
# 계단오르기 - S3
# 26.03.07
import sys

input = sys.stdin.readline
"""
1.테이블 정의 -> 2.점화식 찾기 -> 3.초기값 설정 
"""
# main
N = int(input())
arr = [0]  # idx: 1~N  사용
for _ in range(N):
    arr.append(int(input()))

dp = []
for i in range(N + 1):
    dp.append([0, 0, 0])  # col idx: 0,1,2 중 1,2만 사용

# 예외처리
if N == 1:
    print(arr[1])
    sys.exit()

elif N == 2:
    print(arr[1] + arr[2])
    sys.exit()

"""
dp[i][j]= i번째 계단까지 올랐을때, 점수의 최댓값,  단 j개의 계단을 연속해서 밟음. 단,i번째 계단은 반드시 밟아야함
j=0 :X
j=1 계단:(i-2)->(i)   
j=2 계단:(i-1)->(i)
"""
# 초기값 설정
dp[1][1] = arr[1]
dp[1][2] = 0
dp[2][1] = arr[2]
dp[2][2] = arr[1] + arr[2]

# i: 3~N
for i in range(3, N + 1):

    # arr[i-2]를 무조건 밟았다는 뜻이니
    dp[i][1] = arr[i] + max(dp[i - 2][1], dp[i - 2][2])

    # (i-1)을 무조건 밟음, i-2는 밟으면안됨
    # dp[i-1][2]불가능
    dp[i][2] = arr[i] + dp[i - 1][1]

result = max(dp[N][1], dp[N][2])
print(result)
