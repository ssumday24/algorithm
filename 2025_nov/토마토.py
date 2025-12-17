# boj 7576 : 토마토 - G5
"""
1 -> 익은 토마토
0 -> 익지 X
-1 -> 들어있지 X 
M*N 행렬

거리 -> -1로 초기화 하기 

할일 : 예외처리 
"""

import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
board=[] 
dist=[] #방문체크 + 거리계산 
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque() # 큐 자료구조

day=0 # 모두 익기 위한 최소날짜

# 0. 입력부분
for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    board.append(row)

    dist.append([-1 for _ in range(M)])

# 1. 익은 토마토 찾기 (시작점)
for i in range(N):
    for j in range(M):
        if board[i][j]== 1 : 
            q.append((i,j)) #바로 큐에넣기 
            dist[i][j]=0 # dist 값을 0으로 바꿔주기
# 토마토 큐에 넣고 dist 값을 0으로 바꿔주기. ->이부분 생각

while q :
    cur_x,cur_y = q.popleft()

    for i in range(4): # 상하좌우 탐색 
        nx = cur_x+dx[i]
        ny = cur_y + dy[i]

        # 인덱스 범위 체크 
        if nx <0 or ny < 0 or nx >= N or ny >= M : continue

        # 거리가 0 초과면 이미 bfs 진행한것
        if dist[nx][ny] != -1 : continue 

        #방문 체크후 push (거리기반)
        dist[nx][ny] = dist[cur_x][cur_y] + 1 
        q.append((nx,ny))


# 모두 익지 못하는 상황 -> -1 출력 (-1에 가로막혔을때)
# 처음부터 모두 익어있으면 -> 0 출력 (0이 존재하지않을때)
 
for i in range(N):
    for j in range(M):
        if dist[i][j] > day:
            day = dist[i][j]

print(day) # 모두 익기 위한 최소날짜 