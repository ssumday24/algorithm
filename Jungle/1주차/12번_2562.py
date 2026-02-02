# 8958 : OX 퀴즈
n=int(input())



for i in range(n):

    cnt =0 # cnt 는 연속된 'O' 의 개수
    score = 0 # 총 점수


    x = list(input())  # 배열 x에 입력

    for k in x:
        if k == 'O':
            cnt = cnt + 1      # O 를 만나면 연속된 O 개수 1 추가
            score = score + cnt 
            #print('O 만남')
        else: # k == 'X' 
            cnt = 0   # cnt 0으로 초기화 하고 점수도 그대로
            #print('X 만남')
    print(score)

