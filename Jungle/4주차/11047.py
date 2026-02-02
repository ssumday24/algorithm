#11047 동전0
import sys
input=sys.stdin.readline

### 배수 관계가 아닐때는 어떻게풀어야 할까
# 1, 9 ,10 원으로 18원 만들기 
#필요한 동전 개수의 최대값?
N,K=map(int,input().split())
coins=[]
for _ in range(N):
    c= int(input())
    
    if c > K : # K보다 동전이 크면 추가X
        continue
    else:
        coins.append(c)
coins.sort()

cnt=0

while K>0:
    while (K // coins[-1] ==0 and coins) : #몫이 0이라면
        coins.pop()
    
    A =  K // coins[-1]
    cnt += A        
    K = K- A*coins[-1]
    coins.pop() # coins[-1] , 즉 맨끝원소 제거


print(cnt)