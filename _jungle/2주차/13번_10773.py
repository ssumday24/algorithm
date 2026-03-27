


K=int(input())

stack=[]

for i in range(K):
    num=int(input())
    
    if num == 0:
        stack.pop()
    else: #0이 아닌경우
        stack.append(num)
        

result = sum(stack)
print(result)
    

