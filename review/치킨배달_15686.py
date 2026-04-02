# BOJ 15686
# 치킨배달-G5
# 26.03.05
# 26.04.03 복습
"""
0: 빈칸/1:집 /2:치킨
치킨거리 : 집<->치킨집 거리
도시의 치킨거리 : sum(모든집 치킨거리)

치킨집의 개수: 최대M개 , 나머지 모두 폐업
도시의 치킨거리 최소로 =?

[문풀 노트]
1. 조합 => start부터 보니까 방문체크 필요없음


"""
import sys
from collections import deque

input = sys.stdin.readline


# 도시의 치킨거리 계산
# 리턴값 : 치킨거리
def calc_dist():
    total = 0  # 도시의 치킨거리

    # 각 집마다 치킨거리 계산
    for home_x, home_y in arr_home:
        minval = float("inf")  # 각 집의 치킨거리

        # M개의 치킨집들과 거리비교, 그중 최솟값 구하기
        for chick_x, chick_y in arr_selected:
            dist = abs(home_x - chick_x) + abs(home_y - chick_y)
            minval = min(dist, minval)

        total += minval

    return total


def backtr(depth, start):
    global result

    if depth == M:
        # 도시의 치킨거리 계산후 최솟값이면 업데이트
        result = min(result, calc_dist())

        # 디버깅1
        # print(*board, sep="\n")

        return

    # 치킨집중 하나 고르기
    # 순열로 중복탐색하지 않게 조합으로 시작인덱스 넘기기
    for i in range(start, len(arr_chick)):
        # 조합이니  start부터 탐색하면 중복선택 안함

        # 치킨집 선택
        arr_selected.append(arr_chick[i])

        # 백트래킹 다음깊이
        # i+1 인덱스부터 선택
        backtr(depth + 1, i + 1)

        ## 상태복구
        arr_selected.pop()


# main
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = float("inf")  # m개 골랐을떄 치킨거리의 최솟값

# 치킨집 좌표(i,j)만 모아둔 배열
arr_chick = []

# 집 좌표만 모아둔 배열
arr_home = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            arr_chick.append((i, j))

        elif board[i][j] == 1:
            arr_home.append((i, j))

# 전체 arr_chick 에서 M개만 고른 arr_selected
arr_selected = []


backtr(0, 0)


# 출력
print(result)
