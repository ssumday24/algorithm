#1388 바닥장식 -반복문버전
import sys

N,M  = map(int,input().split())
cnt=0 # 나무 판자 개수 

nx=[-1,1,0,0]
ny=[0,0,-1,1]
arr=[]

for _ in range(N):
    row=input()
    arr.append(row)

for i in range(N):
    
    for j in range(M):
        
        if arr[i][j]=='-':
            
            if j==0: # 첫 '열'에 바로 가로판자가 나올때
                cnt+=1
            else: 
                if arr[i][j-1]=='|' : # 전 '열'이 세로판자일때
                    cnt+=1
            
        elif arr[i][j] == '|':  #바로 윗행에 세로판자 '|'가 있었다면,
            
            if (i>=1 and i<=N-1) and (arr[i-1][j]=='|'): 
                continue  #증가없이 그대로 
            else:
                cnt +=1

       
    



print(cnt)

