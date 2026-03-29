# 숫자카드2 #10816 - S4
# 26.03.28
"""
하한/상한 이분탐색
# (while start < end) 등호 없음 주의
# 중요: 이분탐색과 다르게 end = len(arr)

1. 이분탐색으로 개수를 구하는 공식
- 개수  = Upper - Lower
- Lower bound : 타겟 숫자가 처음 "시작하는" 위치
- Upper bound : 타겟보다 "큰 값"이 처음 나오는 위치
- bisect 라이브러리로 가능
- 수의 등장횟수 = bisect_right(arr, target) - bisect_left(arr, target)
- [start,end) 등호 생각 - 반 개구간

2. 딕셔너리
"""

# 타겟이 처음 나오는 인덱스 찾기
# mid에서 타겟을 찾았더라도, 이게 진짜 처음 나온건지 확인위해
# 범위 계속 좁혀감
def lower_bound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        # mid 가 타겟값일때, 처음나오는 위치는 mid 이하이므로
        # end = mid
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1

    # 종료조건 : start ==end , 둘중 아무거나 리턴
    return start


# 타겟보다 큰값이 처음으로 나오는 위치
# mid에서 타겟과 같은값을 만나도, 계속 오른쪽으로 이동
# start,end 를 다음 탐색 구역으로 생각
def upper_bound(arr, target):
    start = 0
    end = len(arr)
    """
    arr[1,2,2], targe=2 일때
    upper_bound 는 배열의 끝 너머의 3
    그런데 end = len(arr)-1 로 설정하면 2가최대니 도달불가
    """

    while start < end:
        mid = (start + end) // 2

        # 타겟값을 만나도 그 인덱스 이상부터 보기
        if arr[mid] <= target:
            start = mid + 1

        # mid 값이 , 우리가 원하는 타겟보다 큰값이 처음으로 나오는 위치일 수도 있으니 end= mid-1 이 아니라 end = mid
        # 즉 타겟보다 큰 값을 만나면 일단 "후보" 로 두고 왼쪽을 좁힘
        elif arr[mid] > target:
            end = mid

    return start


# 기본 이분탐색
def bi_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        # 타겟이 오른쪽에 위치
        elif arr[mid] < target:
            start = mid + 1

        # 타겟이 왼쪽
        elif arr[mid] > target:
            end = mid - 1

    # 못찾음
    return 0


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

# 1.정렬 o(n logn)
arr.sort()

# 숫자 M 을 몇개 가지고 있는지
for target in arr_m:

    tmp1= lower_bound(arr,target)
    tmp2= upper_bound(arr,target)

    # 출력
    print(tmp2-tmp1, end=" ")
