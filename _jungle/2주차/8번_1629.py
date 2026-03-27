#1629 : 곱셈 - 분할정복
# (A^B) % C =? 

def mod_divide(A,B,C):
    # (a*b) mod C = ((a mod c)*(b mod c))mod c
    if B==0:
        return 1%C
    
    divide = mod_divide(A,B//2,C)
    
    if B %2 ==0 : # B= 짝수일때
        result = (divide*divide)%C 
        return result   
        
    else: # B = 홀수일때 짝과 홀로 다시분할
        
        if B==1 : # 더이상 나눌수 없을때
            result = A % C
            return result
        
        else :
            result = (divide * divide * (A%C))% C
            return result
    
    
        



A,B,C=map(int,input().split())
print(mod_divide(A,B,C))