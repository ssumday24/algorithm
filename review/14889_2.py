# BOJ 14889
# 스타트와 링크
# 26.04.04
# 26.04.15 - 25분
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


def func(depth, start):
    global result

    if depth == (N // 2):
        # 1.점수차 계산
        # 선택된 수 i에대해, 전부 used[i]=true
        score_1 = 0
        score_2 = 0

        for i in range(1, N + 1):
            # 팀1
            if used[i]:
                # j=1 부터 비교, i=j 여도 0점이니 예외처리필요x
                for j in range(1, N + 1):
                    if used[j]:
                        score_1 += board[i][j]

            # 팀2
            else:
                for j in range(1, N + 1):
                    if not used[j]:
                        score_2 += board[i][j]

        temp = abs(score_2 - score_1)

        # 2. 최솟값이면 업데이트
        result = min(temp, result)

        # 조기종료
        if result == 0:
            print(0)
            sys.exit()

        return

    # 1~N 중 고르기
    # 조합이니 start부터 시작
    for i in range(start, N + 1):
        if not used[i]:
            used[i] = True
            # arr.append(i)

            # 다음깊이
            func(depth + 1, i + 1)

            # 상태복구
            used[i] = False
            # arr.pop()


# 1-indexed, n+1 * n+1 설계
N = int(input())
board = [[0] * (N + 1)]
board += [[0] + list(map(int, input().split())) for _ in range(N)]
used = [False] * (N + 1)  # 1~N 인덱스만 사용
result = float("inf")  # 능력치 차이

# arr = []  # 고른팀 담을배열

# 백트래킹으로 절반 고르기
# start=1 시작
func(0, 1)

# 결과 출력
print(result)


# print(*board, sep="\n")
