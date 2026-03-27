# 12852 : 1로만들기 2
# 여러개의 하위문제를 먼저 푼뒤  그 결과를 쌓아올려 주어진 문제를 해결
# 하는 알고리즘
import sys
input=sys.stdin.readline

N =int(input())
d=[0]*(N+1)
d[1]=0

route = [0]*(N+1)


for i in range(2,N+1):
   
    d[i]=d[i-1]+1
    route[i]=i-1 #기본 경로는 i-1
    
    if i % 2 == 0 and d[i]>d[i//2]+1:
        d[i]=d[i//2]+1
        route[i] = i//2
        
    if i % 3 ==0 and d[i]>d[i//3]+1:
        d[i]=d[i//3]+1
        route[i]= i//3

    # 비교가 끝나면, d[i] = min(d[i-1]+1,d[i//2]+1,d[i//3]+1)
    # +1인 이유는 d[i] 정의 자체가 "횟수" 이기 때문 
 
#출력1
print(d[N])

  # N에서 시작
ptr = N
path=[]
while ptr :
    path.append(ptr)
    ptr = route[ptr]

print(' '.join(map(str,path)))