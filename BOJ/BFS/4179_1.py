# BOJ 4179 불! : Gold 3
# 26.02.04
"""
1. 시작점이 여러 "종류" 인 경우
<-> BOJ-4179 토마토의 시작점이 "여러개" 와 다름

2. A 가 B의 상태에 영향을 받는다면 반드시 B의 상태를 먼저 확정짓거나
동시에 진행해야함 -> (스트림/실시간 처리)
"""
import sys
from collections import deque
input= sys.stdin.readline

R,C = map(int,input().split()) # R*C 행렬
board = [] 
q_j= deque()
q_f = deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
dist_j = [[-1]*C for _ in range(R)] # 지훈 위치 
dist_f = [[-1]*C for _ in range(R)] # 불 위치

for _ in range(R):
    row= list(input().strip()) # string -> list
    board.append(row)

for i in range(R):
    for j in range(C):

        if board[i][j]=='J': # 지훈
            q_j.append((i,j))
            dist_j[i][j]= 0 # 시작점 : 0
        
        if board[i][j]=='F': # 불
            q_f.append((i,j)) 
            dist_f[i][j]=0 # 시작점 : 0

# 1. 지훈 bfs
while q_j:
    cur_x,cur_y= q_j.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 인덱스 범위 아웃
        if nx <0 or ny <0 or nx >=R  or ny >=C : continue

        # 이미 방문한곳
        if dist_j[nx][ny] >= 0 : continue

        # 벽인곳
        if board[nx][ny] == '#' : continue

        # BFS-> 거리 1씩 증가 
        dist_j[nx][ny]= dist_j[cur_x][cur_y]+ 1 

        q_j.append((nx,ny))

# 2. 불 bfs
while q_f : 
    cur_x,cur_y = q_f.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 인덱스 범위 아웃
        if nx <0 or ny <0 or nx >=R  or ny >=C : continue

        # 이미 방문한곳
        if dist_f[nx][ny] >= 0 : continue

        # 벽인곳은 통과 불가
        if board[nx][ny] == '#' : continue

        # BFS-> 거리 1씩 증가 
        dist_f[nx][ny]= dist_f[cur_x][cur_y]+ 1 

        q_f.append((nx,ny))

# # 디버깅용
# for r in dist_j:
#     print(r)
# print("====================")
# for r in dist_f:
#     print(r)

list_min=[] #탈출시간을 담아둘 리스트


# 3. 탈출조건 판별
for a in range(R):
    for b in range(C):

      
        # 가장자리일때만 탈출가능
        if a==0 or a== R-1 or b== 0 or b== C-1 :

            # 벽인곳은 애초에 판별x
            if dist_j[a][b]==-1 : continue 

            # case1. 불이 안났을때
            if dist_f[a][b]== -1 : 
                list_min.append(dist_j[a][b]+1)

            # case2.지훈의 시간 < 불의 도착 시간 (등호x)
            if dist_j[a][b] < dist_f[a][b]:
               list_min.append(dist_j[a][b]+1)

if list_min:
    print(min(list_min))
else:
    # list_min이 비었으면 탈출불가
    print("IMPOSSIBLE")
