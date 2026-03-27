#2630 색종이 만들기
import sys

def divide(x,y,N): #한변의 길이: N
    global white, blue
    color = arr[x][y]
    same = True #디폴트 True로 설정
    half = N // 2
    
    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j] !=color:
                same = False
                break
        
        if same == False:
            break
    
    if same: # 계속 같았다면
        if color ==0:
            white +=1
        else:
            blue +=1 
        return
    
    else: # if same ==False:
        divide(x,y,half) #왼쪽위 (x+half,y+half 까지만탐색)
        divide(x,y+half,half)  # 오른쪽위
        divide(x+half,y,half)  #왼쪽 아래  
        divide(x+half,y+half,half) #오른쪽 아래

    

##############################################
N=int(sys.stdin.readline())
arr=[]
white=0
blue=0

for _ in range(N):
    row=list(map(int,sys.stdin.readline().split()))
    arr.append(row)
    
divide(0,0,N)

print(white)
print(blue)