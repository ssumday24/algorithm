# BOJ 15684
# 사다리조작 - G3
# 삼성 2018 기출
# 26.04.22
"""
[문풀 WIL]
1. 순열->조합
백트래킹에서 조합으로 중복 카운팅 줄일수 있는지 항상 생각
- 2차원 배열의 조합문제 복습

2. 깊이별 탐색
문제에서 백트래킹 최대 깊이가 3으로 주어졌으므로 종료 깊이를 0~3 으로 두고 각각 확인해보면 됨. (첫 유형)

3. 양방향 마킹하면 한 row에서 연속으로 가로선을 선택했을때
ex) [1,2] [3,4] 를 마킹시  2와3이 연결x 임에도 연결된 것으로 계산됨
=> 단방향 마킹이 유일한 해결책

4. 문제조건 잘 읽기
연속되는 가로선을 놓지 않으려면,
왼쪽 오른쪽 모두 가로선이 존재하면 안됨


[문제 조건]
i번 세로선의 결과 : i번이 되도록  추가해야하는 가로선 개수의 최솟값=?

"""
import sys
from collections import deque

input = sys.stdin.readline


# 가로선 추가 백트래킹
# 순열 : start 행 부터 시작
def backtr(depth, target_depth, start):
    global result

    # 가지치기 - 정답 찾았으면 조기종료
    if result >= 0:
        return

    # 가로선 타겟깊이만큼 골랐으면 check() 검사
    if target_depth == depth:
        # 문제 조건을 만족하는 경우
        if check():
            result = depth
        return

    # 가로선 선택 : [i][j],[i][j+1] 이 연결됨
    # 중복 카운팅 없게 순열로 변경
    for i in range(start, H + 1):
        for j in range(1, N):  # 마지막 열 N 제외
            # idx 벗어나는경우
            if i > H or j > N:
                continue

            # 이미 선이 있는곳
            # 문제조건 : 연속되는 가로선을 놓지 않으려면,
            # 왼쪽,오른쪽에 가로선이 존재하면 안됨
            if board[i][j] == 1 or board[i][j - 1] == 1 or board[i][j + 1] == 1:
                continue

            # (i,j),(i,j+1) 가로선선택
            board[i][j] = 1

            # 다음깊이 진행
            backtr(depth + 1, target_depth, i)

            # 상태복구
            board[i][j] = 0


# [1,num]에서  출발해서 [H,num]에 도착해야함
def check():
    #  1~N 각 선이 제대로 도착했는지확인
    for num in range(1, N + 1):

        x, y = 1, num  # 시작위치 (1,num)

        while x <= H:
            # 오른쪽 사다리
            if board[x][y] == 1:
                y += 1

            # 왼쪽 사다리 이동
            elif board[x][y - 1] == 1:
                y -= 1

            # 연속한 가로선 없으니  아래로 이동
            x += 1

        # 자기번호와 도착점 다르면 무조건 실패
        if y != num:
            return False

    # 위의 실패처리 안걸렸으면 성공
    return True


### main
# N= 세로선
# M= 선택한 가로선
# H= 각 세로선마다 가로선놓을수 있는 위치의 개수
N, M, H = map(int, input().split())

# 1-indexed  설계
# (H+1)*(N+1)
board = [[0] * (N + 1) for _ in range(H + 1)]

result = -1  #  추가해야 하는 가로선 개수의 최솟값

# 가로선 M개의 정보 (a,b)
# (b,b+1) 세로선을 a번 점선 위치에서 연결
for _ in range(M):
    a, b = map(int, input().split())

    # [a][b],[a][b+1] 가로선 연결
    board[a][b] = 1


# 가로선 추가 : 0개/1개/2개/3개일때 확인
for i in range(4):
    backtr(0, i, 1)

    # 이번 i개에서 찾았으면, 최솟값이니 뒤는 안봐도됨
    if result >= 0:
        break

# 출력
# 못찾았을때 : -1
# 찾았을때: 0,1,2,3
print(result)
