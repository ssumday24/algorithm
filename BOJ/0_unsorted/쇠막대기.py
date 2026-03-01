# 10799 쇠막대기 - 스택
# 7월 29일 (화)
# 구하는것 : 잘려진 막대기 조각의 총 개수
"""
방법: 레이저를 기준으로, 현재까지 열린 막대기의개수에 따라 sliced ++
    이때 특수 케이스 : 중간에 끊어져 있을때 -> )(  

"""
# 1회차 걸린시간 : 3시간

import sys
inputs = sys.stdin.readline().rstrip("\n")

sliced= 0 # 잘려진 조각의 수
stack =[]


for i in range(len(inputs)): # x 는 각 괄호들
    if inputs[i]=='(':
        stack.append('(')

    elif inputs[i]== ')':
        if  inputs[i-1] == '(' : # ()레이저일때
            stack.pop()
            sliced += len(stack)

        else : # 레이저가 아닌, 닫는 막대일때 -> ))
            sliced +=1 #무조건 한조각이 더 잘림
            stack.pop()


print(sliced)