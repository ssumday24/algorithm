# 1920 : 수 찾기

def binary_find(): #이진탐색 함수
    A_arr.sort() #탐색전에 정렬
     
    for i in range(M): # M안의 원소 i 에 대해 체크
        key = M_arr[i] # key = 값
        left=0 #인덱스
        right=N-1 #오른쪽 인덱스
        center = (left+right) // 2
          
        while (True):  
            if key == A_arr[center]: #값으로 비교
                
                print(1)
                break
            
            elif key < A_arr[center] :
                right=center -1 
                center = (left + right) // 2
                
            elif key > A_arr[center]:
                left=center+1
                center = (left+right) // 2 
                
            if left > right:
                print(0)  #일치하는게 없었으면
                break
                
      
###############################

N=int(input())
A_arr=list(map(int,input().split())) # N개의 수
M=int(input())
M_arr=list(map(int,input().split())) # M개의 수

binary_find()