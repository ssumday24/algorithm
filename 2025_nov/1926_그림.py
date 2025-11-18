import sys
from collections import deque
# n*m 배열

n,m = map(int,input().split(' '))
arr=[] 
vis=[] # 방문표시 
q= deque() # 빈 큐 만들기

# 상하좌우 탐색좌표
dx=[1,-1,0,0]
dy=[0,0,-1,1]

pic_cnt =0 # 그림의 개수
max_area = 0 # 가장 넓은 그림의 넓이 

for _ in range(n):
    row = list(map(int,input().split(' ')))
    arr.append(row)
    vis.append([0 for _ in range(m)]) # 방문배열 만들기

cur_x = 0 #현재 좌표 cur
cur_y = 0
vis[0][0]=1 ; # 방문표시

while q : 
    # 각 방향에 대해 검사 
    for _ in range(4):
        nx= cur_x + dx
        ny = cur_y + dy

        # 1. 범위 걸리는지 검사
        if (nx >=n or ny >= m or nx <0 or ny <0 ):
            continue

        # 2. 방문 여부 체크 
        if vis[nx][ny]==1 : 
            continue
        
        # 3. 큐에 넣기
        q.append((nx,ny))

        # 4. 방문 등록
        vis[nx][ny]=1
    
    # 5. 디큐로 하나씩 제거  
    q.popleft()
        
print(pic_cnt)
print(max_area)