# 10.30(목)
#0x01 강의 연습문제  -> o(N) 으로 풀이


def func2(arr,N):
    result = 0; # 디폴트값

    cnt=[0 for _ in range(101)] # idx 0은 비워두고, 1~100 사용

    for num_1 in arr:
        if cnt[100-num_1] ==1 : 
            result=1
            break

        cnt[num_1]+=1 # 이제 방문체크 
    print(result) 


# int() 형변환은 문자열 하나 or 숫자 한개만 변환가능.
# 따라서 map 사용 
# 입력예시: 1 23 53 77 60
arr=list(map(int,input().split(' ')))
N=len(arr)

func2(arr,N)
