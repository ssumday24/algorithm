# 2675:문자열 반복

N=int(input())

for _ in range(N):
    
    R , S = input().split(' ')
    
    R = int(R) # 문자열=> 정수
    
    for i in S: #ABC 
        
        for j in range(R): # R번반복
            print(i,end='') # AAA    
    print()
    