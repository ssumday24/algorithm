# BOJ 1932
# 정수 삼각형-S1
# 26.03.13
import sys

input = sys.stdin.readline
"""
[WIL]
- 경로추적 
- 1로만들기(2) - BOJ #12852 다시 풀고 비교 
- ########### 백트래킹 풀이 <-> DP풀이 각각 비교 ###########

시간복잡도:

dp[i]: i번째row 까지 골랐을떄 
"""
n = int(input())
arr = []  # 크기n인 삼각형 담을 배열

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
