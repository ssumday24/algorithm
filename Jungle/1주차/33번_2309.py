#2309 : 일곱 난쟁이
# 배열의 합=sum(A), 두명의합 = SUM - 100

a=[]
not_dwarf=set()

for _ in range(9):
    n=int(input())
    a.append(n)
    
a.sort()

for i in range(0,8): 
    for j in range(i+1,9):   # index 8 까지 탐색
        if (a[i]+a[j])==sum(a)-100:
            not_dwarf.add(a[i])
            not_dwarf.add(a[j])
            
            for x in a:                    # a=[7,8,10,13,15,19,20,23,25]
                if x not in not_dwarf:
                    print(x)                   
            exit()