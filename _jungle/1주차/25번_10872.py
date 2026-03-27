#10872 : 팩토리얼

N=int(input())


def fact(n):
     
    if n==0:
        return 1
     
    else : # n>=1
        return n * fact(n-1)
    
print(fact(N))