# BOJ 15656
# N 과 M (7) - S3
# 26.03.06
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))

def backtr(depth):
    if depth==M:
        for elem in new_arr:
            print(f"{elem} ",end='')
        print()
        return
    
    # idx : 0~(N-1)
    for i in range(N):
        # 숫자 사용
        new_arr.append(arr[i])
        
        #다음깊이 진행
        backtr(depth+1)

        new_arr.pop()

arr.sort()

#결과 담을 배열
new_arr=[]
backtr(0)