# BOJ 15683
# 감시 - G3
# 26.02.27  
# 버전1
"""
-SW A형기출(2문제 3h)
- CT 서로 통과가능
- CT 방향정해서, 사각지대 최소 -> 감시영역'#' 최대
- 0 :빈곳
- 1~5:CCTV (서로통과 가능) 
- 6:벽(통과불가)

- CT가  다른CT를 만나면 어떻게처리?
(벽으로 바꿔버리면 func() 호출못하므로)

- 배열 복사 ([row[:] for row in current_arr])
- 백트래킹 복구
- 함수 재사용(상하좌우)

- 인덱스 범위 조심
  for a in range(i-1,-1,-1):
  (끝나는 숫자 포함하지 않으니 신경쓰기)
  
- *** 방향이동에 대한 추상화 (BFS의 dx,dy)
"""
import sys
input=sys.stdin.readline

arr=[] # 사무실의 배치상태 담긴 ARR

N,M = map(int,input().split())
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

cnt = 0 # 사각지대(0) 개수

temp_ct=[] # cctv (1~5) 숫자만 고려한 경우 
final_ct=[] # 위에서 cctv 방향까지 고려한  경우의수 

k=0 # CCTV 개수

# cctv 개수 k 구하기
for i in range(N):
    for j in range(M):
        if (arr[i][j]==1): 
            temp_ct.append(1)
            k+=1
        
        elif (arr[i][j]==2): 
            temp_ct.append(2) 
            k+=1
        elif (arr[i][j]==3): 
             temp_ct.append(3)
             k+=1
        elif (arr[i][j]==4): 
             temp_ct.append(4)
             k+=1
        elif (arr[i][j]==5):  
            temp_ct.append(5)
            k+=1

# 이동함수 정의
def up(arr,i,j):
     # 상: idx (i-1) ~ 0 이동 , j 고정 
    for a in range(i-1,-1,-1):
        if arr[a][j]==6: # 벽을만나면 종료
            break
        
        # 다른 cctv 만나면 그대로 두기 
        elif (arr[a][j]==1 or 
            arr[a][j]==2 or
            arr[a][j]==3 or
            arr[a][j]==4 or
            arr[a][j]==5):
            continue
        
        arr[a][j]= '#'

def down(arr,i,j):
     # 하: idx (i+1) ~ (N-1) 이동 , j 고정 
    for a in range(i+1,N,1):
        if arr[a][j]==6:
            break
        
         # 다른 cctv 만나면 그대로 두기 
        elif (arr[a][j]==1 or 
            arr[a][j]==2 or
            arr[a][j]==3 or
            arr[a][j]==4 or
            arr[a][j]==5):
            continue
        
        arr[a][j]= '#'

def left(arr,i,j):
    # 좌: idx (j-1) ~ (0) 이동 , i 고정 
    for a in range(j-1,-1,-1):
        if arr[i][a]==6:
            break
        
         # 다른 cctv 만나면 그대로 두기 
        elif (arr[i][a]==1 or 
            arr[i][a]==2 or
            arr[i][a]==3 or
            arr[i][a]==4 or
            arr[i][a]==5):
            continue
        
        arr[i][a]= '#'

def right(arr,i,j):
    # 우: idx (j+1) ~ (M-1) 이동 , i 고정 
    for a in range(j+1,M,1):
        if arr[i][a]==6:
            break
        
         # 다른 cctv 만나면 그대로 두기 
        elif (arr[i][a]==1 or 
            arr[i][a]==2 or
            arr[i][a]==3 or
            arr[i][a]==4 or
            arr[i][a]==5):
            continue
        
        arr[i][a]= '#'
#############################

min = N*M  # 초기값 : 사무실넓이

# temp_ct로 백트래킹 
def backtr(depth,temp_ct):
    
    # k개 cctv 전부 계산했을때 종료
    # 사각지대(0)이 최소가 되어야함 
    if depth == k :
        for row in temp_ct:
            for val in row : 
                if val==0:
                    cnt+=1

        #사각지대 최소값 갱신
        if cnt < min:
            min = cnt
        
        return
        
    # 인덱스 : 0 ~ (k-1)
    for i in  range(0,k):
        cctv(temp_ct[i])



#사각지대의 최소 크기 : 0이 최소가 되어야함 
# depth : 0 , arr : [1,2,3,5]등으로 시작
backtr(0,temp_ct)
