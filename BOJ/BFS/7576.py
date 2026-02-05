# BOJ 7576 토마토 : Gold 5 
# 26.02.04
import sys
from collections import deque
input = sys.stdin.readline

"""
며칠이 지나면 모두 익는지 최소 일 수 
1 : 익음 
0 : 익지 X
-1 : 없는 곳
"""

# N*M 행렬
M, N = map(int,input().split())
board=[]
visit=[[0]*M for _ in range(N)]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
day = 0 # 날짜계산

for _ in range(N):
    row = list(map(int,input().split()))
    board.append(row)

for a in range(N):
    for b in range(M):
        # 여러 시작점을 전부 큐에 넣기
        if board[a][b]== 1 : 
            visit[a][b]=1
            q.append((a,b))

        # 토마토가 없는곳 : 여기서 visit 예외처리
        if board[a][b] == -1 : 
            visit[a][b]= -1 

# 시작점 다 넣어두고, BFS 시작
while q:
    cur_x,cur_y = q.popleft()

    #상하좌우 탐색
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 인덱스 범위체크
        if nx <0 or ny <0 or nx >= N or ny >=M : continue

        # 이미 방문한곳
        if visit[nx][ny] >=1 : continue

        # 토마토가 없는곳 
        if board[nx][ny] == -1 : continue
        
        # 거리계산(방문체크 포함) 후  큐에넣기
        visit[nx][ny]= visit[cur_x][cur_y] +1
        q.append((nx,ny))

for a in range(N):
    for b in range(M):
        # 예외) 익지 못한 토마토가 존재할때 -1출력 , 종료
        if visit[a][b] == 0 : 
            print(-1)
            sys.exit()

        # vis 안에서 최대값 찾기
        day = max(day,visit[a][b])

# 최종 출력 : 시작점 포함이니 -1. 
print(day- 1)


# 디버깅
# for row in visit:
#     print(row)