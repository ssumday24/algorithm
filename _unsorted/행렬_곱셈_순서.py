import sys 
input=sys.stdin.readline
N = int(input())

row = []
col =[]
dp=[0]*(N+1)

for i in range(N):
    R,C = map(int,input().split())
    row.append(R)
    col.append(C)

        