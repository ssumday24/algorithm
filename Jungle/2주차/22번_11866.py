#11866: 요세푸스 원순열
#queue = [1, 2, 3, 4, 5, 6, 7]
# K=3 이라면:
# 1 → 뒤로 보내
# 2 → 뒤로 보내
# 3 → 제거 (출력)
# 다시 4부터 시작...

N,K= map(int,input().split())
queue=list(range(1,N+1))


result=[]
cnt=0

while(queue): 
    for _ in range( K-1):
        
        queue.append(queue.pop(0))
        
    result.append(queue.pop(0))
    
    
print("<"+", ".join(map(str,result))+">")

        
            
         
    






