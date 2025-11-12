#2025.11.12 
#균형잡힌 세상 - 스택
import sys
res =[] # 결과값 담을배열 

while True :

    sent = sys.stdin.readline().rstrip("\n")

    if sent == '.':
        break

    else:
        stack=[] # 괄호만 추가할 스택
      
        for  x in sent :
            # 왼쪽 괄호일 때
            if x =='(' or x=='[':
                stack.append(x)
            
            elif x==')':
                # 빈스택이 아니면서 짝이맞을때
                if stack  and stack[-1]=='(':
                    stack.pop()
                
                else:
                    stack.append(x)
                    break 
                   
            elif x==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                  
                else:
                    stack.append(x)
                    break
        #정답출력                           
        if not stack:
            print ("yes")
        else:
            print("no")
        
