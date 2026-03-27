#1197 : MST 최소신장 트리
import sys
input=sys.stdin.readline

V,E = map(int,input().split())

result =0  #MST 의 가중치 
M=[[0]*(V+1) for _ in range(V+1)] # 인접 행렬 그래프

#0번 인덱스는 비워두자

for i in range(1,E+1): # i = 1~ E
    A,B,C = map(int,input().split()) #C는 가중치
    
    M[A][B]=C
    M[B][A]=C
    

for i in range(V+1):
    print(M[i])
    