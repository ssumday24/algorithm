# BOJ 1463
# 1로만들기 - S3
# 26.03.07
"""
DP연습문제(1)
연산 횟수의 최솟값 (N<10^6)

-파이썬에서 /를 쓰면 소수점(float) 타입으로 변환
=> '//' 쓰기

DP: 테이블 정의 -> 점화식 찾기 -> 초기값 설정
"""

import sys

input = sys.stdin.readline


# 방법1) 백트래킹 -> 시간초과
# 트리 깊이 = 연산횟수
def backtr(depth, num):
    global result  # 함수안에서 result값 갱신

    # 가지치기 -> 최소값을 초과하면 더볼필요x
    if depth >= result:
        return

    if num == 1:
        if depth < result:
            result = depth
        return

    # 3가지 연산중 1 선택후 다음깊이
    if num % 2 == 0:
        backtr(depth + 1, num // 2)
    if num % 3 == 0:
        backtr(depth + 1, num // 3)

    backtr(depth + 1, num - 1)


# 방법2) DP[i]: i=>1로 가는데 필요한 최적연산횟수
def func(n):
    # 기본값: dp[n-1]+1
    # dp[2]=1, dp[3]=1
    dp[n] = 1 + dp[n - 1]

    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n // 2] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n // 3] + 1)


# main부분
N = int(input())
result = 99999  # 연산횟수-> 백트래킹전용

dp = [0] * (N + 1)  # idx: 1~N 사용

# dp[2]~dp[N] 구하기
for i in range(2, N + 1):
    func(i)

print(dp[N])
# print(dp)
