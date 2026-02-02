#1978: 소수찾기

def prime(num):
    
    if num == 0 or num==1 :
        return 0 
    # 0과 1은 소수아님
    
    
    for i in range(2,num): # 2~ (num-1) 까지 확인
        if num % i ==0 : 
            # 나누어떨어짐 => 약수가 있으면 소수가 아님
            return False
  
        
    return True  # 다 돌아서 반복문 나왔으면 소수  
            

N=int(input())

x=list(map(int,input().split()))

cnt =0  # cnt는 소수의 개수

for i in range(N): # N 만큼 반복
    cnt = cnt + prime(x[i])
    

print(cnt)