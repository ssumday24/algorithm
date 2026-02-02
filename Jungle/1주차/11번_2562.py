#2562:

# 9개의 '서로다른' 자연수가 주어질때 

max=0
x=[]

for i in range(9): 
    n = int(input())
    x.append(n) #  빈 배열 x에 숫자 추가


MAX = x[0]  # 일단 첫번째 값을 최대값으로 가정
index = 0 #  최댓값이 몇번째 수인지? => 일단 0으로 초기화

for i in range(9) :  # i = 0 ~ 8  
    if x[i] >= MAX:
        MAX=x[i]
        index=i+1   # ex) x[2] 가 최댓값이라면  index = 3
     
    
print(MAX)
print(index)
    
