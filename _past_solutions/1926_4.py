# BOJ 1926 : 그림 - 실버1 
# 26.02.04
"""  (가독성)
많은 개발자와 채점자가 선호하는 스타일은 '예외 조건은 최대한 빠르게 걸러낸다 (Early Exit)'는 원칙을 따릅니다.
=> 이렇게 continue 로 거르면 조건문 안깊어짐  
"""
import sys
from collections import deque
# 포인터로 input -> sys.stdin.readline 함수 가리킴 
input = sys.stdin.readline

# n*m matrix
n,m=map(int,input().split()) 
board=[]
# [0 * m ] 과 다름주의
visit=[[0] * m for _ in range(n)]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
pic_cnt =0  #그림의 개수 
max_area = 0 # 최대 넓이

for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

# "모든 점에 대해" BFS
for a in range(n):
    for b in range(m):

        # 이미 방문한곳 or 0인곳 스킵
        if visit[a][b]== 1 or board[a][b]== 0 : continue
        
        # 1. 방문 표식 남기고 큐에 넣기
        visit[a][b]=1
        q.append((a,b))

        area = 1 # 그림 넓이 : 시작점 포함 1로시작
        pic_cnt +=1 # 그림 개수 ++ 

        while q:
            cur_x,cur_y = q.popleft()

            #print(f"큐에서 나온 x,y 좌표 : {cur_x,cur_y}")

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

                # 넓이 증가 
                area +=1 
    
        # 그림 최대 넓이 갱신
        if area > max_area :
            max_area = area

# 그림의 개수
print(pic_cnt)

# 그림 최대 넓이
print(max_area)