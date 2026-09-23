# BOJ 1697 숨바꼭질
# BFS 복습(5) - 26.09.23
"""
[문풀 노트]
- N값의 범위

"""

from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # N:수빈 K:동생

# idx: 0~ 2K 사용
vis = [0] * (2 * K + 1)
q = deque()

# 시작점 체크후 큐에넣기
vis[N] = 1
q.append(N)

# 1차원 bfs
while q:
    cur_x = q.popleft()

    # -1,+1,*2
    for nx in [cur_x - 1, cur_x + 1, cur_x * 2]:

        # 범위체크
        if nx < 0 or nx > 2 * K:
            continue

        # 이미 방문한곳 = 최단시간x
        if vis[nx] != 0:
            continue

        # 방문체크,큐에넣기
        vis[nx] = vis[cur_x] + 1  # 이전지점에서 1번 이동
        q.append(nx)

# 결과
print(vis[K] - 1)

# print(vis)
