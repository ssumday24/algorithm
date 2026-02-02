#2217 로프
import sys
input = sys.stdin.readline
import math

N= int(input())
ropes=[]
for _ in range(N):
    rope=int(input())
    ropes.append(rope)

result=0

weakest = min(ropes)

#들어올릴수 있는 물체의 최대 중량을 i
for i in range(1,1001):
    check=False
    
    #가장 약한 로프가 들수있는 무게보다 무겁다면   
    if weakest<=math.ceil(i // N) :
        check=True    
   
    
    if check==True:
        break        
    
    result +=1


print(result)
