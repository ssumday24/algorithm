# BOJ 18808
# 스티커붙이기 - G3
# 26.03.03
"""
- TODO: 붙일수있는곳 : 가장 위쪽 + 가장 왼쪽 순
- 0-90-180-270도 회전시에도 못찾으면 버림 
스티커마다 각도별 find -> 추가or버리기-> 다음스티커 
- for문 변수 여러개같이?
"""
import sys
input=sys.stdin.readline

# N*M , K개 스티커 : R*C
N,M,K=map(int,input().split())

# 노트북: N*M
board=[[0]*M for _ in range(N)]

# 성공:1 실패: 0 , board 원본수정
# TODO: 붙일수있는곳 : 가장 위쪽 + 가장 왼쪽 순
def find(board,stick,R,C,cur_x,cur_y):
    # 스티커 배치 좌표 보존위해 사용
    check_x=cur_x
    check_y=cur_y
    
    # 1. 모든 구역이 깨끗한지 검사
    for i in range(R):
        for j in range(C):
            
            # 인덱스 범위 검사
            # 모눈종이 벗어날때 (각도마다 스티커모양 고정)
            if check_x <0 or check_y<0 or check_x>=N or check_y>=M: 
                return 0
            
            # 이미 스티커가 있을때
            if board[check_x][check_y]==1: 
                return 0
            
            # 빈곳(0)일때 오른쪽이동
            check_y +=1
                
        # 아랫줄 이동 
        check_x +=1 
        
    # 2. 이제 스티커 배치가능     
    for i in range(R):
        for j in range(C):
            # 노트북에 붙이기
            if stick[i][j]==1:
                board[cur_x][cur_y]=1
            cur_y +=1
        cur_x +=1
    
    # 3. 성공 
    return 1
            
            
####################################
# 배열회전    
def rotate(stick,dir):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    
    #원본
    if dir == 0 : return stick

    #90도 회전
    elif dir ==1 :
        return stick
    
    #180도
    elif dir==2:
        return stick
    
    #270도
    elif dir==3:
        return stick
####################################
for _ in range(K):
    R,C = map(int,input().split())
    stick= [list(map(int,input().split())) for _ in range(R)]
    
    for dir in range(4):
        # 0-90-180-270회전
        # TODO : 
        stick = rotate(stick,dir)
        
        # 스티커 붙이기 성공 -> 다음스티커 진행
        if find(board,stick) == 1 : break
    
        

#구하는것 : 스티커 수
cnt=0
for row in board:
    for elem in row:
        if elem==1:
            cnt+=1
print(cnt)