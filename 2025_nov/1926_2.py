# 1926그림 . 복습
"""
7576: 토마토와 비교해보기.
이 문제에서는 그림의 개수를 세어야 하기 때문에 
모든 시작점을 한번에 큐에 넣는 방법을 적용할수없음.
"""


import sys
from collections import deque
input=sys.stdin.readline

n,m= map(int,input().split(' '))  # n*m 배열

board=[] #그림판
vis=[] #방문체크
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque() # 큐로 사용햘 q

pic_cnt=0 # 그림의 개수 
area=0 # 가장 넓은 그림의 넓이 
max_area=0

for _ in range(n):
    line = list(map(int,sys.stdin.readline().split(' ')))
    board.append(line)

    vis.append([0 for _ in range(m)])

# 0. 시작점이 될수있는지 체크
for a in range(n):
    for b in range(m):
        # 방문하지 않았고, 1이면 시작점 가능함
        if vis[a][b] == 1 : continue
        if board[a][b] ==0 : continue

        pic_cnt+=1 # 그림의 수 +1 
        area= 1 # 넓이는 시작점인 1로 시작 

        # 1. "하나의 시작점에 대해" 시작점 방문체크후 큐에넣기
        cur_x=a
        cur_y=b
        vis[cur_x][cur_y]=1
        q.append((cur_x,cur_y))

        while q:
            cur_x,cur_y = q.popleft() # x,y좌표 저장 -> 이문제에서필요한가? 

            for i in range(4) : # 상하좌우 탐색
                nx = cur_x + dx[i] #(nx,ny) 는 현재 탐색좌표임
                ny = cur_y + dy[i]

                if nx<0 or nx>=n or ny <0 or ny >=m : continue #인덱스범위 체크 

                if vis[nx][ny] == 1 : continue # 방문여부 체크

                if board[nx][ny] == 0 : continue #  0인곳 체크 

                # 문제없으면 방문체크 후 큐에넣기
                vis[nx][ny]=1
                q.append((nx,ny))
                
                # 넓이 +1
                area +=1

        max_area = max(area,max_area) # 그림 넓이 갱신 


print(pic_cnt)
print(max_area)