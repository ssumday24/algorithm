#2750 : 수 정렬하기
import sys
    
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
    
    if left < pr : qsort(a,left,pr)
    if pl < right:qsort(a,pl,right)
    
def quick_sort(a):
    qsort(a,0,len(a)-1)



n=int(input())
a=[]   
for _ in range(n):
    x=int(sys.stdin.readline())
    a.append(x)


quick_sort(a)

for i in a:
    print(i)

    
            

    