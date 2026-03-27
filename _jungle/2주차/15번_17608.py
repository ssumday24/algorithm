#17608 막대기
import sys
input=sys.stdin.readline

N=int(input())  #오른쪽에서 몇개가 보이는지?
stack=[]
inputs=[]

#겹쳐있을때 생각 
# ex) 9 9 9 9 9 6
# ex) 8 9 7 6 4 6 ->3


for _ in range(N):
    num= int(input())
    inputs.append(num)
    
cnt=0
max= inputs[-1]

for i in reversed(inputs):
    #스택이 비었거나 or 맨오른쪽보다 크다면
    if not stack or i > max:
        max = i
        stack.append(i)
        
        cnt+=1
        
print(cnt)