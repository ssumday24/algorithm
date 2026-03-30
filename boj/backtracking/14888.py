# 연산자 끼워넣기_14888
# 26.03.30
"""
- A형 기출

[규칙]
r1. 계산은 연산자 우선순위 무시하고 앞에서부터 차례로
r2. 나눗셈은 정수 나눗셈으로 몫만
r3. 음수 나누기 양수 :  양수로 바꾸고 나눈 몫을 음수로 바꾸기

[문풀WIL]
1. 몫 나눗셈은 나머지 버리기떄문에 역연산으로 원본숫자 복구불가

2. 상태 복구 아이디어
백트래킹(DFS)에서 현재 깊이의 상태값(total)을 직접 변경하지않고 계산된 '결과값' 자체를 다음 함수의 인자로 넘기기.
이를 통해 TOTAL값 상태 복구(역연산) 필요없어짐
"""

import sys
from collections import deque


"""
깊이0 : ar[0]
깊이1:ar[0],ar[1]
즉 깊이 만큼 ar[k]까지 연산진행
"""

# 시작점 : depth=1, total=arr[0]
def backtr(depth, total):
    global maxval, minval

    # 숫자 N개를 전부고르면 종료
    if depth == N:
        # 최댓값 갱신
        maxval = max(total, maxval)

        # 최솟값 갱신
        minval = min(total, minval)

    # 4가지 연산자 oper[0]~oper[3] 중 고르기
    for i in range(4):
        # 값이0 : 다 쓰면 못고름
        if oper[i] == 0:
            continue

        # 연산자 고르기
        oper[i] -= 1  # 남은갯수 -1

        # 더하기
        if i == 0:
            backtr(depth + 1, total + arr[depth])
        # 뺴기
        elif i == 1:
            backtr(depth + 1, total - arr[depth])
        # 곱하기
        elif i == 2:
            backtr(depth + 1, total * arr[depth])
        # 나누기
        elif i == 3:
            # 음수 // 양수 :  양수로 바꾸고 나눈 몫을 음수로 바꾸기
            if total < 0:
                temp = total * (-1) // arr[depth] * (-1)
                backtr(depth + 1, temp)
            else:
                backtr(depth + 1, total // arr[depth])

        # 상태복구
        oper[i] += 1

        # total 값은 복구필요X


input = sys.stdin.readline
N = int(input())

# [a1,a2,....an]
arr = list(map(int, input().split()))

# +/-/x/나눗셈 갯수 , 총n-1개
oper = list(map(int, input().split()))

# 최댓값,최솟값
maxval = (-1) * float("inf")  # 음수값 가능하니 마이너스 무한대로 ####
minval = float("inf")

# 수의 합 total=arr[0] 시작
backtr(1, arr[0])


# 결과출력
print(maxval)
print(minval)
