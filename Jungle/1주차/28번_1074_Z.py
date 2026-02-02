#1074 : Z 

# N이 주어졌을때 R행 C열을 몇번째로 방문?

N,R,C = map(int,input().split())

def Z(N,R,C):
    
    if N==0:              # N=3
        return 0
    
    half  = 2** (N-1)       #half=4
    area = half * half      #넓이 = 16
      
    if R<half and C<half: #1사분면
        return Z(N-1,R,C)
    
    if R<half and C>=half: #2사분면
        return area + Z(N-1,R,C-half)
    
    if R>=half and C<half: #3사분면
        return 2*area+Z(N-1,R-half,C)
    
    if R>=half and C>=half: #4사분면
        return 3*area+Z(N-1,R-half,C-half)
    
    
#################################
# 2^(N-1) * 2^(N-1) 행렬

result=Z(N,R,C)
print(result)