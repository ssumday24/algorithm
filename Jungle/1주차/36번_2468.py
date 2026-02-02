#2468 : 안전영역의 최대개수?

N = int(input())
Matrix = [list(map(int,input().split())) for _ in range (N)]

check = []
for i in range(N):
    row=[]
    for j in range(N):
        row.append(0)
    check.append(row)  #check= 모두 0인 배열 초기화
    

max_safe = 0 # 안전영역 개수


for rain in range(1,101):  # 비의 양 : 1m~100m
    cnt=0 #물에 잠긴 원소 개수 -> cnt=N*N 이면 종료
    for i in range(N):
        for j in range(N):
            if rain>check[i][j]:
                check[i][j]=1 #물에 잠긴 곳은 1로 표시, 나머진 0
                cnt+=1
            
            if cnt == N*N :
                break
            
    # 1. 꼭짓점 (RD,LD,RV,LU)  # i=행 , j = 열
    for i in range(N):
        for j in range(N):
            
            if (i==0 and j==0) or (i==0 and j==N-1) or (i==N-1 and j==0)or(i==N-1 and j==N-1):
                
    
    # 2. 꼭짓점 제외한 모서리: N-2개씩
    
    # 3. 나머지

