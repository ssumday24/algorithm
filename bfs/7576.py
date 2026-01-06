# 7576 - 토마토 G5 : 2026.01.06
"""
며칠이 지나면 토마토가 모두 익는지? 최소일수 계산 
1 = 익음
0 = 익지 X
-1 = 존재 X
"""
import sys
from collections import deque
input  = sys.stdin.readline # () 쓰면 함수실행이니 안됨

# N * M 행렬 
M,N = map(int,input().split(' '))
day = 0 
board=[]
vis=[[0] * M for _ in range(N)] # 방문체크
q=deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(N):
    row = list(map(int,input().split()))
    board.append(row)

# "동시에 시작점이 여러개인" BFS 
for a in range(N):
    for b in range(M):

        if board[a][b] ==1 and vis[a][b]==0 :
            # 방문체크 후 큐에넣기  
            vis[a][b]=1
            q.append((a,b))


############### BFS 시작
while q:
    cur_x,cur_y = q.popleft()

    for i in range(4):
        nx = cur_x+ dx[i]
        ny = cur_y + dy[i]

        # 인덱스 예외처리
        if nx <0 or ny < 0 or nx >=N or ny>=M : continue

        # 방문하지 않았고, 안익은(0) 토마토 자리만 가능 
        if vis[nx][ny] != 0 or board[nx][ny] != 0 : continue

        # 방문체크-> 거리 기반으로 큐에넣기
        vis[nx][ny]= vis[cur_x][cur_y]+ 1
        q.append((nx,ny))

        # 사과도 익게 처리
        board[nx][ny]=1

###############
flag=0

for a in range(N):
    for b in range(M):

        # 안익은 0 이 존재 -> -1 출력
        if board[a][b] == 0 : 
            flag = -1
            break

        # vis 행렬에서 최대값 찾기
        day = max(day, vis[a][b])
        
if flag == -1 :
    print(-1)


else: #입력이 이미 모두 익은 케이스도 포함 (day=0)
    print(day- 1) 

# ### 출력 확인용 ### 
# for a in range(N):
#     print(vis[a])        