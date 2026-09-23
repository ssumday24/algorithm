# 스타트링크_5014
# 26.04.01
"""
총F층/ S층 -> G층

ex1) 1층-10층
1-3-5-7-8-9-10
6번이동


"""

import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
arr = [0] * (F + 1)  # 1층~F층

# 시작점에서 방문체크후 bfs
q = deque()
q.append(S)
arr[S] = 1

while q:
    cur = q.popleft()

    # 목적지 도착
    if cur == G:
        # 시작점 1로 시작했으니 상쇄
        print(arr[cur] - 1)
        sys.exit()

    # U / D 중 한곳으로 이동
    for d in [(-1) * D, U]:
        nx = cur + d

        # 범위 벗어나는곳으로 이동불가
        if nx <= 0 or nx > F:
            continue

        # 이미 방문한곳은 절대 최단거리x
        if arr[nx] != 0:
            continue

        # 이동 계산
        arr[nx] = arr[cur] + 1
        q.append(nx)

    # #디버깅
    # for x in q:
    #     print("현재큐 상태:",end=" ")
    #     if x!=0:
    #         print(x,end=" ")
    # print()

###
# break 안걸렸으면 도착불가
print("use the stairs")
