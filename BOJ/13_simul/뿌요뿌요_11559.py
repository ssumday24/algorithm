# BOJ 11559 뿌요뿌요 - G4
# 26.03.25
import sys

input = sys.stdin.readline
from collections import deque

"""
[BOJ 11559 뿌요뿌요 - G4]
1. 어떻게 4개로 이어진곳을 추적해서 지우지? 추적용 큐 만들수밖에없는데

2.터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 
- 이러면 모든지점 bfs 끝난 이후에  끌어내리기.
- 연쇄가 없을때 종료

3. 중력 아이디어 ###################
- 배열을 새로만들지 말고, 제자리 덮어쓰기로 구현
- 2048(EASY) 문제와 비교 

"""
"""
조건 메모
r1. 바닥 or 다른 뿌요나올때까지 떨어짐 
r2. 같은 색 뿌요가 4개 "이상" 상하좌우로 연결 -> 1연쇄
r3. 동시에 여러그룹 터짐 가능 -> 1연쇄
"""


def bfs(i, j, c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS전용 큐
    q = deque()

    # 연결된 부분 기억할 큐
    con_q = deque()

    # 색깔이 있는곳 골랐으면 큐에넣고 bfs시작
    q.append((i, j, c))
    visited[i][j] = 1

    # 몇개 연결되어있는지 , 출발점 1로 시작
    cnt = 1
    con_q.append((i, j))

    while q:
        cur_x, cur_y, cur_color = q.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            # 인덱스OOR 체크
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue

            if visited[nx][ny]:
                continue

            # 인접한색이 같을때만
            if arr[nx][ny] == cur_color:
                visited[nx][ny] = 1
                q.append((nx, ny, cur_color))

                # 연결된 영역도 넣기, 좌표만 알면됨
                con_q.append((nx, ny))

                # 연결영역 +1
                cnt += 1

    # 4개이상 연결됐을때 폭발
    if cnt >= 4:

        # 폭발후 빈칸으로 변경
        while con_q:
            cur_x, cur_y = con_q.popleft()
            arr[cur_x][cur_y] = "."

        return True

    # 3개이하 폭발x
    else:
        return False


###### 중력 아이디어 #######
# 임시배열+ 제자리 덮어쓰기로 구현
# 떨어지는 상황은 무조건 아래가 빈칸('.')
def push_down(arr):
    # 각 세로줄 마다
    for j in range(C):
        temp = deque()

        # 맨아래줄 -> 첫줄 순회
        for i in range(R - 1, -1, -1):
            if arr[i][j] != ".":
                temp.append(arr[i][j])

        # 맨 밑부터 채워넣기
        for i in range(R-1, -1, -1):

            # 뿌요가 남아있을때
            if temp:
                # 혹은 temp=[] 이후 temp.pop(0)
                arr[i][j] = temp.popleft()

            # 뿌요 다썼으면 빈칸으로 채우기
            else:
                arr[i][j] = "."


# main
R, C = 12, 6
arr = [list(input().strip()) for _ in range(R)]
total = 0  # 연속연쇄값

# 폭발이 동시에 터져야하니
# 모든지점에서 bfs 한 이후가 1초.
while True:
    # 각 초마다 위치가 갱신되니, vis 초기화
    visited = [[False] * 6 for _ in range(12)]

    # 각 초마다 폭발 여부
    explode = False

    # 각 초마다 폭발 있었는지 체크
    flag = False

    for i in range(R):
        for j in range(C):

            if arr[i][j] == ".":
                continue

            if visited[i][j]:
                continue

            # bfs , 폭발여부 계산
            explode = bfs(i, j, arr[i][j])

            # 현재지점에서 폭발못하면 다음 좌표 탐색
            if not explode:
                continue

            # 폭발있었으면 플래그
            if explode:
                flag = True

    # 모든 지점 BFS+폭발 끝나고 난후, 맨아래로 끌어내리기
    push_down(arr)

    # 이번 초에 폭발없으면 종료
    if not flag:
        break

    # 각시행 (초로 생각) 마다 폭발횟수 추가
    # 동시에 여러개 폭발해도 1회.
    total += 1

# 결과: 연쇄가 몇번 일어나고 종료?
print(total)
