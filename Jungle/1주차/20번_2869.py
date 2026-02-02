#2869 : 달팽이는 올라가고 싶다

# 낮에 A 미터 + , 밤에 B 미터 - 
# 높이는 V미터
# 모두 올라가려면 며칠?
import math
A,B,V = map(int,input().split(' '))   

# up = 0  # 지금까지 올라간 높이
# day= 1  # day1 부터시작

# while True:
    
#     #낮
#     up += A
    
#     if up >= V :  # 낮에 올라갔을때 도착점 이상 이라면 바로끝
#        break
    
#     #밤
#     up -= B
    
#     day +=1   #밤이 지나면 하루 추가


# print(day)
######################################################

# 마지막날을 제외하면 V-A 거리를 하루에 (A-B) 감

Q = (V-A) // (A-B)   # A,B,V = 2 1 3
R = (V-A) % (A-B)
if (R==0):
    day = Q + 1
else: #나머지가 있다면 이틀 더가야함
    day = Q + 2



print(day)