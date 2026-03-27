#9020 골드바흐:

#골드바흐수 : 2보다 큰 모든 짝수는 "두 소수의 합"으로 나타낼수있나?
# 2<n<=10000 인 모든짝수 n에 대해 골드바흐 파티션은 존재.
# 여러가지인 경우, 두 소수의 차이가 가장 작은 것을 출력

T= int(input())

for _ in range(T):
    
    num = int(input())
    x1=[]
    x2=[]
    result_1=-99999
    result_2=-99999
    # 입력받은수 num 보다 작은 소수를 만드는 배열
    
    for i in range(2,num): # i가 소수인지 아닌지 판별
        
        not_prime=0  #소수인지 판별하는 not_prime
        
        for j in range(2,i): # 2부터 i-1을 검사
            if i % j == 0: # num은소수가 아님
                not_prime+=1
                break
            else : 
                continue
                
            # 지금까지 break로 안빠져나가고 살아남았다면
            # 소수이므로 i 를 배열에 추가'
        if not_prime ==0:
            x1.append(i) 
            
    x2=x1  # 배열 복사 
    
    min_gap=num
    
    for i in x1:
        for j in x2:
            if (i+j == num) :  
                gap =abs(i-j)
                
                if gap < min_gap:
                    result_1=i
                    result_2=j
                    min_gap=gap

    print(f'{result_1} {result_2}')

