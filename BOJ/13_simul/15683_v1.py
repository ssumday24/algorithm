# BOJ 15683
# 감시 - G3
# 26.03.01
"""
- 배열 복사 ([row[:] for row in current_arr])
- 방향이동에 대한 추상화 (BFS의 dx,dy)
-원본배열 쓰지않는건 상태복원이 어려우니까 임시배열쓰고 버리기
- 팁 : 시계방향으로 0,1,2,3 맞추면 회전로직짤때 편함
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    
- 비트마스킹 (완전탐색)or 
- 누적카운트(0,-1,-2)방식으로 풀어보기 
"""
import sys
input=sys.stdin.readline

N,M = map(int,input().split())
office= [list(map(int,input().split())) for _ in range(N)]
cnt = 0 # 사각지대(0) 개수
arr_ct=[] # cctv 정보저장 배열
k=0 # cctv 개수

for i in range(N):
    for j in range(M):
        # (CCTV 종류,i좌표,j좌표) 튜플저장
        if (office[i][j] in [1,2,3,4,5]): 
            arr_ct.append((office[i][j],i,j))
            k+=1 

###################
# 0,1,2,3: 상->우->하->좌
def move(office,x,y,dir):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    #만약 dir=[0,1]이 들어온다면
    # vector = 상하좌우중 1방향
    for vector in dir:
        nx = x
        ny = y
        
        # 영역의 끝 또는 벽을 만날때까지 이동
        while True:
            nx += dx[vector] 
            ny += dy[vector]
            
            # 인덱스 범위체크, 영역 벗어나면 종료
            if nx<0 or ny<0 or nx>=N or ny>=M : break
            
            # 벽만나면 종료
            if office[nx][ny]==6 : break
            
            # 다른 CCTV 만나면 통과, 즉 0일때만 #으로 변경
            if office[nx][ny]==0:
                office[nx][ny]='#'
        
    # 바뀐 배열 반환
    return office

################################################
cctv_mode=[[], #사용x
            [[0],[1],[2],[3]], #1번
            [[0,2],[1,3]], #2번
            [[0,1],[1,2],[2,3],[3,0]], #3번
            [[0,1,3],[0,1,2],[1,2,3],[2,3,0]], #4번
            [[0,1,2,3]]] #5번

min = N*M  # min 초기값: 사무실 넓이
################################################
# 백트래킹
def func(depth,cur_office):
    global min # 외부변수 min 접근
    
    # k개 ct의 방향을 모두 정하면 최종계산 후 리턴
    if depth == k:
        cnt=0
        
        for row in cur_office:
            for elem in row:
                if elem == 0 :
                    cnt+=1
        
        # 사각지대 최소값 갱신 
        if cnt < min:
            min = cnt
            
        return
        
    # depth 번째 (cctv,x,y) 꺼내기
    # arr_ct  idx: 0~(k-1)
    num,x,y = arr_ct[depth]
    
    # num 번 cctv에 대한 모든 가짓수 순회
    for dir in cctv_mode[num]:
        
        ### 위치 중요: 반복문 안에 위치해야함
        #원본은 그대로 두고, 배열복사
        copied_office= [row[:] for row in cur_office]
        
        changed_office=move(copied_office,x,y,dir)
        
        func(depth+1,changed_office)
 
    # 배열 복사해서 썼으니 상태복원 필요x

#######################################
#사각지대의 최소 크기 
func(0,office)

print(min)
