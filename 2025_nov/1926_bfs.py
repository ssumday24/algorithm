# 25.12.10 
# boj 1926 : 그림 - 실버1 
# 55분 
""" 선호되는 코딩 스타일 (가독성)
많은 개발자와 채점자가 선호하는 스타일은 '예외 조건은 최대한 빠르게 걸러낸다 (Early Exit)'는 원칙을 따릅니다.
=> 이렇게 continue 로 걸러야 조건문 안깊어짐  
"""
from collections import deque
import sys 

# n*m  
n,m = map(int,sys.stdin.readline().split(' '))
board=[] # n*m 그림판 배열
vis = [] # n*m 방문체크 배열 
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q= deque()

cnt= 0  #그림의 개수 
mx_area = 0 # 가장 넓은 그림의 넓이 
area=0 #각 그림들의 넓이 
mx_area =0# 그림넓이 최대값

for _ in range(n):
    row =list(map(int,sys.stdin.readline().split(' ')))
    board.append(row)
    
    vis.append([0 for _ in range(m)]) # 방문체크 배열 만들기 

#bfs 시작 -> 모든 칸을 돌며 bfs의 시작점이 될수있는지 체크 
for a in range(n):
    for b in range(m):

        # 방문하지 않았고, 파란칸일때만 시작점 가능 
        if vis[a][b]==0 and board[a][b]==1 : 

            cnt +=1  #그림 개수 추가 
            area= 0 # 그림 넓이 저장 
            cur_x= a
            cur_y= b

            #시작점 (a,b)
            vis[cur_x][cur_y]=1
            q.append((cur_x,cur_y))
            area +=1 

            while q :  #큐가 비어있지 않은 동안

                cur_x,cur_y = q.popleft() 

                for i in range(4): # 상하좌우 탐색
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]

                    # 범위 체크
                    if (nx<0 or nx>=n or ny<0 or ny>=m): continue
                    
                    # 방문여부 체크 
                    if (vis[nx][ny]==1) : continue

                    #그림판의 숫자가 1일때만,
                    # 큐에 넣기 + 방문체크
                    if board[nx][ny]==1 :  
                        q.append((nx,ny))
                        vis[nx][ny]=1

                        area +=1  

            mx_area= max(area,mx_area)
   
# 그림의 개수 , 가장 넓은 그림의 넓이
print(cnt)
print(mx_area)