#10871 : 


# N 개의 정수로 이루어진 배열 A
N,X = map(int,input().split())
A = list(map(int,input().split()))

B=[]

# A 에서 

for i in A :  # 정수i 가 배열 A 에 있는 동안
    if i < X :        # X 보다 작다면
        B.append(i)   # 빈 배열 b에 추가
        

for i in B:
    print(i,end=' ') # 공백 추가