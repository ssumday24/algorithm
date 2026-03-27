import sys
input= sys.stdin.readline
# 큐에서는 pop 연산 X
# 큐가 비어있을 조건은 front ==back

N = int(input())
queue=[0]*2000000
front=0 # front , back 은 index. back은 push시 저장될 위치
back=0


for _ in range(N):
    inputs = input().strip().split()
    
    cmd=inputs[0] #배열에 어떻게 저장?
    
    if cmd=='push':
        queue[back]=inputs[1]
        back +=1    
       
        
    elif cmd=='pop':
        
        if front ==back: # 비어있는경우 -1
            print(-1)
        
        else:
            print(queue[front])
            front +=1
       
                
    elif cmd=='size':
        print(back-front)
        
    elif cmd=='empty':
        if front==back :
            print(1)
        else:
            print(0)
        
    elif cmd=='front':
        if front==back:
            print(-1)
        else:
            print(queue[front])
        
    elif cmd=='back':
        if front==back:
            print(-1)
        else:
            print(queue[back-1])