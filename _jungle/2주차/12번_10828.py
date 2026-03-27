#10828 : 스택
#중요점 : 스택의 find는 꼭대기에서 바닥쪽으로 검색

import sys
input=sys.stdin.readline

stack = []


N=int(input())
for i in range(N):
    instruction = input().strip().split()
    
    cmd=instruction[0]
    
    if cmd=='push':
        stack.append(int(instruction[1])) 
    
    elif cmd =='pop':
        if stack:
            removed=stack.pop()
            print(removed)
        else:
            print(-1)
        
    
    elif cmd=='size': #들어있는 정수의 개수
        print(len(stack))
            
    elif cmd =='empty':
        if stack:
            print(0)
        else:
            print(1)
        
        
    elif cmd == 'top':
        if not stack:
            print(-1)
        else: # 가장 위에있는 정수
            print(stack[-1])