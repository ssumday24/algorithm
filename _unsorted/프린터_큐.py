#1966  - 2주차 시험 2번 - 프린터 큐
from collections import deque

# 1. deque 사용
# 2. heapq 라이브러리 사용 -> 비추천


case= int(input()) 

for _ in range(case):
    N,M=map(int,input().split())
    P=deque(map(int,input().split()))
    
    check=deque([0]*N)  #인덱스 체크용 배열, 0으로 초기화
    check[M]=1 #우리가 찾을 곳 위치만 1로 지정
    
    cnt =0 # 문서가 몇번째로 print 되는지 카운트
   
    
    max_val = max(P) 
    
    while P: # 덱이 빌때까지 반복
        if P[0] <max_val:
            out=P.popleft()
            out_check= check.popleft()
            
            #이때 값이 비었다면
            if not P:
                break
            
            P.append(out) #앞에있는게 뒤로 다시감
            check.append(out_check)
            
        else: #이때만 출력가능
            out=P.popleft()
            is_target= check.popleft()
            cnt+=1
            
            #이때 값이 비었다면
            if not P:
                break
                
            max_val=max(P) #MAX 값 다시 계산
            
            #값이 중복될때도 처리가능
            if  is_target:
                break
    print(cnt)