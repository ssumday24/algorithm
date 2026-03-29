# 좌표압축_18870
# 26.03.29
"""
좌표압축
- 중복을 제외하고 나보다 작은수가 몇개?

1. set() 중복제거
uni= sorted(list(set(arr))
"""

import sys
from collections import deque

input = sys.stdin.readline

from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, input().split()))

# 원본배열의 순서대로 출력해야하니까
# 복사배열 사용
copy = arr[:]

# 1.정렬
copy.sort()

# 2.중복제거 - 정렬pt.2 보기
uni = []  # 중복제거된 unique
for i in range(N):
    # 앞의 숫자와 비교해서 다를때만 추가
    if i == 0 or copy[i - 1] != copy[i]:
        uni.append(copy[i])

# 3.이분탐색
# 원본배열의 순서대로 출력해야하니
for target in arr:
    # 타겟이 처음으로 나오는 인덱스 i,
    # 타겟보다 작은수도 i개
    print(bisect_left(uni, target), end=" ")
