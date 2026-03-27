# BOJ 2217
# 로프-S4
# 26.03.17
import sys

input = sys.stdin.readline
"""
그리디 연습문제(3)
[WIL]
- 지금 당장은 이득이더라도 나중 가서는 이득인 경우가 존재하는지
- N 크기부터 보기, 10^5 이상이면  N^2 풀이불가
    -> 이분탐색, 해시(딕셔너리),투포인터,DP(1차원),그리디 가능 
    
    
큰 로프부터 내림차순 정렬후, 하나씩 추가하면서 비교하기
"""

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

result = 0  # 구하는값, 최대중량
minval = 99999

# O(N logN)정렬
arr.sort(reverse=True)

# O(N logN)정렬 -> O(N) 완성
for i in range(N):
    # 지금 보고있는 로프가 가장 약한 로프
    minval = arr[i]

    # 인덱스가 i면 로프는 i+1개 사용
    # 최대중량 갱신
    result = max((i + 1) * minval, result)

# 출력부분
print(result)
