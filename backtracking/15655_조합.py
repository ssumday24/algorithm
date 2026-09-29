# BOJ 15655
# N 과 M (6) - S3
# 26.03.02
"""
- 조합은 이전숫자는 보지도 않으니 used배열 필요없음
(오름차순인 경우)
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr_N = list(map(int, input().split()))
result = []  # 결과담을배열

# 오름차순이어야하니 sort
arr_N.sort()


def func(depth, start):
    # 고른 개수가 M개면 출력후 return
    if depth == M:
        print(*result)
        return

    # idx : num~(N-1)
    # (인덱스 기준) arr[num]~arr[N-1] 이 사용되었는지
    for i in range(start, N):
        result.append(arr_N[i])

        # 다음 깊이진행
        """
            몇번째 수를 인자로 골랐는지(i값을) 넘겨야
            다음 깊이부터는 그 숫자이후(i+1)부터 선택하게됨
            """
        func(depth + 1, i + 1)

        # 상태복구
        result.pop()


####
# 오름차순이라 start =0 넘기면됨
func(0, 0)
