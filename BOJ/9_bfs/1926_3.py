# 1926 그림 - 2026.01.06 
import sys
from collections import deque

n, m =  map(int,input().split(' '))
board = [] # 그림판 
vis= [] 
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q= deque() #bfs에 사용할 큐 
pic_cnt = 0 # 그림의 수
max_area = 0 # 가장 넓은 그림의 넓이

for _ in range(n): 
    # int로 문자 -> 정수 변환 후 다시 리스트 변환 
    row = list(map(int,input().split(' ')))
    board.append(row)
    vis.append([0 for _ in range(m)])

# BFS 시작
for a in range(n): # a : 0~ n-1
    for b in range(m): # b : 0 ~ m -1 

        if vis[a][b] ==1 : continue # 이미 방문했으면 시작점 불가
        if board[a][b] == 0 : continue

        # 여기가 "BFS 의 1 싸이클"
        area = 0 
        cur_x=a
        cur_y=b

        vis[cur_x][cur_y]=1 # 시작점 방문체크후 큐에넣기
        q.append((cur_x,cur_y))
        area += 1  # 시작점 넓이 생각
        pic_cnt +=1 # 그림 개수 추가
       
        while q: # 큐가 비어있지 않은 동안

            cur_x,cur_y = q.popleft() # 큐에서 꺼낸후 

            for i in  range(4): #상하좌우 탐색
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                # 인덱스 범위체크
                if nx < 0 or nx >= n or ny <0 or ny >=m : continue
                
                # 이미 방문한곳, 0인곳 체크 
                if vis[nx][ny]==1 or board[nx][ny]==0 : continue 

                # 방문체크 후 큐에 넣기 
                vis[nx][ny]=1 
                q.append((nx,ny))

                # 그림의 넓이
                area +=1 
    
        if area > max_area :
            max_area = area # 최대 그림 넓이 갱신 



# 최종출력
print(pic_cnt)
print(max_area)