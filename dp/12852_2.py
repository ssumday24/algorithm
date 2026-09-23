# BOJ 12852
# 1로 만들기(2) - G5
# 26.03.12
# 26.03.16
import sys

input = sys.stdin.readline

"""
경로추적 복습

dp[i]: i->1 로 가는데 필요한 연산횟수의 최솟값

tr[i]: i에서 i-1, i//2 , i//3 중 하나로 이동할때, 
이 3가지 값중 하나 기록
"""
N = int(input())
dp = [0] * (N + 1)  # idx : 1~N
tr = [0] * (N + 1)

# dp[2]~dp[N]
for i in range(2, N + 1):
    # 3가지 비교후 최솟값 갱신
    dp[i] = 1 + dp[i - 1]

    """
    경로도 같이 갱신, 조건추가
    i->i-1 or i//2 or i//3 로 가는게 최단경로일때만 기록
    """
    tr[i] = i - 1

    # 실제로 최단연산일때만 tr[i]에 추가
    if i % 2 == 0 and 1 + dp[i // 2] < dp[i]:
        dp[i] = min(dp[i], 1 + dp[i // 2])
        tr[i] = i // 2

    # 실제로 최단연산일때만 tr[i]에 추가
    if i % 3 == 0 and 1 + dp[i // 3] < dp[i]:
        dp[i] = min(dp[i], 1 + dp[i // 3])
        tr[i] = i // 3

# 출력
print(dp[N])

# 예외처리 N==1일때
if N == 1:
    print(1)
    sys.exit()


# 경로출력:N->tr[N]->tr[tr[N]]->...1
i = N
while i > 0:  # i가 0이 되기 전까지 계속 돔
    print(i, end=" ")  # 현재 위치 출력
    i = tr[i]
