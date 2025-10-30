# 3273 : 두수의 합 
# 10.30 (목)
# 투포인터로 풀수있다고함 

n=int(input())
arr= list(map(int,input().split(' ')))
x = int(input())

# 수열의 크기 n  / 배열 arr / 두수의 합 x 
result =0

cnt_arr = [0 for _ in range(x+1)] # 인덱스0은 사용x

for k in arr:
    # x - k 수가 존재한다면 , 순서쌍개수 추가. 
    if (x-k <0):
        continue # 음수가 되면 어차피 해당안되니 스킵 

    cnt_arr[k]=1

    if x-k != k and cnt_arr[x - k]==1 :  
        result+=1

print(result)
