# BOJ 1074 Z - G5
# 26.02.11
"""
전체를 1~4 사분면으로 나눈 후 
1. r과 c를 통해 몇 사분면에 존재하는지 파악
2. 각 사분면에 따라 N을 줄이며 누적합 구하기
3. 베이스는 N=1 일떄 0,1,2,3

전체를 2등분했을때, 각 사분면의 넓이는 (2^n * 2^n) / 2 이므로 
area = 2^(2n-2) = 4^(n-1)
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 필수

N, r, c = map(int,input().split())
def func(n,r,c):

    # base, 숫자는 Z자로 커짐
    if n==1 : 
        if r==0 and c==0 : return 0
        elif r==0 and c==1 : return 1
        elif r==1 and c==0 : return 2
        else : return 3

    area = 4**(n-1) # 각 사분면의 넓이
    ##### half = 2**(n-1) 

    # 2 사분면 ex) func(2,1,1)
    if r< 2**(n-1) and c < 2 ** (n-1):
        return func(n-1, r,c)
    
    # 1사분면 : c 를 줄이기
    elif r < 2**(n-1) and c >= 2**(n-1):
        return area + func(n-1,r, c-2**(n-1)) 
    
    # 3사분면 : r 줄이기
    elif r >= 2**(n-1) and c < 2**(n-1):
        return 2*area + func(n-1,r-2**(n-1),c)
    
    # 4사분면 : c,r 줄이기  
    else : 
        return 3*area + func(n-1, r-2**(n-1),c-2**(n-1))

print(func(N,r,c))