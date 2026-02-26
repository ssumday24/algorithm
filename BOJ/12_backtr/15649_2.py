# BOJ 15649 N과M(1) - S3
# 26.02.12
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
1~N 의 자연수중 중복없이 M개를 고른 수열 
depth == 지금까지 채워넣은 숫자 개수 + 트리 깊이
"""
N,M= map(int,input().split())
arr=[] # 결과 담을 배열 
visited=[False] * (N+1) # 사용여부 체크 , 1번 idx부터사용

def func(depth):
    if depth==M: # len(arr)==M
        # M개숫자 출력
        for i in range(M):
            print(f"{arr[i]} ",end="")
        print() 
        return 

    # index : 1~N 이 사용되었는지 검사,
    # i 값과 사용되는 수는 같음
    for i in range(1,N+1): 
        
        if visited[i] == False :
            
            # 방문표시후 배열에 추가
            visited[i] = True
            arr.append(i)  

            func(depth+1)
            
            visited[i] = False
            arr.pop()


func(0)
"""
ex) 1,2 -> 1,3 으로 넘어가는 과정 
1,2 에서 return 을 받고
arr.pop()을 해도, 
반복문 안에서 i=3 에서 다시 3이 append됨
"""