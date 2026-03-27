#1931 : 회의실 배정
import sys
input = sys.stdin.readline

N= int(input())
arr=[tuple(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1],x[0]))

#for i in arr:
#    print(i)

answer= 0 # 회의의 개수
present = 0 #현재 시간 t
for start, end in arr:
    if start >= present:
        present = end
        answer += 1
    

print(answer)
#print(present)
