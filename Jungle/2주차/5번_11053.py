#11053 : 가장 긴 증가하는 부분 수열
import sys
input=sys.stdin.readline
import bisect

def binary_search_left(arr,target):
    left =0
    right = len(arr)
    # 원소를 삽입해야 하므로 인덱스가 하나더 많아야함
    # 탐색이라면 right =len(arr) - 1 
    
    
    while (left<right):
        mid = (left + right) //2
        
        if arr[mid] <target:
            left = mid +1
 
        elif arr[mid] >= target:
            right = mid 
    
    # left == right 이 되면서 while 빠져나옴
    return left  
    


 

N=int(input())
A=list(map(int,input().split()))
seq=[] #부분수열 

for i in A:
    pos=binary_search_left(seq,i)
    if pos ==len(seq):
        seq.append(i)

    else: # 더 좋은 값 대체 
        seq[pos]=i



print(len(seq))