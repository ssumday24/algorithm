# 10971 : 외판원 순환
from itertools import permutations

N=int(input())
arr=[]
Matrix=[]

# N*N 행렬 만들기
for i in range(N): # S
    element= list(map(int,input().split()))
    Matrix.append(element)
    
    arr.append(i)  # N=4 일때 arr=[0,1,2,3]
    
PER_arr=permutations(arr)    #튜플 arr=[(0,1,2,3),(0,1,3,2),...]

min_cost=float("inf")

# route= (3,1,2,0) 
# N! Permutation 중 한가지 방법인 route
for route in PER_arr: 
    total=0
    blocked= False # 디폴트는 길히 막히지 않은 상태.
    
    for i in range(0,N-1):  # M[3][1] + M[1][2] + M[2][0]
         if Matrix[route[i]][route[i+1]]==0:
              #예외상황 : 길이 막혔을때 
            blocked=True
            break
         else: 
            total += Matrix[route[i]][route[i+1]] 
            
     #마지막 출발지로 돌아올때는 따로 계산
    if blocked==False and Matrix[route[N-1]][route[0]] != 0: 
        total += Matrix[route[N-1]][route[0]] #M[0][3]
        min_cost = min(total,min_cost)


print(min_cost)

