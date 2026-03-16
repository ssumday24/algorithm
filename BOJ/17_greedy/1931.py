# BOJ 1931
# 회의실배정-G5
# 26.03.16
import sys

input = sys.stdin.readline
"""
그리디 연습문제(2)

[WIL]
1. 그리디의 핵심은 지금 당장 최선을 고르는것
회의실을 가장 많이 빌려주려면? 
-> 앞 회의가 무조건 빨리 끝나야 내 뒤에 남은 빈 시간이 제일 길어짐
-> 끝나는 시간을 기준으로 오름차순 정렬1
-> 끝나는 시간이 같다면 "시작 시간이 빠른순" 정렬2

2번째 정렬에서 시작 시간이 빠른순으로 해야하는 이유는,
start=end 인 경우 (2,2)-(1,2) 로 정렬되므로 배치불가.

meetings.sort(key=lambda x: (x[1], x[0]))
(1순위: 끝나는 시간 오름차순, 2순위: 시작 시간 오름차순)

2. N=10^5 이므로  N^2 절대 불가능 
-> O(N *log N) 인 sort()이후 for 문 1번으로 끝내야함
최종: O(n logn) 
"""
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
