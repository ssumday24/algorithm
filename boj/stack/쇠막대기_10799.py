# 10799:쇠막대기
# 26.03.28
"""
- pop()전에 항상 스택 비었는지 확인
if stack:
    stack.pop()
else:
"""

import sys
from collections import deque

input = sys.stdin.readline

arr = list(input().strip())
stack = []
result = 0  # 잘려진 막대개수

# 스택에 넣을값 x
for x in range(len(arr)):
    # 왼쪽괄호- 레이저 or 막대 시작점
    if arr[x] == "(":
        stack.append(arr[x])

    # 오른쪽 괄호
    else:
        # 레이저 ()
        if arr[x - 1] == "(":
            stack.pop()
            # 배열의 길이 == 왼쪽 괄호 갯수
            result += len(stack)

        # 나무막대끝, ) )
        else:
            stack.pop()
            result += 1

# 출력
print(result)
