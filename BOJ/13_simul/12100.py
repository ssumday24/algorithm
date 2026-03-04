# BOJ 12100
# 2048(EASY) - G1
# 26.03.04
"""
# [WIL]
# 1. 백트래킹에서 상태복구가 힘들때 : 복사배열 (감시문제와 같음)
# 2. 파이썬 for i in range()는 루프 안에서 i 값을 바꿔도 다음 바퀴에 초기화 (i 2칸씩건너뛰기 불가)
# 2-1. 인덱스를 내 맘대로 점프 : for문 말고 while i < len(row) 사용
# 3.문제 핵심: 빈칸(0)이 섞인 배열 이동은 데이터만 추출해서 리스트로 처리

-N*N 보드, 최대5번이동으로 만드는 가장큰 값
- 5번 이동전에는 결과를 알수없으니 백트래킹+브루트포스?
"""
import sys

input = sys.stdin.readline


# 배열,방향 -> 한쪽벽으로 쭉밀기
# return : 변경된 배열
# TODO : 함수 완성
# TODO : 왼쪽 완성후 다른방향도 완성
def push(arr, dir):
    # 1. 0이아닌 원소들만 temp에 모으기
    temp = []
    for row in arr:
        temp_row = []

        for elem in row:
            if elem != 0:
                temp_row.append(elem)

        temp.append(temp_row)

    # 2.양쪽수 비교 - 각 row마다 진행
    # temp는 각행별로 0이아닌값만 모아놓은 2차원 배열
    new_arr = []
    for row in temp:
        new_row = []
        for i in range(len(row)):
            # 맨끝값은 볼필요없음
            if i == len(row) - 1:
                # 맨끝값 append
                new_row.append(row[i])

                break

            else:
                if row[i] == row[i + 1]:
                    # 합친값을 new_row 에 저장
                    new_row.append(row[i] + row[i + 1])

                ###TODO: i= i+2 하면 어떻게 동작?

        # 3. 0으로 채우기
        new_row += [0] * (N - len(new_row))

        new_arr.append(new_row)


# 백트래킹 함수
def backtr(depth, arr):
    global result  # 함수밖 변수값 수정

    # 5번 이동후
    if depth == 5:
        for row in arr:
            for elem in row:
                result = max(result, elem)
        return

    # 0:상->1:우->2:하->3:좌 , 시계방향
    for dir in range(4):
        # TODO: 원본배열 복사-> 벽으로 밀기
        # 참고: 15683 - 감시
        copy = [row[:] for row in arr]

        # 백트래킹 다음깊이
        backtr(depth + 1, push(copy, dir))

        # 원본배열 안건드렸으니 상태회복x


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
# 구하는값
print(result)
