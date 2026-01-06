#3190 : 뱀
import sys
input = sys.stdin.readline
from collections import deque #덱 임포트

N = int(input()) #보드의 크기
K = int(input()) #사과의 개수

rows=[]
cols=[]

for _ in range(K): # 사과의 위치
    row,col = map(int,input().split())
    rows.append(row)
    cols.append(col)
    
L = int(input()) # 뱀의 방향변환 횟수

T_list=[]
C_list=[]

for _ in range(L):
    T,C = input().split()
    T_list.append(int(T))
    C_list.append(C)
#############################################
arr=[]


for i in range(N+2): # (n+2)*(n+2) 인 배열
    temp=[]
    
    if i == 0 or i==N+1:
        arr.append([-1]*(N+2))
        continue
    
    for j in range(N+2):
        if j==0 or j == N+1:
            temp.append(-1)
        else:
            temp.append(0)
    
    arr.append(temp)

for i in range(K):
    arr[rows[i]][cols[i]]=1  # 사과가 있으면 1 표시
################################################
time =0  # 지난 시간체크
ptr = 0 # T,C 위치를 체크할 포인터
direction = 0  # 방향 체크 - 오른쪽:0, 아래:1, 왼:2,위:3
x,y=1,1 #이동전 시작점 arr[1][1]
arr[x][y]=2 

snake = deque()
snake.append((x,y))

while(True): # 예시) T=[3,15,17] / C=[D,L,D]
   
    if ptr <L: #L = 방향변환 횟수
        if time == T_list[ptr]: # 방향 이동
            if C_list[ptr]=='D':
                direction =(direction + 1)%4   # 오른쪽방향 이동
            elif C_list[ptr]=='L':
                direction =(direction-1)%4   # 왼쪽방향 이동
                
            ptr +=1 #다음인덱스 이동
    
    # 방향 정해졌으니 이동
    # 시작점은 arr[1][1] -> arr[x][y] 
    
    if direction==0: #오른쪽
        y+=1
        
    elif direction==1: #아래
        x+=1
    
    elif direction==2: #왼쪽
        y-=1
        
    elif direction==3: #위쪽
        x-=1

# 이동 끝난 후 
    if arr[x][y] == -1 or arr[x][y]== 2: 
            # 벽에부딪히거나 몸에 부딪히면 종료
            print(time+1)
            break

    #(1,2)->(2,3)->(3,4)... 
    #사과 먹을경우 몸길이 1 늘어남
    if arr[x][y]==1 : 
        arr[x][y]=2 # 그자리는 뱀이 차지
        snake.append((x,y)) #좌표저장

    #사과가 없으면 꼬리칸 제거
    elif arr[x][y]==0:
        arr[x][y]=2
        snake.append((x,y)) # 이동한곳 저장
        tx,ty = snake.popleft() #이동전 자리 삭제
        arr[tx][ty]=0 # 이동전 자리는 다시 0
        
    #다 끝났으면 시간++
    time +=1 
    

