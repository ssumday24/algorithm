# BOJ 15686
# 치킨배달-G5
# 26.03.05
"""
[WIL]
1. 특정 idx pop  
x = arr.pop(idx)

2. 인덱스를 돌면서 pop()을 해버리면 절대 안됨 
=>인덱스에러 발생
arr = ['A', 'B', 'C']
for i in range(3):
    arr.pop(i)

3. 백트래킹
X개 -> M개로 줄여가기와
0개 -> M개로 늘려가기는 같으므로 (조합)
기존의 append 방식 쓰면되네

4. 순열,조합
이문제의 치킨집은 같은것을 중복으로 고를수 없으니
순열이 아닌 조합 
=> visited 필요없이, 인자로 i+1 넘겨주기

순열로 풀이->시간초과
조합으로 수정 -> 정답

=> 이전 백트래킹 어떻게 썼는지 복습 
boj 12100 (2048) : 중복순열
boj 15683(감시CCTV) : 독립시행(순차선택)
"""
import sys

input = sys.stdin.readline


# 치킨거리 계산: 가장 가까운 치킨집
# home:튜플 ,arr:튜플 list
def calc_dist(home, arr):

    home_x, home_y = home

    # 초기값 :999999
    min_dist = 999999

    for arr_x, arr_y in arr:
        if abs(home_x - arr_x) + abs(home_y - arr_y) < min_dist:
            min_dist = abs(home_x - arr_x) + abs(home_y - arr_y)

    return min_dist


# 백트래킹, 조합
# start : 탐색시작 idx
def backtr(depth,start):
    global min_dist, best_arr

    # 깊이: 0 -> M , 최종선택한 arr 완성
    if depth == M:

        # 도시 치킨 거리가 최소가 되어야함
        cnt = 0
        for home in arr_home:
            cnt += calc_dist(home, arr)

        if cnt < min_dist:
            min_dist = cnt

            # # 디버깅용 - 살려야할 치킨집 좌표 출력
            # best_arr = arr[:]

        # 리턴
        return

    # arr_chick중 1개 고르기
    for i in range(start,len(arr_chick)):
      
        # new_arr에 선택
        x, y = arr_chick[i]
        arr.append((x, y))

        # 다음깊이 진행
        backtr(depth + 1,i+1)

        # 상태복구
        arr.pop()
      


N, M = map(int, input().split())
# 도시정보 N*N
board = [list(map(int, input().split())) for _ in range(N)]


# 치킨집,가정집 좌표(x,y) 저장
arr_home = []
arr_chick = []
result = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            arr_home.append((i, j))

        elif board[i][j] == 2:
            arr_chick.append((i, j))

# 폐업 필요X
if len(arr_chick) <= M:

    for home in arr_home:
        # 각집마다 치킨거리 계산
        result += calc_dist(home, arr_chick)

    print(result)

# 폐업 필요
else:
    # 선택한 치킨집 담을 arr
    arr = []
    min_dist = 999999

    #깊이:0, start:0 
    backtr(0,0)

    print(min_dist)

    # # 디버깅용
    # print("살려야 할 치킨집 좌표:", best_arr)
