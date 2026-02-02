#9012: 괄호
import sys
input =sys.stdin.readline


N=int(input())

for _ in range(N):
    inputs = list(input().strip())
    stack=[]
    valid= True
 
    for i in inputs:
        if i =='(':
            stack.append(i)
        elif i ==')':
            if not stack : #스택이 비었다면
                valid=False
                break
            else:
                stack.pop()
            
        
    if (valid == True) and not stack: 
        #스택이 비었다면 YES
        print("YES")
    else:
        print("NO")
    
