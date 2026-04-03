# BOJ 14889
# 스타트와 링크
# 26.04.04
# 26.04.14
"""
[문제조건]
- S[i][j] 는 S[j][i]와  다를수있음
- 두 팀의 능력치 차이 "최소"=?

[문풀 노트]
- visited 를 사용해 O(1)에 바로 계산하기

"""
import sys
from collections import deque

input = sys.stdin.readline
