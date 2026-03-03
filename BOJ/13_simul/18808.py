# BOJ 18808
# 스티커붙이기 - G3
# 26.03.03
"""
- for문 변수 여러개같이?
"""
import sys
input=sys.stdin.readline

# N*M , K개 스티커 : R*C
N,M,K=map(int,input().split())

# 노트북: N*M
board=[[0]*M for _ in range(N)]

####################################
def find(board,stick,start_x,start_y):
    R = len(stick)
    C = len(stick[0])
    
    # 스티커(R*C)가 모눈종이 벗어날때 (각도마다 스티커모양 고정)
    if start_x +R >N or start_y +C>M: 
        return 0
    
    # 1. 모든 구역이 깨끗한지 검사
    for i in range(R):
        for j in range(C):
            # 음수인덱스 검사 
            if start_x <0 or start_y<0 : 
                return 0
            
            # 이미 스티커가 있을때
            # 즉 노트북,스티커 모두 1일때
            if (board[start_x+i][start_y+j]==1 and 
                stick[i][j]==1) : 
                return 0
            
    # 2. 이제 스티커 배치가능 -> 원본 board 수정가능
    for i in range(R):
        for j in range(C):
            # 노트북에 붙이기
            if stick[i][j]==1:
                board[start_x+i][start_y+j]=1
    
    # 3. 성공 
    return 1
            
            
####################################
# 배열 90도회전 R*C -> C*R
# 인자로 R,C받지말고 안에서 len()으로 처리
def rotate(stick):
    R = len(stick)
    C = len(stick[0])
    
    new_arr= [[0]*R for _ in range(C)]

    for x in range(R):
        for y in range(C):
            # (x,y) -> (y,-x+R-1) 
            if stick[x][y]==1:
                new_arr[y][R-1-x]=1
    
    return new_arr
####################################
def try_attach(board,stick):
    
    # 각 각도에 대해(4방향)
    # (원본,rot)->(90,rot)->(180,rot)->(270,rot)
    for i in range(4):
        
        # (0,0)->(N-1,M-1) 전부 대보기
        for start_x in range(N):
            for start_y in range(M):
                # find() 성공 -> break -> 다음스티커 진행
                if find(board,stick,start_x,start_y) == 1 : 
                    return
        
        # 실패 -> 다음각도 진행 
        stick = rotate(stick)


####################################
# main파트

# 각 스티커마다 진행
for _ in range(K):
    R,C = map(int,input().split())
    stick= [list(map(int,input().split())) for _ in range(R)]
    
    try_attach(board,stick)
        
      
        
        
#구하는것 : 스티커 수
cnt=0
for row in board:
    for elem in row:
        if elem==1:
            cnt+=1
print(cnt)