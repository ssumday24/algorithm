# 07.29 (화) 
# #1129. 그림 - BFS 
# 그림의 개수와, 가장 넓은 것의 넓이 출력

from collections import deque
import sys
N,M = map(int,input().split(" "))
dx=[1,0,-1,0]
dy=[0,1,-1,0]

arr=[]
que=deque([]) # 덱 라이브러리 사용
visited=[[0]*M for _ in range(N)] #방문체크용 배열

for i in range(N):
    row =map(int,sys.stdin.readline().split())
    arr.append(list(row))


for i in range(N):
    for j in range(M):
        if arr[i][j] ==1 and visited[i][j] ==0: # 값이 1이고, 방문안했을때
            que.append(arr[i[j]]) # 큐에집어넣기
            visited[i][j]=1 #방문 체크 

            