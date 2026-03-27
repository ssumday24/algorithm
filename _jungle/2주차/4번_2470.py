#2470 두 용액 => 투포인터 방식 : O(N)
# 투포인터 조합에서 이미 지나간 포인터는 돌아가지 않음.
# 투포인터는 가장 0에 가까운 합이 보장되도록 움직임

import sys
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

arr.sort()

left=0
right=N-1
min_result=float('inf') # 초기값 설정
answer=(0,0)

while(left<right): #서로 다른 두수를 고르므로 등호 X
   
    total = (arr[left]+arr[right])
    
    if abs(total)<min_result:
        answer =(arr[left],arr[right])
        min_result = abs(total)
    
    
    if total == 0:
        answer=sorted(answer)
        print(answer[0],answer[1]) 
        exit()
    
    elif total < 0 : #합이 음수일때 큰수로 TRY
                    # Sort 해놨기에 arr[left+1]은 큰수 보장.
        left +=1  
    
    elif total > 0: # 합이 양수일때 작은수로 TRY
        right-=1    # sort 해놨기에 arr[right-1]은 작은수 보장.
        
    
    # left > right 이면 종료

answer=sorted(answer)
print(answer[0],answer[1]) 