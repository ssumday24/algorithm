# boj 7576 : 토마토 - G5
"""
1 -> 익은 토마토
0 -> 익지 X
-1 -> 들어있지 X 
M*N 행렬
"""

import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
board=[] 
vis=[] #방문체크
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque() # 큐 자료구조

day=0 # 모두 익기 위한 최소날짜

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    board.append(row)

    vis.append([0 for _ in range(M)])



# 모두 익지 못하는 상황 -> -1 출력 (-1에 가로막혔을때)
# 처음부터 모두 익어있으면 -> 0 출력 (0이 존재하지않을때)

print(day) # 모두 익기 위한 최소날짜  