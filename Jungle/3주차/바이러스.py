import sys
from collections import deque
input= sys.stdin.readline


def bfs(graph,N):
    for i in range(1, N+1): #오름차순 정렬
        graph[i].sort()

    Q=deque()
    visited=[False]*(N+1) # 0번 인덱스는 비워두기

    Q.append(1)
    visited[1]=True
    
    while Q: # 큐가 비면 종료
        front = Q.popleft()
        print(front,end=' ')
        
        for neighbor in graph[front]: # 주변 이웃 원소 확인
            
            if not visited[neighbor]: #방문하지 않았다면,  
                visited[neighbor]=True #방문했다는 표시를 남기고
                Q.append(neighbor) #큐에 넣음

   
    return





N=int(input())
E=int(input())
graph={i:[] for i in range(1,N+1)}

for _ in range(E):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
print(graph)
bfs(graph,N)