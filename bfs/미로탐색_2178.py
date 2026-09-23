# BOJ 2178 미로탐색 - 실버1 , BFS
# 26.02.04
from collections import deque
import sys 
input = sys.stdin.readline

# N*M 행렬
N, M = map(int,input().split())
board=[]
visit=[[0]*M for _ in range(N)]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
min_move = 0 # 지나야 하는 최소 칸 수 (정답)

for _ in range(N):
    # 문자열 리스트화
    row = list(map(int,list(input().strip())))
    board.append(row)

# 방문체크후 큐에넣기
cur_x,cur_y = 0,0 # 시작점(0,0)고정
visit[cur_x][cur_y]= 1 
q.append((cur_x,cur_y))

while q:
    cur_x,cur_y = q.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        
        # 인덱스 범위 체크 vis[nx][ny]
        if nx < 0 or ny <0 or nx >= N or ny >=M : continue 

        # 1 이상 -> 이미 방문한곳
        if visit[nx][ny]>=1 : continue

        # 0 인곳 제외
        if board[nx][ny]==0 : continue
        
        # 거리 계산 -> 무조건 상하좌우 인접이니 +1
        visit[nx][ny] = visit[cur_x][cur_y] + 1
        q.append((nx,ny))


print(visit[N-1][M-1])
