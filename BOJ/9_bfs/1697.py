# BOJ 1697
# 숨바꼭질-S1
# 26.03.19
"""
BFS 연습문제-5
[WIL]
- 1차원 BFS

bfs도중 n의 값이 10^5를 넘어갔다면 -1 연산만 해야하는데
이건 n->(n-1)->(n-1)*2 연산보다 무조건 느림
따라서 0~10^5 안에서 움직이는게 최선


"""
import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque()

# 초기화 크기 고민:
vis = [0] * 100001

# 시작점 큐에넣기
q.append(N)
vis[N] = 0  # 시작시간:0

# BFS 시작
while q:
    num = q.popleft()

    # K에 도착하면 종료
    if num == K:
        print(vis[num])
        break

    # num -> i로 이동가능
    for i in (num - 1, num + 1, num * 2):
        # 인덱스 범위 체크
        if i < 0 or i > 100000:
            continue

        # 방문체크
        if vis[i] != 0:
            continue

        # 방문체크후 큐에넣기
        # vis[i]= 이전시간+1초
        vis[i] = vis[num] + 1
        q.append(i)
