# BOJ 15663
# N 과 M (9) - S2
# 26.03.13
import sys

input = sys.stdin.readline
"""
[WIL]
# 같은 깊이에서, "방금전에 사용한 숫자" 기억하는 방법
'특정 깊이전용 휘발성 메모리' 변수 스코프
-> 깊이별로 변수를 두기.

- 중복선택 못하니 visited 필요 
- 중복되는 수열을 여러번 출력하면안됨
ex) 1,7,9,9]: (1 9),(1 9) 중복출력 해결필요
"""


def func(depth):
    # 원소 m개를 골랐을때
    if depth == M:
        for x in result:
            print(x, end=" ")
        print()
        return

    # 같은 깊이에서, "방금전에 사용한 숫자" 기억
    prev = 0

    # idx: 0~(N-1)
    for i in range(N):

        # arr[i]를 안썼을때 + 방금쓴 숫자가 중복이아닐때
        if not visited[i] and prev != arr[i]:
            # 방문체크후 append
            visited[i] = True
            result.append(arr[i])

            # prev 갱신
            prev = arr[i]

            # 다음깊이
            func(depth + 1)

            # 상태복원
            visited[i] = False
            result.pop()


# main
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
# arr[idx]가 사용되었는지 체크 ,idx : 0~(N-1)
visited = [False] * (N)

arr.sort()
func(0)


# unique_arr = [] # 중복이 없는 수들만 담을 새 배열

# for i in range(N):
#     is_duplicate = False # 일단 중복이 아니라고 가정

#     # 내 앞(0 ~ i-1)에 똑같은 애가 있는지 검사
#     for j in range(0, i):
#         if arr[i] == arr[j]:
#             is_duplicate = True
#             break # 하나라도 찾았으면 더 검사할 필요 없음

#     # 내 앞에 똑같은 애가 없었다면 새 배열에 추가
#     if not is_duplicate:
#         unique_arr.append(arr[i])
