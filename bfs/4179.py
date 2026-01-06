# 4179 - 불! 골드3 : 2026.01.06
import sys
from collections import deque
input = sys.stdin.readline

# split() 은 strip까지 처리
# R*C 행렬
R,C = map(int,input().split())
board = []
vis=[[0] * C  for _ in range(R)] # 문제 조건처리용 행렬
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()

for _ in range(R):
    row = list(input().strip())
    board.append(row)

for a in range(R):
    for b in range(C):

        # 지훈 시작점 -> 방문체크후 큐에넣기
        if board[a][b]=='J':
            vis[a][b]='J'
            q.append((a,b))

        elif board[a][b]=='F':
            vis[a][b]='F'
            q.append((a,b))