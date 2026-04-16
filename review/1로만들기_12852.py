# BOJ 12852
# 1로 만들기(2) - G5
# 26.03.12
# 26.03.16
# 26.04.16
import sys

input = sys.stdin.readline

"""
- 경로추적
- dp[i]: i->1 로 가는데 필요한 연산횟수의 최솟값
- tr[i]: i에서 i-1, i//2 , i//3 중 하나로 이동할때, 
이 3가지 값중 하나 기록

- 탑다운으로 풀면 i=10 일때 dp[5]가 필요한, 의존성 문제 발생
- 따라서 bottom-up 으로 풀기

"""
from collections import deque

N = int(input())

# 테이블,점화식
dp = [0] * (N + 1)  # 1~N 사용

# 초기값
dp[1] = 0

trace = [0] * (N + 1)  # 경로추적용 배열

# DP[2]~DP[N]
for i in range(2, N + 1):
    # i-1 에서 왔을때
    dp[i] = dp[i - 1] + 1
    trace[i] = i - 1

    # i/2 에서 왔을때가 더 빠른경우
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        # i//2로 교체,
        dp[i] = dp[i // 2] + 1

        # 전에 어디서 왔는지 기억
        trace[i] = i // 2

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        trace[i] = i // 3

# 출력
print(dp[N])

# 경로
# N-tr[N]-tr[tr[n]]-tr[3]

cur = N
while cur >= 1:
    print(cur, end=" ")
    cur = trace[cur]
