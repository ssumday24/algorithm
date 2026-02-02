# 4949 -스택  
# 날짜 7월 29일 (화)
import sys

while True:
    line = sys.stdin.readline().rstrip("\n")

    if line == '.' :
        break  # 입력 종료조건

    stack =[]

    for char in line: # 각 문자마다 검사
        if char == '(':
            stack.append(char)
            
        elif char =='[':
            stack.append(char)
           

        elif char ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break

        elif char ==']':
            if stack and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(char)
                break
        
        

    if (not stack ):
        print("yes") # 스택이 비어있으면, 즉 조건에 안걸렸으면 yes 출력
    else: 
        print("no")