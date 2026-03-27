import sys
input = sys.stdin.readline

N = int(input().strip())    
arr=list(map(int,input().split()))
result=[0]*N
stk=[] #이 스택에는 인덱스 저장



for i in range(N):
    
    current_height = arr[i] #현재 탑 기준
    
    #스택이 비어있지 않고 현재탑이 더 클때 !
    while( stk and arr[stk[-1]]<current_height):  
        stk.pop()
       
   
    # 현재탑이 (스택의 top보다) 더 작을때
    if stk :
        result[i] = stk[-1]+1  #몇번째 기둥이니 1더함
    
    #스택에 탑의 인덱스  추가 

    stk.append(i)

for i in result:
    print(i,end=' ')