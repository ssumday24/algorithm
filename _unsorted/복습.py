#복습 - 11047 동전0
import sys
input=sys.stdin.readline
N,K = map(int,input().split())
coins=[]
for i in range(N):
    coin=int(input())
    coins.append(coin)

result =0 #필요한 동전 