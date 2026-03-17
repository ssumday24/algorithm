# BOJ 1931
# 회의실배정-G5
# 26.03.16
import sys

input = sys.stdin.readline
"""
그리디 연습문제(2)
[WIL]
- 지금 당장은 이득이더라도 나중 가서는 이득인 경우가 존재하는지
생각해보기

1. 그리디의 핵심은 지금 당장 최선을 고르는것
회의실을 가장 많이 빌려주려면? 
-> 앞 회의가 무조건 빨리 끝나야 내 뒤에 남은 빈 시간이 제일 길어짐
(귀류법으로 증명가능)
-> 끝나는 시간을 기준으로 오름차순 정렬1
-> 끝나는 시간이 같다면 "시작 시간이 빠른순" 정렬2

2번째 정렬에서 시작 시간이 빠른순으로 해야하는 이유는,
start=end 인 경우 (2,2)-(1,2) 로 정렬되므로 배치불가.

meetings.sort(key=lambda x: (x[1], x[0]))
(1순위: 끝나는 시간 오름차순, 2순위: 시작 시간 오름차순)
-> 파이썬은 튜플(A,B) 정렬시 앞부터 비교, A가 같으면 B비교 
+ 튜플은 한번 생성되면 불변성, 내부 순서쌍은 바뀌지xxxxxx

2. N=10^5 이므로  N^2 절대 불가능 
-> O(N *log N) 인 sort()이후 for 문 1번으로 끝내야함
최종: O(n logn) 
"""
N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

# end 기준오름차순 정렬 - start 오름차순 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# print(arr)

cnt = 0  # 총 회의수
time = 0  # 첫 시작시간 : 0시

for start, end in arr:
    # 회의 시작시간 >= 이전회의 끝난시간 일때
    if start >= time:
        time = end
        cnt += 1

        # 디버깅용
        # print((start,time))


print(cnt)
