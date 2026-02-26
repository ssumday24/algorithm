# BOJ 15651 
# N과M (3) - S3
# 26.02.26
"""
- 1~N중 M개를 고른 수열, 같은수여러번 가능
- 백트래킹에서 append와 pop은 반드시 같은 층, 같은 괄호 안에존재
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M= map(int,input().split())
arr=[]
vis=[False] * (N+1) # idx : 1~N 

def func(depth):
    
    if depth == M:
        for i in arr:
            print(f"{i} ",end='')
        print()
        # 콜스택 pop
        return  
    
    # 기존엔 1~N 의 vis 검사
    # 중복순열이면 필요없지않나?
    for i in range(1,N+1):
        
        # 배열에 추가
        arr.append(i)
        
        # 다음 깊이
        func(depth+1)

        arr.pop() 
        # pop은 depth==m일때 하면안됨 

#####
func(0)