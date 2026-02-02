#1541 잃어버린 괄호
import sys
#input = sys.stdin.readline

# 다음엔 for i , num in enumerate(x) 쓰기

x= input().split('-')
calc=0

first = True

for num in x:
    # 안에 +가 있다면 식별
    
    if '+' in num:
        temp = sum(map(int,num.split('+')))    
        
    else:
        temp = int(num)
    
    if first:
        calc+=temp
        first=False
    
    else: # '-' 앞의 첫 숫자가 아닐 때
        calc-=temp
        


print(calc)

