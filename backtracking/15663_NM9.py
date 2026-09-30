# BOJ 15663 N과M(9)
# 백트래킹 복습 - 26.09.30
"""
[노트]
- 입력 자체에 중복된 수가 존재
  [1, 7, 9, 9]

- visited
   같은 인덱스를 한 수열에서 두 번 사용하는 것 방지

- prev
   같은 depth에서 같은 값을 여러 번 선택하는 것 방지

- 핵심:
  각 depth마다 이미 선택한 값을 기억
   prev는 함수 내부 지역변수로 둠

- arr 정렬 필요
  같은 값들이 붙어 있어 중복 제거가 쉬워짐
"""

import sys

input = sys.stdin.readline


def func(depth):
    if depth == M:
        print(*result)
        return

    temp = None

    # arr[i] 가 넣을수 있는 수인지 체크
    for i in range(N):

        # 현재 위치에는 같은수가 여러번 나오면 안됨
        if not visited[i] and arr[i] != temp:

            # 결과에 추가
            visited[i] = True
            result.append(arr[i])

            # 다음 반복문에서 확인한 temp 변경
            temp = arr[i]

            # 다음 깊이
            func(depth + 1)

            # 상태복구
            visited[i] = False
            result.pop()


#########
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

# 자기자신 제외하고 골라야하니 vis필요
visited = [False] * N


# 1.정렬
arr.sort()

# 2.백트래킹
func(0)
