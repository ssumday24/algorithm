# BOJ 1182
# 부분수열의 합 - S2
# 26.02.26
"""
N개의 합 = S인 경우의 수 
"""
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))

result=[]
vis=[False]* (N+1) # idx : 1~N 사용 
cnt = 0 # 경우의 수 

def func(depth):
    global cnt
    
    # 부분수열의 원소의 개수 : 1 ~ N개 가능, 각case별 확인
    for i in range(1,N+1):
         
    
    





#########################
func(0)
print(cnt)