# BOJ 1697
# 숨바꼭질-S1
# 26.03.19
# 26.03.20
""" """
import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [-1] * (200001)
q = deque()

# 시작점 큐에넣기
q.append(N)
visited[N] += 1  # 시작값: -1 -> 0

# 큐가 비지 않는동안 bfs
while q:
    # 큐에서 꺼낸후 다음이동 탐색
    curr = q.popleft()

    # K에 도달하면 정답출력후 종료
    if curr == K:
        print(visited[curr])
        sys.exit()

    # 3가지중 하나로 이동가능
    for i in [curr - 1, curr + 1, 2 * curr]:

        # 인덱스 범위 체크
        if i < 0 or i > 200000:
            continue

        # 이미방문한곳 제외
        if visited[i] != -1:
            continue

        # 방문처리후 큐에넣기
        # 이전숫자 vis[N]->vis[i] 로 이동횟수1 추가
        visited[i] = visited[curr] + 1
        q.append(i)
