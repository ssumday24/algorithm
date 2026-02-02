#2577 : 숫자의 개수

a=int(input())
b=int(input())
c=int(input())

result = a*b*c  # result = 17037300  =>각 원소들 리스트화 필요
result=str(result)


for i in range(10): # i : 0 ~ 9
    cnt = 0 
    
    for x in result:
        if int(x) == i :  # 문자열 '0' 을 정수화 한후 비교, 같다면
            cnt+=1 
            
            
    print(cnt)
    