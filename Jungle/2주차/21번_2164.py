#2164 : 카드2
import sys
input = sys.stdin.readline
N=int(input())

queue= [i for i in range(1,N+1)]
front = 0
rear  = N
capacity = N 
present_size=N # 여기서는 N으로 차있음

while (present_size>=2):
    #1.디큐 
    out = queue[front]
    front +=1
    
    if front == capacity: # front 가 맨뒤로 갔으면 되돌림
        front = 0
    
    present_size -=1 #현재사이즈 1감소
    
    if (present_size==1):
       break
    
    
    #2. 제일위를 카드 밑으로 "디큐" 후에 ->  "인큐"
    out = queue[front]
    front +=1
    
    if front == capacity: # front 가 맨뒤로 갔으면 되돌림
        front = 0
    if rear == capacity : # rear가 맨뒤로 갔으면 되돌림 
        rear = 0
    
    queue[rear] = out  #제일 위 카드가 맨 뒤로 
    rear +=1

print(queue[front]) #마지막에 남는 카드