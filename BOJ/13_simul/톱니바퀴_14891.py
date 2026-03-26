# BOJ 톱니바퀴_14891 - G5
# 26.03.25
import sys

input = sys.stdin.readline
from collections import deque

"""
BOJ 톱니바퀴_14891 - G5

1. 배열 shift연산 
- 도착점 역순 순회의 법칙
- 즉 도착지점부터 먼저 채우면서 진행하면 됨 (암기) 

- 뿌요뿌요 문제와 다르게 매초마다 업데이트가 아니라
회전시킬것들만 미리 골라놓고 한번에 업데이트, 훨씬간단 

-BFS가 필요한 곳 (2차원 맵)
- 톱니바퀴 (1차원 선형 맵)


"""
"""
조건 메모
1. a,b 톱니바퀴가 만난 극이 다르면 -> b는 a 반대 방향회전
    => 극이 달라도 a가 회전 안했다면 b도 회전x

2. a,b 극이 같으면 : b는 회전 x
"""


# 바퀴번호 x ,
def rotate(x, dir):
    # 시계방향
    if dir == 1:
        # 1.마지막원소 저장해두기
        tmp = arr[x][7]

        # 2.나머지 당기
        """
        # 중요: 만약 정방향으로 i=1부터 시작하면
        모든 값이 ar[0]으로바뀌니 주의 
        ar[1]=ar[0]
        ar[2]=ar[1]
        ar[3]=ar[2]  
        """

        for i in range(7, 0, -1):
            arr[x][i] = arr[x][i - 1]

        # 3.tmp 시작지점으로
        arr[x][0] = tmp

    # 반시계
    elif dir == -1:
        # 첫원소 저장
        tmp = arr[x][0]

        # 나머지 당기기
        for i in range(0, 7):
            arr[x][i] = arr[x][i + 1]

        # 0번원소는 마지막원소가 되니까 그곳으로 복구
        arr[x][7] = tmp


# 1-index  , 4개톱니바퀴
arr = [[0] * 8]
for _ in range(4):
    row = list(map(int, input().strip()))
    arr.append(row)

K = int(input())  # 회전횟수 k
score = 0  # 점수의 합

for _ in range(K):
    # dir== 1: 시계 / -1: 반시계 / 0 : 멈춤
    start_num, dir = map(int, input().split())

    # 회전할 바퀴들 모아놓을 리스트
    rotate_list = [(start_num, dir)]

    # 왼쪽 바퀴들 탐색
    # 1번바퀴는 왼쪽탐색 못하니 i=2 에서 종료
    temp_dir = dir

    for i in range(start_num, 1, -1):
        # 왼쪽 바퀴와 극이 같으면 그곳부터는 회전X
        if arr[i][6] == arr[i - 1][2]:
            break

        # 방향을 바꾸고, 다음 바퀴에 영향줘야함
        else:
            temp_dir *= -1
            rotate_list.append((i - 1, temp_dir))

    # 오른쪽 쭉 탐색
    temp_dir = dir
    # i=4면 오른쪽 탐색 못하니 i=3 까지만
    for i in range(start_num, 4):
        if arr[i][2] == arr[i + 1][6]:
            break
        else:
            temp_dir *= -1
            rotate_list.append((i + 1, temp_dir))

    # 바퀴 전부 회전
    for x, d in rotate_list:
        rotate(x, d)


# 2.점수계산
for i in range(1, 5):
    # S극: 각 1,2,4,8점
    if arr[i][0] == 1:
        if i == 1:
            score += 1
        elif i == 2:
            score += 2
        elif i == 3:
            score += 4
        elif i == 4:
            score += 8

    # n극: 0점
    else:
        continue

# 결과
print(score)
