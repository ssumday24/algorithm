#1388 바닥장식 -bfs 버전
import sys
from collections import deque

global count
count =0

def bfs(graph,x,y,tree,N,M):
    
    queue=deque()

    #방문표시하고 넣기
    queue.append((x,y))
    visited[x][y]=True
 
    if tree=='-' : #가로판자면 오른쪽으로만 탐색
        dx=[0]
        dy=[1]
        
    else: #세로판자면 아래로만 탐색
        dx=[1]
        dy=[0]
    
    while queue:
        x,y=queue.popleft()

        nx = x+ dx[0]
        ny = y + dy[0]
        
        if nx<0 or ny <0 or nx>=N or ny>=M : continue
        
        if not visited[nx][ny] and graph[nx][ny]==tree:
            
            #방문표시하고 넣기
            visited[nx][ny]=True
            queue.append((nx,ny))
        
    
    
    return 

#########################################
N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)] 
visited=[[False]*M for i in range(N)]


for i in range(N):
    for j in range(M):
        if not visited[i][j] : 
            bfs(graph,i,j,graph[i][j],N,M) 
            count+=1

print(count)