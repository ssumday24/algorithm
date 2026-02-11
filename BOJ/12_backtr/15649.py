# BOJ 15649 N과M(1) - S3
# 26.02.12
"""
1~N 의 자연수중 중복없이 M개를 고른 수열 
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

N,M = map(int,input().split())
arr=[] # 결과를 담을 배열 
used=[False]*(N+1) # 1~N이 사용되었는지 체크, 0번인덱스 안씀 
 
def func():
    # base condition
    if len(arr) == M :
        for i in range(M):
            print(f"{arr[i]} ",end='')
        print()
        return

    # "i" 를 사용했는지 체크
    for i in range(1,N+1):
        
        # 사용안했으면 사용
        if not used[i] :
            arr.append(i)
            used[i]= True 
            
            func()
            
            # 다시 사용x 상태로 되돌림 
            arr.pop()
            used[i]=False

func()