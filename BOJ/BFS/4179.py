# 4179 - 불! 골드3 : 2026.01.06
import sys
from collections import deque
input = sys.stdin.readline

# split() 은 strip까지 처리
# R*C 행렬
R,C = map(int,input().split())
board = []
dx=[1,-1,0,0]
dy=[0,0,1,-1]

fire=[[0] * C  for _ in range(R)] # 1. 불의 이동경로
pos= [[0]*C for _ in range(R)] # 2. 지훈 이동경로
 
fire_q=deque() # 불 bfs
pos_q=deque() # 지훈 bfs

for _ in range(R):
    row = list(input().strip())
    board.append(row)

for a in range(R):
    for b in range(C):

        # 방문체크후 큐에넣기
        if board[a][b]=='J':
            pos[a][b]=1
            pos_q.append((a,b))

        elif board[a][b]=='F':
            fire[a][b]=1
            fire_q.append((a,b))

# 1. 불의 이동경로 - 기존에 불이 있던곳도 계속 유지돼야함 
while fire_q:
    cur_x,cur_y= fire_q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx <0 or ny <0 or nx>=R  or ny>=C: continue
    
        # 이미 방문 / 벽인곳 예외처리
        # board[nx][ny]=='J' 인것도 처리가능
        if fire[nx][ny] != 0 or board[nx][ny] =='#' : continue

        # 방문처리후 큐에넣기 
        fire[nx][ny]=fire[cur_x][cur_y]+ 1
        fire_q.append((nx,ny))

# 2. 지훈 이동경로
while pos_q:
    cur_x,cur_y = pos_q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx <0 or ny <0 or nx>=R  or ny>=C: continue

        # board[][]=='F' 인것도 처리가능
        if pos[nx][ny] != 0 or board[nx][ny]=='#': continue

        pos[nx][ny]=pos[cur_x][cur_y]+1
        pos_q.append((nx,ny))

# 3. 탈출조건 체크
for a in range(R):
    for b in range(C):
        
        #3-1. 가장자리인지 체크 
        if a== 0 or a==R-1 or b==0 or b==C-1:

            #3-2. 먼저 도착시 탈출가능
            if fire[a][b] > pos[a][b] :
                print(pos[a][b])
                sys.exit() # 탈출가능 -> 시스템 종료
            
            # 불이더 빨리 도착하면 탈출 불가
            # 같은 값이여도 탈출 불가 

# 종료안됐다면 탈출불가 판정
print("IMPOSSIBLE")
            

# #디버깅용
# for row in fire:
#     print(row)

# for r in pos:
#     print(r)