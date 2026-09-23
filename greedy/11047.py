# BOJ 11047
# 동전0 - S4
# 26.03.16
import sys

input = sys.stdin.readline
"""
그리디 연습문제-1
DP풀이도 가능하지만 시간초과

- 다음엔 for c in coin[::-1] 슬라이싱 활용
"""
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

cnt = 0  # 동전개수
start = N - 1  # 시작인덱스

while K > 0:
    # 현재 동전이 너무클때 줄이기
    # 조건1. start=0 , 1원일때 인덱스가 감소하면 안됨
    if K // coin[start] == 0 and start >= 1:
        start -= 1

    # 나눌수 있을때 최대로 구성
    cnt += K // coin[start]

    # 남은돈 : 나머지
    K = K % coin[start]


# 방법2) 슬라이싱
"""
for c in coin[::-1]: 
    cnt += K // c
    K %= c
"""

# 출력
print(cnt)
