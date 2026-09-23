# BOJ 11729 하노이탑이동순서-G5
# 26.02.10
"""
f(1) = 1
f(2) = 3
f(3) = (1->3) ,(1->2),(3->2),(1->3) + f(2)를 수행한것과 동일
=7
f(4) = 8번 이동 + f(3)   = 15

f(4) 의 8번 이동 == f(3) 이후 가장큰것을 1->3 으로 이동 한것과 동일
즉 f(4)= f(3) + 1 + f(3),
같은 방식으로
f(3) = { f(2) + 1 } + f(2),
f(n) = 2f(n-1)+1  의 일반항 도출,

base case -> n==1

f(n-1)을 알면 f(n) 을 구할수있으니
"원판을 n-1 개 옮길수 있으면 -> 원판이 n개일떄도 옮길 수 있다" 명제가 참이므로 귀납적으로 문제해결 가능 

"""
import sys
input = sys.stdin.readline

N = int(input())

# 이동경로는 어떻게 처리?
def f(n,start,end):
    # start -> end 로 단 1개 이동 
    if n==1 :  
        print(f"{start} {end}")
        return

    # start + end + (중간지점) = 6
    # 1. n-1 개를 start -> (중간점) 으로 옮기기
    f(n-1,start,6-start-end)

    # 2. 가장큰 원판을 start -> end 로 이동
    f(1,start,end)

    # 3. n-1 개를 중간점 -> end 로 이동
    f(n-1,6-start-end,end)

# 이동횟수
print(2**N - 1)

# 이동경로
f(N,1,3)
