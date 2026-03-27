#1260 : DFS와 BFS
import sys
from collections import deque
input= sys.stdin.readline
import copy

def dfs(graph,N,V):
    for i in range(1, N+1): #내림차순 정렬
        graph[i].sort(reverse=True)


    stack=[]
    visited =[False]*(N+1)  # 0번인덱스는 비워두기 
    
    stack.append(V) #시작점 스택에 넣기
    
    while stack: #스택이 비게되면 종료
        out= stack.pop()

        if visited[out]:
            continue
    
        visited[out]=True
        print(out,end=' ')
    
    
        ###### reversed 주의
        for neighbor in (graph[out]): 
            if not visited[neighbor]:
                stack.append(neighbor)
               
    return
#######################################################

def bfs(graph,N,V):
    for i in range(1, N+1): #오름차순 정렬
        graph[i].sort()

    Q=deque()
    visited=[False]*(N+1) # 0번 인덱스는 비워두기

    visited[V]=True
    Q.append(V)
    
    while Q: # 큐가 비면 종료
        front = Q.popleft()
        print(front,end=' ')
        
        for neighbor in graph[front]: # 주변 이웃 원소 확인
            if not visited[neighbor]: #방문하지 않았다면,  
                visited[neighbor]=True #방문했다는 표시를 남기고
                Q.append(neighbor) #큐에 넣음

   
    return




N,M,V = map(int,input().split())

#V는 탐색을 시작할 번호

graph={i:[] for i in range(1,N+1)}  #1번부터 n번 노드까지


#양방향 그래프에 추가
for _ in range(M):
    start,end =map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)



dfs(graph,N,V)
print()
bfs(graph,N,V)
print()
