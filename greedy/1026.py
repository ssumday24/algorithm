# BOJ 1026
# 보물-S4
# 26.03.17
import sys

input = sys.stdin.readline
"""
그리디 연습문제-4
[WIL]

B는 재배치하면 안되고 A만 재배열해야하지만
어차피 모든원소 다 포함되니 
결과적으론 똑같아서 상관없음

그리디 풀이: O(NlogN) 
완전탐색: O(N!) =불가능
"""
N = int(input())
arr1 = list(map(int, input().split()))  # A
arr2 = list(map(int, input().split()))  # B

# B 내림차순 정렬
arr2.sort(reverse=True)

# A 오름차순 정렬
arr1.sort()

result = 0
for i in range(N):
    result += arr1[i] * arr2[i]

print(result)
