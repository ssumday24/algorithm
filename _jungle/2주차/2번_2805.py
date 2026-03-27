# 2805 : 나무 자르기
# 나무의수 N, 집으로 가져는 길이 M
import sys
input= sys.stdin.readline


N, M = map(int,input().split())

trees= list(map(int,input().split()))

left=0                  # 톱의 높이 H : left ~ right 사이
right=max(trees)
H=0

#left,right,mid 는 인덱스가 아니라 값
#mid 를 구하는 과정 : 20 -> 10 -> 5 -> 2 -> 1 .....
while(left<=right): # H를 높일수록 가져가는 나무는 적어짐
    mid =(left+right) // 2  # 톱의 높이가 mid라고 가정
    total=0
    
    
    for tree in trees:
        
        if tree > mid: # 나무가 톱보다 클때 나무를 집에 가져감
            total += tree -mid
            
    
    if total >= M:  #나무를 M이상 가져갔으면 톱을 높이기
        H=mid  # 톱의 높이 H로 저장 , 
        left= mid+1

        
    elif total < M:  # 톱을 다시 낮추기
        right = mid -1 
    

print(H)



