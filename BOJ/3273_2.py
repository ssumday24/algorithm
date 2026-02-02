# 3273 - 복습
import sys

n = int(sys.stdin.readline().strip()) # 수열의 크기
arr=list(map(int,sys.stdin.readline().split(' ')))
x = int(input()) # ai + aj = X 

result =0 # 최종값 

# 순서쌍의 개수 ?
# 추가배열의 크기 : x+1개
cnt_arr = [0 for _ in range(x+1)]

# cnt_arr에 1 만들어주기 
for num in arr:
    if num < x :
        cnt_arr[num]=1

# 본격적인 조사 시작
for num in arr:
    # 숫자는 x보다 무조건 작아야함 
    if num<x and cnt_arr[x-num] ==1 and x-num !=num : # X- num 값이 존재하면
        result +=1
        cnt_arr[num]=0 # 이제 필요없으니 0으로변경
        cnt_arr[x-num]=0

print(result) # O(N)에 해결가능 