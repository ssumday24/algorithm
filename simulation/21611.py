import sys

input = sys.stdin.readline

# BOJ 21611
# 마법사 상어와 블리자드 - P5
# 삼성 2021 상반기 기출
# 26.04.23
"""
[문풀 WIL]
1. 2D 좌표 -> 1차원 배열 매핑 (달팽이 이동)
   - 나선형으로 도는 좌표들을 미리 1차원 배열의 인덱스(1 ~ N^2-1)로 맵핑해두면,
     블리자드가 2차원 좌표를 타격할 때 어느 1차원 인덱스가 파괴되는지 바로 알 수 있음.

2. 1차원 배열을 통한 시뮬레이션
   - 구슬의 이동: 중간에 구슬이 파괴되어 빈 칸(0)이 생기면, 1차원 리스트에서 
     0을 제외하고 다시 합치는 리스트 컴프리헨션(filter)만으로 이동 로직 완벽 대체 가능.

3. 투 포인터(Two Pointer)를 활용한 그룹화
   - 연속된 구슬의 '폭발'과 '증식(개수, 번호)' 모두 같은 숫자가 몇 개 연속되는지 
     찾는 과정이므로 투 포인터(i, j)를 사용하여 연속된 블록을 묶어서 처리.
"""

# 블리자드 마법 방향: 1(상), 2(하), 3(좌), 4(우)
b_dr = [0, -1, 1, 0, 0]
b_dc = [0, 0, 0, -1, 1]

# 달팽이 방향: 좌(0), 하(1), 우(2), 상(3)
s_dr = [0, 1, 0, -1]
s_dc = [-1, 0, 1, 0]


def get_snail_mapping(N):
    board_to_idx = [[0] * N for _ in range(N)]
    r, c = N // 2, N // 2
    idx = 1
    d = 0

    # 1, 1, 2, 2, 3, 3 ... N-1, N-1 길이만큼 이동
    for length in range(1, N):
        for _ in range(2):
            for _ in range(length):
                r += s_dr[d]
                c += s_dc[d]
                board_to_idx[r][c] = idx
                idx += 1
            d = (d + 1) % 4

    # 마지막 줄은 N-1 번 한 번 더 이동
    for _ in range(N - 1):
        r += s_dr[d]
        c += s_dc[d]
        board_to_idx[r][c] = idx
        idx += 1

    return board_to_idx


def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 1. 2D 맵을 1D 배열 매핑 인덱스로 변환
    board_to_idx = get_snail_mapping(N)

    # 2. 초기 구슬들을 순서대로 1차원 리스트에 담기
    idx_to_val = [0] * (N * N)
    for r in range(N):
        for c in range(N):
            if board_to_idx[r][c] > 0 and board[r][c] > 0:
                idx_to_val[board_to_idx[r][c]] = board[r][c]

    marbles = [idx_to_val[i] for i in range(1, N * N) if idx_to_val[i] > 0]

    ans = 0  # 폭발한 구슬 점수 합

    # M번의 블리자드 마법 시전
    for _ in range(M):
        d, s = map(int, input().split())

        # [단계 1] 블리자드 마법 (파괴)
        curr_r, curr_c = N // 2, N // 2
        for _ in range(s):
            curr_r += b_dr[d]
            curr_c += b_dc[d]
            target_idx = board_to_idx[curr_r][curr_c]

            # 파괴 타겟이 현재 남은 구슬 리스트 길이 안쪽일 경우 파괴(0으로 표기)
            if target_idx - 1 < len(marbles):
                marbles[target_idx - 1] = 0

        # 파괴된 구슬(0) 제거하여 당기기
        marbles = [m for m in marbles if m > 0]

        # [단계 2] 구슬 폭발
        while True:
            exploded = False
            next_marbles = []
            i = 0
            while i < len(marbles):
                j = i
                # 연속된 같은 구슬 찾기
                while j < len(marbles) and marbles[j] == marbles[i]:
                    j += 1

                # 4개 이상 연속 시 폭발
                if j - i >= 4:
                    ans += marbles[i] * (j - i)  # 점수 = 구슬번호 * 터진개수
                    exploded = True
                else:
                    # 폭발하지 않으면 그대로 다음 리스트에 저장
                    next_marbles.extend(marbles[i:j])
                i = j

            marbles = next_marbles
            if not exploded:
                break

        # [단계 3] 구슬 변화 (그룹화)
        if len(marbles) == 0:
            break

        next_marbles = []
        i = 0
        while i < len(marbles):
            j = i
            while j < len(marbles) and marbles[j] == marbles[i]:
                j += 1

            next_marbles.append(j - i)  # A: 연속된 구슬의 개수
            next_marbles.append(marbles[i])  # B: 구슬의 번호
            i = j

        # 격자 크기(N*N - 1)를 넘어가면 잘라내기
        marbles = next_marbles[: N * N - 1]

    print(ans)


solve()
