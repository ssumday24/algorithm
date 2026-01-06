# 2178. 미로탐색 - 실버1
# N*M 미로  , 시작위치와 도착위치포함 
from collections import deque
import sys 

N,M= map(int,input().split(' '))

board=[]
vis=[]  # bfs 방문체크 
result=[] # 시작점부터의 거리를 담을 배열 result
q=deque()
dist = 0  # 거리변수 dist 

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# 입력부분 
for _ in range(N):
    row=list(sys.stdin.readline().strip())
    board.append(row)

    vis.append([0 for _ in range(M)])

# 시작점 방문 체크후 
cur_x=0
cur_y=0
vis[cur_x][cur_y]=1
q.append(cur_x,cur_y)

# bfs 시작 
while q:
    cur_x,cur_y= q.popleft()

    # 상하좌우 체크 
    for i in range(4):
        nx= cur_x + dx[i]
        ny = cur_y + dy[i]

        # nx : 0 ~ N-1  , ny : 0 ~ M-1
        if nx<=0 or ny<=0 or nx>=N or ny>= M: continue

        if vis[nx][ny]==1 : continue

        # 안걸렸다면 방문체크 후 큐에 넣기
        vis[nx][ny]=1
        q.append((nx,ny))

        # 문제 추가조건 : 시작점으로부터의 거리 ****** ?

# 시작점(0,0) -> (N,M)지나야 하는 최소 칸의 수
print(result[N-1][M-1])