# BOJ 1629 곱셈: S1
# 26.02.10
"""
(A**B) % C = ?
{(A**(B/2) % C) (A**(B/2) % C)} % C ... 반복 
"""
import sys
input = sys.stdin.readline


A,B,C = map(int,input().split())

def mod(a,b,c):
    
    # 지수가 1, 즉 b==1 이면 base case.
    if b==1 : 
        return a % c 

    # 지수b가 홀수일때,b-1은 짝수이므로 
    # (f(a,b-1,c)*(a mod c)) mod C
    if b %2 ==1 :
        return (mod(a,b-1,c)*(a % c)) % c
    
    # 2분의 b 승으로 분할 
    return mod(a,b/2,c)**2 % c  

print(mod(A,B,C))