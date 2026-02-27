# BOJ 15654
# N-queen - G4
# 26.02.27
"""
- N*N에 N개의 퀸 배치 경우의 수
- #1182 와 다르게 가지치기/유망성 판단가능 
- 2차원 행렬을 상태공간 트리처럼 보기

- 조건검사 부분은 n과m 문제의 if not visited[i]와 같은역할로
생각하기
- 가지치기가 빈번하면 시간복잡도 파악힘듬
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N= int(input())
cnt = 0
arr = [[0]*N for _ in range(N)] # N*N matrix 

vis_1=[False]*N  #각 col에 퀸의 배치여부
diag_1=[False]*(2*N-1)  # 오른대각(/) : 각 2N-1 개 존재 
diag_2=[False]*(2*N-1)  # 왼대각(\)

# row : 0 ~ (n-1) 탐색
def func(row):
    global cnt # 함수 내부에서 외부변수 접근 
    
    # N개 row 에 전부 배치완료
    # ex) N=4 일때 arr[3][] 까지배치후 row=4면 리턴
    if row == N :
        cnt +=1 
        return 
    
    # 최소한 각 row에 한개는 배치해야하므로
    # 각 row마다 col좌표 탐색
    for col in range(N): # idx : 0~(N-1)
        
        # 퀸을 놓을수 있는지 확인 
        if (not vis_1[col] and 
            not diag_1[row+col] and
            not diag_2[row-col+(N-1)]) :
            
            # 1.같은열 전부 배치로 생각
            vis_1[col] = True  
                
            # 2-1. 대각선(/) 배치
            # row+col = k 인곳은 전부 배치간주
            diag_1[row+col]=True
                    
            # 2-2. 대각선(\) 배치
            # row-col +(N-1) = k 인곳은 전부 배치간주
            diag_2[row-col+(N-1)]=True
           
            # 다음 row 배치 
            func(row+1)
            
            # 상태 복원
            arr[row][col]=0
            vis_1[col]=False
            diag_1[row+col]=False
            diag_2[row-col+(N-1)]=False
        
##################### 
#출력
func(0)
print(cnt)