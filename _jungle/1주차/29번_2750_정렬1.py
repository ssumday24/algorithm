#2750 : 수 정렬하기

def bubble_sort(a): #버블정렬
    n=len(a)
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if a[j-1] >a[j]:
                a[j],a[j-1]=a[j-1],a[j]
 
def insertion_sort(a): #삽입정렬
    n=len(a)
    for i in range(1,n): 
        j=i
        temp=a[i]
        while j>0 and a[j-1]>temp:
            a[j]=a[j-1]
            j=j-1
        a[j]=temp


n=int(input())
a=[]   
for _ in range(n):
    x=int(input())
    a.append(x)

#insertion_sort(a)
#bubble_sort(a)
quick_sort(a)

for i in a:
    print(i)

    
            

    