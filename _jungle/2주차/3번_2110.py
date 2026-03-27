#2110 공유기 설치
import sys

def can_place(arr,mid,C):
    count=1
    last_pos = arr[0]  #마지막에 공유기 설치한 위치 
    
    for i in range(1,len(arr)):
        if arr[i] - last_pos>=mid:
            count +=1       #공유기설치
            last_pos=arr[i] #설치 위치 저장
            
    return count >= C  # C개이상 설치할수있으면 True


def max_dist(arr,C):  #N=집의개수 / C=공유기개수
    d=0
    
    if C==2 : 
        print(arr[-1]-arr[0])  # C=2일때는 양끝에 설치
        return 
    
    # C>=3 일때 : 양\left <= result <=right
    left=1  #공유기간 최소 거리 = 1
    right = max(arr) - min  (arr) #공유기간 최대거리
    result =0 
    
    # 이진탐색 구간 , left와 right 사이의 result 찾는 과정 
    while ( left <=right):
        mid =(left+right) //2
        if can_place(arr,mid,C) == True:
            result = mid
            left = mid +1  # 더 큰 거리 시도
        else: # can_place == Flase 일때 
            right = mid -1 # 거리 줄이기
            
    print(result)    
        
   

#########################################
N,C= map(int,sys.stdin.readline().split())
arr=[None]*N

for i in range(N):
    x=int(sys.stdin.readline())
    arr[i]=x

arr.sort() # 일단 정렬
max_dist(arr,C)