#2025.11.12 - 스택
# 10799 - 쇠막대기  

# 핵심 : 스택문제라고해서, 무조건 stack만 쓰는게 아니다.

import sys

x= sys.stdin.readline().strip() #괄호입력
stack=[]
result =0

for i in range(len(x)):
    if x[i]=='(':
        stack.append('(')
    
    elif x[i]==')':

        # 1. 레이저'()' 인 경우
        if x[i-1]=='(':
            #이제 이 레이저'()'는 안쓰므로 없애기 
            stack.pop()

            # 왼쪽 괄호의 개수를 더함 
            result  += len(stack)
            
           
        # 2. 막대기의 끝인 경우 
        elif x[i-1]==')':
            stack.pop()
            result +=1


print(result)