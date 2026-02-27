# BOJ 15683
# 감시 - G3
# 26.02.27
"""
-SW A형기출(2문제 3h)
- CT 서로 통과가능
- CT 방향정해서, 사각지대 최소 -> 감시영역'#' 최대
- 0 :빈곳
- 1~5:CCTV (서로통과 가능) 
- 6:벽(통과불가)

p1:CCTV가 진행하면서 다른CT를 만나면 어떻게처리?
(벽(#)으로 바꿔버리면 func() 호출못하므로)
=> 백트래킹 복구 
=> 감시함수 구조화(상하좌우)

"""
import sys
input=sys.stdin.readline

N,M = map(int,input().split())
arr=[]
cnt = 0 # 사각지대의 개수 

# 입력부분
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)


def func1(i,j):
    #1번 CT:한쪽방향만 감시 + 벽(6)생각    

    # 상: idx (i-1) ~ 0 이동 , j 고정 
    for a in range(i-1,0,-1):
        if arr[a][j]==6: # 벽을만나면 종료
            break
        arr[a][j]= '#'

    # 하: idx (i+1) ~ (N-1) 이동 , j 고정 
    for a in range(i+1,N,1):
        if arr[a][j]==6:
            break
        arr[a][j]= '#'

    # 좌: idx (j-1) ~ (0) 이동 , i 고정 
    for a in range(j-1,0,-1):
        if arr[i][a]==6:
            break
        arr[i][a]= '#'
        
    # 우: idx (j+1) ~ (N-1) 이동 , i 고정 
    for a in range(j+1,N,1):
        if arr[i][a]==6:
            break
        arr[i][a]= '#'



# 각CCTV
for i in range(M):
    for j in range(N):
        if arr[i][j]== 1:
            func1(i,j)
        
        else if arr[i][j]==2:      
            func2(i,j)
    
        else if arr[i][j]==3:      
            func3(i,j)
            
        else if arr[i][j]==2:      
            func4(i,j)    
    
        else if arr[i][j]==5:      
            func5(i,j)

    
#사각지대의 최소 크기 : 전체 - 0의 개수
print(N*M -cnt)
