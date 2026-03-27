#4344 : 평균은 넘겠지

#첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#둘째 줄부터 각 테스트 케이스마다 
# N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 

# 특정 케이스에 대해 생각해본 이후에 일반화?

c=int(input())

for i in range(c): # c번의 테스트 케이스
    
    x =list(map(int,(input().split())))
    
    n=x[0]
    score=x[1:]     
    
    total=0
    cnt= 0 # 평균을 넘는 사람의 수
    
    for j in score: # score=[50,50,50,70,100] 등
        total +=j   # j = 점수
        
    average = total / n
    
    for k in score:
        if k>average:
            cnt+=1
    
    
    result = (cnt/n) * 100 #백분위 변환
    
    print(f'{result:.3f}%')  #소숫점 셋재짜리까지 출력
    
