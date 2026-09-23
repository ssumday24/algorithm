# BOJ 18808
# 스티커붙이기 - G3
# 26.03.03
# 26.03.19
"""
[WIL] 03.19
1.이 문제는 스티커를 한번 붙이면 다시 떼지 않기때문에 경우의 수를 전부
탐색하는 백트래킹이 아님 -> 그리디 시뮬

2. "함수 분리(모듈화)"와 "Early Return"
 검사 로직을 별도의 함수로 빼면됨
 (함수는 return으로 즉시 종료하니 flag도 필요없어지므로)

3. 배열회전시 R*C 가 뒤바뀌니 함수 안에서 다시계산

4. 슬라이딩 윈도우?
for i in range(N - R + 1):
        for j in range(M - C + 1):

-다중반복문 conti/break
"""
import sys

input = sys.stdin.readline


# 미리보고 붙일수있는지 판단
def attachable(i, j, R, C):
    for x in range(R):
        for y in range(C):

            # 이미 다른스티커가 붙어있을때
            if arr[i + x][j + y] == 1 and stick[x][y] == 1:
                return False

    # 붙일수있음
    return True


# (0,0)~(N-1,M-1) 모든칸에 대해 스티커 붙이기 시도
def attach():
    R = len(stick)
    C = len(stick[0])

    # board[i][j] 칸부터 스티커를 대보면됨
    # idx i : 0~ N-R , j: 0~(M-C)
    for i in range(N - R + 1):
        for j in range(M - C + 1):

            # 미리보고 붙일수있는지 판단
            if not attachable(i, j, R, C):
                continue

            # 위에서 안걸러졌으면 붙이기
            for x in range(R):
                for y in range(C):
                    if arr[i + x][j + y] == 0 and stick[x][y] == 1:
                        arr[i + x][j + y] = 1

            # 붙이기 성공
            return True

    # 모든칸 조사했지만 붙이기 실패
    return False


# 스티커 배열회전 -시계방향 90도
def rotate(arr):
    R = len(arr)
    C = len(arr[0])

    # R*C -> C*R 새로운 배열
    new_arr = [[0] * R for _ in range(C)]

    # 기존 (x,y)-> 회전후 (y,-x+R-1)
    for x in range(R):
        for y in range(C):
            new_arr[y][-x + R - 1] = arr[x][y]

    return new_arr


# N*M , K개 스티커 : R*C
N, M, K = map(int, input().split())

# 노트북: N*M
arr = [[0] * M for _ in range(N)]

# 스티커 K개
for _ in range(K):
    R, C = map(int, input().split())

    # R*C 스티커
    stick = [list(map(int, input().split())) for _ in range(R)]

    # 0-90-180-270 중 한 각도 정하기
    for _ in range(4):
        # (0,0)~(N-1,M-1) 모든칸에 대해 스티커 붙이기 시도
        success = attach()

        # 성공 -> 다음 스티커로 넘어가기
        if success:
            break

        # 실패시 90도 회전후 다음각도로 시도
        if not success:
            stick = rotate(stick)

    # 이번 스티커로 못붙이면 다음스티커로 넘어가기


# 최종결과 계산
result = 0

for row in arr:
    for elem in row:
        if elem == 1:
            result += 1

print(result)
