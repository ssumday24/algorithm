# BOJ 1926 : 그림 - 실버1 
# 
"""  (가독성)
많은 개발자와 채점자가 선호하는 스타일은 '예외 조건은 최대한 빠르게 걸러낸다 (Early Exit)'는 원칙을 따릅니다.
=> 이렇게 continue 로 거르면 조건문 안깊어짐  
"""
import sys
from collections import deque

# n*m matrix
n,m=map(int,input().split()) 
board=[]
# [0 * m ] 과의 차이 ?
visit=[[0] * m for _ in range(n)]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

start_x=0
start_y=0

# 1. 방문 표식 남기고 큐에 넣기
visit[start_x][start_y]=1
q.append((start_x,start_y))

while q:
    cur_x,cur_y = q.popleft()

    # 상하좌우 탐색
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 범위 벗어날때
        if nx <0 or ny < 0 or nx >=n or ny>=m : continue 

        # 이미 방문한곳일때
        if visit[nx][ny] ==1  : continue

        # 문제조건 : board==1 인곳만 탐색해야함
        if board[nx][ny] == 0 : continue
        
        # 방문표시 후 큐에 넣기
        visit[nx][ny]=1
        q.append((nx,ny))