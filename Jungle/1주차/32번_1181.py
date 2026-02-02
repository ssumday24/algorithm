#1181 단어 정렬
#길이가 짧은 것부터
# 길이가 같으면  사전순으로 -
# 중복된 단어는 제거 

# a.sort() 만 해도 결과 바뀜

import sys

def quick_sort(a):
    def qsort(a,left,right):
        
        pl=left
        pr=right
        x=a[(left+right)//2]
        
        while pl<=pr:
            while a[pl]<x: 
                pl +=1
            while a[pr]>x: 
                pr -=1
            if pl<=pr:
                a[pl],a[pr]=a[pr],a[pl]
                pl +=1
                pr -=1    
        
        if left < pr : 
            qsort(a,left,pr)
        if pl < right:
            qsort(a,pl,right)
    

    qsort(a,0,len(a)-1)
  
####################################################

N=int(input())
a=set()

for _ in range(N):
    word=sys.stdin.readline().strip()
    a.add(word)
 
a=list(a)   
a.sort() #알파벳순 정렬
a.sort(key=len) #길이순 정렬

for word in a:
    print(word)
        