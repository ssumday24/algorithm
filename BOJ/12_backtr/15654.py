# BOJ 15654
# N 과 M (5) - S3
# 26.02.26
"""
- 사전순으로 증가하는순 출력
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M= map(int,input().split())

# N개의 숫자 담은 list
# idx : 0 ~ N-1
nums = list(map(int,input().split()))

# 주의 : sort()의 반환값은 none이니 변수에 담지 x
# nums = sorted(nums)는 사용가능 
nums.sort()

arr=[]
vis=[False] * (N+1) # idx : 1~N 

def func(depth):
    if depth == M :
        for x in arr:
            print(f"{x}",end=' ')
        print()
        return
    
    # vis[i] : nums 의 [i] 번째 원소의 사용여부
    for i in range(0,N):

        if vis[i] == False :
            
            vis[i] = True
            arr.append(nums[i])

            func(depth+1)

            vis[i]=False
            arr.pop()

##########################    
func(0)

#print(nums)