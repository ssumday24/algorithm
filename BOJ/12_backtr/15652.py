# BOJ 15652
# N과M (4) - S3
# 26.02.26
"""
- 1~N중 M개를 고른 수열
- 같은수 여러번 가능
- 비 내림차순 : a1 <= a2 <= a3 ...
- BOJ 15650과 비교 
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M= map(int,input().split())
arr=[]
vis=[False] * (N+1) # idx : 1~N 

def func(depth,start):
    
    # M개 골랐으면 출력후 pop
    if depth == M:
        for x in arr:
            print(f"{x} ",end='')
        print() 
        return

    # start~N 사용확인
    # 15651과 다른점은, {2,1}은 출력하면 안됨 
    # 가장 위의 func의 한 싸이클마다 start++가 되어야함 
    for i in range(start,N+1):
            
        arr.append(i)

        func(depth+1,i)
        
        arr.pop()
       

###
func(0,1)