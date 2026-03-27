#1152: 단어의 개수
# continue 는 가장 안쪽의 반복문만 종료?



x=input().split(' ')  # 공백을 제거한문자열로저장

cnt=0

if x=='':
    print(0)

else:
    
    for i in range(len(x)):
    
        if (x[i]==''):
        #배열의 처음이나 끝이 공백일때
            pass   # cnt 증가시키지 않고 그대로
        
        else:
            cnt+=1

    print(cnt)