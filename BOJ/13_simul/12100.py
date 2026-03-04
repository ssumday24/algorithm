# BOJ 12100
# 2048(EASY) - G1
# 26.03.04
"""
# [WIL]
# 1. 백트래킹에서 상태복구가 힘들때 : 복사배열
    - (BOJ 15683-감시 문제와 같음)
# 2. 파이썬 for i in range()는 루프 안에서 i 값을 바꿔도 다음 바퀴에 초기화 (i 2칸씩 건너뛰기 불가)
# 2-1. 인덱스를 내 맘대로 점프 : for문 말고 while i < len(row) 사용
# 3.문제 핵심: 빈칸(0)이 섞인 배열 이동은 데이터만 추출해서 리스트로 처리

-N*N 보드, 최대5번이동으로 만드는 가장큰 값
- 5번 이동전에는 결과를 알수없으니 백트래킹+브루트포스?
"""
import sys

input = sys.stdin.readline


# 배열-> 왼쪽벽으로 쭉밀기
def push(arr):
    # 1. 0이아닌 원소들만 2차원 리스트 temp에 모으기
    # temp_row= [elem for elem in row if elem!=0] 이므로
    temp = [[elem for elem in row if elem != 0] for row in arr]

    # 2.temp에서 붙어있는 두 수 비교
    new_arr = []
    for row in temp:
        new_row = []
        idx = 0

        """
        row -> new_row 
        [2,2,2,2]->[4,4] 
        [2,2,8]->[4,8]
        
        """
        while idx < len(row):
            # 값이 같으면 합치기
            # 주의 : 맨끝일떄 idx+1 인덱스에러
            if idx != len(row) - 1 and row[idx] == row[idx + 1]:

                new_row.append(row[idx] + row[idx + 1])

                # 이제 두수는 볼필요 없으니 idx 2증가
                idx += 2
                continue

            # 값이 다르거나, 맨끝 값이면 원본그대로
            else:
                new_row.append(row[idx])
                idx += 1

        # 3. 나머지 0으로 채우기
        """
        new_row:[4,4]->new_row:[4,4,0,0] 만들기
        """
        for _ in range(N - len(new_row)):
            new_row.append(0)

        # 새로만든 row들 추가
        new_arr.append(new_row)

    # 변경된 배열 반환
    return new_arr


# 시계방향 90도 회전함수
def rotate(arr):
    # R*C -> C*R 변환
    new_arr = [row[:] for row in arr]
    R = len(arr)
    C = len(arr[0])

    for i in range(R):
        for j in range(C):
            # 원본의 j -> 회전후 행 값으로
            # 원본의 i -> -i + (R-1)
            new_arr[j][-i + (R - 1)] = arr[i][j]

    return new_arr


# 백트래킹 함수
def backtr(depth, arr):
    global result  # 함수밖 변수값 수정

    # 5번 이동후
    if depth == 5:
        # result = max(result,max(max(row) for row in arr))
        # max의 인자로 리스트,튜플,map 전부가능.
        for row in arr:
            for elem in row:
                result = max(result, elem)
        return

    # 방법2)
    """
    iter1: rotate(arr)->push : 아래로밀기
    iter2: 180도회전->push : 오른쪽으로밀기
    iter3: 270도회전->push : 아래서 위로밀기
    tier4: 360도회전->push: 왼쪽으로밀기
    
    copy= [row[:] for row in arr]
    
    for _ in range(4):
        copy=rotate(copy)
        backtr(depth+1,push(copy))
    """

    # 방법1) 0:왼->1:위->2:오->3:아 , 시계방향
    for dir in range(4):
        copy = [row[:] for row in arr]

        # 왼쪽으로 밀기
        if dir == 0:
            backtr(depth + 1, push(copy))

        # 위쪽으로 밀기
        elif dir == 1:
            # 270도 회전
            for _ in range(3):
                copy = rotate(copy)

            # 왼쪽으로밀기
            copy = push(copy)

            # 90도회전
            copy = rotate(copy)

            # 여기선 인자로 copy만
            backtr(depth + 1, copy)

        # 오른쪽으로 밀기
        elif dir == 2:
            # 180도 회전
            for _ in range(2):
                copy = rotate(copy)

            # 왼쪽으로밀기
            copy = push(copy)

            # 180도 회전
            for _ in range(2):
                copy = rotate(copy)

            backtr(depth + 1, copy)

        # 아래쪽으로 밀기
        elif dir == 3:
            # 90도 회전
            copy = rotate(copy)

            # 왼쪽으로밀기
            copy = push(copy)

            # 270도 회전
            for _ in range(3):
                copy = rotate(copy)

            backtr(depth + 1, copy)

        # 원본배열(arr) 안건드렸으니 상태회복x


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
backtr(0, board)  # depth=0 시작
print(result)
