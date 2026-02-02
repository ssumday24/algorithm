# 10819: 차이를 최대로
from itertools import permutations

N=int(input())

A=list(map(int,input().split()))

max_value=0

for perm in permutations(A):
    total=0
    
    for i in range(N-1): # N-1번 반복
        diff=abs(perm[i]-perm[i+1])
        total += diff
    if total > max_value:
        max_value=total

print(max_value)