#1026 : 보물 - 그리디
import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#A의 최소값과 B의 최대값을 반복
A.sort() #정렬하는순간 최소값부터 순서대로
B.sort(reverse=True)
total =0

for i in range(N):
    total += A[i] * B[i]
    
print(total)