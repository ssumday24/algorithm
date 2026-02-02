# 11279 : 최대힙
#최대 힙 : 부모노드 값 >= 자식노드 값 , 따라서 루트가 MAX
#최소 힙: 루트가 MIN
#파이썬의 heapq 는 기본적으로 최소 heap
import sys
import heapq

input= sys.stdin.readline
N=int(input())
heap=[]

for _ in range(N):
    x=int(input())

    if x==0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    
    else:
        heapq.heappush(heap,-x) # 음수로 넣어야 최대힙처럼 작동
        
