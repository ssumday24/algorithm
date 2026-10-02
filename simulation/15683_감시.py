# BOJ 15683 감시
# 10.02
# 시뮬레이선 복습
"""
[조건]
- 0:빈칸 1~5:cctv 6:벽 #:감시영역
- 사각지대 최소크기=?

1. cctv 선택 , 8개이하
2. 

[문풀 노트]



"""

import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0  # 사각지대 최소크기
