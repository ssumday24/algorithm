# BOJ 14889
# 스타트와 링크
# 26.04.04
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


def calc():
    # 팀1=[1,2] / 팀2:[3,4]
    sum_1 = 0  # 1팀
    sum_2 = 0  # 2팀

    # 능력치 계산
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # i,j 모두 팀1일때
            if visited[i] and visited[j]:
                sum_1 += board[i][j]
            # 팀2일때
            if not visited[i] and not visited[j]:
                sum_2 += board[i][j]

    # 능력치 차이 리턴
    return abs(sum_1 - sum_2)


def backtr(depth, start):
    global result

    # 절반 선택하면 종료
    if depth == (N // 2):
        # 팀간 능력치 차이계산
        # 최솟값이면 업데이트
        result = min(result, calc())

        return

    # start~N 중에서 선택하기
    for i in range(start, N + 1):
        # 조합-> 방문체크 필요없지만
        # team2 만들때 vis 사용해서 O(1)
        team_1.append(i)
        visited[i] = True

        # 다음수 선택
        # i+1번부터 선택
        backtr(depth + 1, i + 1)

        # 상태복구
        team_1.pop()
        visited[i] = False


N = int(input())
# N+1*N+1
# 1-indexed
board = [[0] * (N + 1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))


result = float("inf")  # 구하는값 : 능력치 차이 최솟값

# 방문체크 1~N idx 사용
visited = [0] * (N + 1)

# 선택된 수 저장배열
team_1 = []

backtr(0, 1)


# 출력
print(result)
