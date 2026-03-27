#2252 : 줄세우기 / 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

def top_sort(N,graph,in_degree):
   
    result=[] #위상정렬 결과 담을곳
    queue=deque()
    
    for i in range(1,N+1): # index=0인 노드는 제외 
        if in_degree[i]==0:
            queue.append(i)
    
    while queue: 
        out = queue.popleft() #큐에서 하나씩 pop
        result.append(out)
        
        for x in graph[out]:  #degree가 0이되면 큐에 추가
            in_degree[x] -=1
            if in_degree[x] ==0:
                queue.append(x)



    return result



############################################
N,M =map(int,input().split())
graph={i:[] for i in range(1,N+1)}  #1번부터 n번 노드까지
in_degree=[0]*(N+1) #진입차수 저장 - 0번은 버림




for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append[B]
    in_degree[B]+=1   #indegree = [0,0,0,2]

#결과 출력
res = top_sort(N,graph,in_degree)
for i in res:
    print(i,end=' ')

