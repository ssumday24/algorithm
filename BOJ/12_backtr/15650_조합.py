# BOJ 15650 N과M(2) - S3
# 26.02.26
"""
- 1~N 의 자연수중 중복없이 M개를 고른 수열 
- 오름차순, nCm 조합 
- {1,2} 를 출력했으면 {2,1}을 출력하면 안됨
- 오름차순일때만 출력하기
    - 오름차순 어떻게 예외처리?
    - {1,4} ->{2,1} 넘어갈때 1을 True 남겨두기?
- 트리를 위에서 아래로 자라는 스택으로 생각
- i를 보고있을때, 1~(i)는 신경쓰지 말아야 오름차순
- 즉, 자신을 제외한 i+1 부터만 보면됨
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M= map(int,input().split())
arr=[]
vis=[False] * (N+1) # idx : 1~N 사용 

def func(depth,start):
    if depth == M : 
        for i in range(M):
            print(f"{arr[i]} ",end='')
        print()
        return # 스택 pop
    
    # i ( start ~ N ) 사용여부 체크
    for i in range(start,N+1):
        
        if vis[i]==False :
            vis[i]=True
            arr.append(i)            

            # 다음 재귀부터는 i+1 부터만 보기
            func(depth+1,i+1)
            
            vis[i]= False
            arr.pop()

########
func(0,1) 