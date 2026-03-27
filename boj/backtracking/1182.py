# BOJ 1182
# 부분수열의 합 - S2
# 26.02.27
"""
N개의 합 = S 경우의 수 

- {-3,-2,5} {-2,-3,5}는 같으니 중복 제거 -> 조합
- 합이 정답이 되었다고 탐색을 멈추지말고, 제일깊게 가봐야
    - EX) [5,-3,-2] 에서 멈추면 [5,-3,-2,-1,1] 놓칠수도

- 조합이면 자신부터 보면되니 start로 인자 넘겨주기 
- 조합이면 vis 배열 필요 x 

- 이문제는 가지치기가 불가능하니 브루트포스
"""
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split())) # idx : 0 ~ (N-1)

result=[]
cnt = 0 

arr.sort() # 오름차순 정렬 - 필수일까?

# sum : 부분수열의 합
def func(depth,sum,start):
    global cnt  # 함수 내부에서 외부의 변수 접근
    
    # 맨처음 호출에 sum = 0 일때 방지 위해 result 비었는지 확인
    # cnt++ 만 하고 계속 진행 (가지치기x)
    if result and sum == S : 
        cnt+=1
        
        # ##### 디버깅용 출력
        # for x in result:
        #     print(f"{x} ",end='')
        # print()
    
    if depth == N : # 가장 깊은곳까지 탐색했을때: return
        return  

   # 중복제거(조합) 이므로 idx : start ~ (N-1) 
    for i in range(start,N):
     
            result.append(arr[i])
            
            # 부분합에 arr[i] 더해지니 인자로 넘겨주기
            # 3번째 인자에는 i+1 넣어줘야함 
            func(depth+1,sum+arr[i],i+1)

            # return 으로 올라왔으면 상태 원상복구  
            result.pop()


#########################
# 시작 : depth =0 , sum = 0 , start = 0 (인덱스)
func(0,0,0)

print(cnt)