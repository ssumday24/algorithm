# boj 2178 : 미로탐색
# 거리배열 

import sys
from collections import deque
#input=sys.stdin.readline

N,M = map(int,input().split())

board=[]
vis=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque() # 큐 자료구조 
cnt = 0 # 지나야 하는 최소 칸 수 (1,1)->(N,M)

dist=[]


for _ in range(N):
    line=list(map(int,sys.stdin.readline().strip()))
    board.append(line)

    vis.append([0 for _ in range(M)])

# 시작점 방문표시 + 큐에넣기
vis[0][0]=1
q.append((0,0))

while q:
    cur_x,cur_y= q.popleft()
    cnt+=1 

    for i in range(4): #상하좌우 탐색
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 인덱스 범위 체크
        if nx <0 or nx>=N or ny<0 or ny>=M : continue 

        # 방문여부 체크
        if vis[nx][ny] !=0 : continue

        # 1인곳만 이동가능  
        if board[nx][ny] == 0 : continue

        # 조건을 만족하면 방문표시 + 큐에넣기
        vis[nx][ny]=vis[cur_x][cur_y]+1
        q.append((nx,ny))

    

# 지나야하는 최소 칸의 수 : 시작점도 포함  
print(vis[N-1][M-1])


# for i in range(N):
#     print(vis[i])
