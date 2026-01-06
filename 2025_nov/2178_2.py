# 2178 미로탐색 - 2026.01.06
import sys
from collections import deque

N,M = map(int,input().split())
board=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q= deque()

# N * M 배열 
for _ in range(N):
        line = list(map(int,sys.stdin.readline().strip()))
        board.append(line)

vis = [[0] * M for _ in range(N)] 

# BFS 시작
vis[0][0]=1
q.append((0,0))

while q:
    cur_x,cur_y= q.popleft() #큐에서 꺼낸후 

    for i in range(4): #상하좌우 탐색
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 예외처리부분 
        if nx < 0 or ny < 0 or nx >= N  or ny>= M : continue
        
        # vis 로 거리 측정까지 포함 
        # 거리가 1 이상이면 이미 방문한곳. 
        if vis[nx][ny] >= 1 or board[nx][ny] == 0 : continue

        # 방문 체크후 큐에 추가
        vis[nx][ny]= vis[cur_x][cur_y] + 1

        q.append((nx,ny))


# 최종 출력
print(vis[N-1][M-1])
print(vis)
