#2667 : bfs 복습
import sys
from collections import deque

def bfs(graph,N,x,y):
    queue=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    home_cnt = 0 
    
    # 큐에 넣고 방문표시 ( 1-> 0)    
    queue.append((x,y))
    graph[x][y]=0 #방문표시
    home_cnt +=1
    
    while queue: #큐가 빌때 종료
        x,y = queue.popleft()
        
        for k in range(4): #상하좌우 탐색
            
            
            nx= x+dx[k]
            ny= y+dy[k]

            # 1. 범위 벗어날때, 2. 집이 없을때
            if nx<0 or ny<0 or nx>N-1 or ny>N-1 : continue
            if graph[nx][ny]==0 : continue
            
            # 집이 있을때
            if graph[nx][ny]==1:
                
                
                # 큐에 넣고 방문 표시
                queue.append((nx,ny))
                graph[nx][ny]=0 # 방문 표시
                home_cnt+=1
    
    
    return home_cnt   #각 단지내 집의 수 
################
N =int(input())
graph = [list(map(int,input())) for i in range(N)]
groups=[] #각 단지내 집의 수

for i in range(N):
    for j in range(N):
        if graph[i][j]==1: #1이고 방문한적 없다면
            groups.append(bfs(graph,N,i,j)) # bfs 시작
            
# 총 단지 수 출력            
print(len(groups))

# 각 단지내 집의 수를 오름차순 정렬하여 출력
groups.sort()
for group in groups:
    print(group)