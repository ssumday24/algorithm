import sys

input = sys.stdin.readline

# BOJ 23291 - 어항 정리
# [문풀 WIL]
# 1. 90도 회전: (r, c) -> (c, H-1-r) 공식을 정확히 적용해야 함
# 2. 어항 조절(adjust) 시 '동시'에 변해야 하므로 변화량(delta) 배열 사용 필수
# 3. 180도 접기는 2번 수행하며, N/2, N/4 단위로 인덱스 슬라이싱 주의


def adjust_fish(board):
    R = len(board)
    C = len(board[0])
    delta = [[0] * C for _ in range(R)]
    dr = [0, 1]
    dc = [1, 0]

    for r in range(R):
        for c in range(C):
            if board[r][c] == -1:
                continue
            for i in range(2):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                    diff = abs(board[r][c] - board[nr][nc]) // 5
                    if diff > 0:
                        if board[r][c] > board[nr][nc]:
                            delta[r][c] -= diff
                            delta[nr][nc] += diff
                        else:
                            delta[r][c] += diff
                            delta[nr][nc] -= diff
    for r in range(R):
        for c in range(C):
            if board[r][c] != -1:
                board[r][c] += delta[r][c]
    return board


def flatten(board):
    new_arr = []
    R = len(board)
    C = len(board[0])
    for j in range(C):
        for i in range(R - 1, -1, -1):
            if board[i][j] != -1:
                new_arr.append(board[i][j])
    return new_arr


def solve():
    N, K = map(int, input().split())
    fish = list(map(int, input().split()))

    count = 0
    while True:
        # 종료 조건: 최댓값과 최솟값의 차이가 K 이하
        if max(fish) - min(fish) <= K:
            print(count)
            break

        count += 1

        # 1. 물고기 추가
        min_v = min(fish)
        for i in range(N):
            if fish[i] == min_v:
                fish[i] += 1

        # 2. 어항 쌓기 (90도 회전)
        # 초기: 가장 왼쪽 어항을 두 번째 어항 위에 올림
        board = [[fish[0]], [fish[1]]]
        remain = fish[2:]

        while True:
            h = len(board)
            w = len(board[0])
            if h > len(remain):
                break

            # 현재 board를 90도 시계방향 회전
            rotated = [[0] * h for _ in range(w)]
            for i in range(h):
                for j in range(w):
                    rotated[j][h - 1 - i] = board[i][j]

            # 회전된 board를 남은 어항(remain) 위에 쌓기
            new_board = [row for row in rotated]
            new_board.append(remain[:h])  # 바닥층 추가
            board = new_board
            remain = remain[h:]

        # 남은 평평한 어항들을 board의 바닥층 오른쪽에 붙여줌 (직사각형 유지 위해 -1 패딩)
        max_w = max(len(row) for row in board)
        if len(remain) > 0:
            for i in range(len(board)):
                if i == len(board) - 1:
                    board[i] = board[i] + remain
                else:
                    # 위층들은 -1로 채움
                    board[i] = board[i] + [-1] * len(remain)

        # 3. 물고기 조절 -> 4. 평면화
        fish = flatten(adjust_fish(board))

        # 5. 어항 접기 (180도)
        # 1차 접기
        n = len(fish)
        row1 = fish[: n // 2][::-1]
        row2 = fish[n // 2 :]
        board_180 = [row1, row2]

        # 2차 접기
        w_180 = n // 4
        final_board = []
        # 위 2줄의 왼쪽 절반을 180도 회전해서 쌓음
        top_part = []
        for i in range(1, -1, -1):
            top_part.append(board_180[i][:w_180][::-1])
        # 아래 2줄 (남은 오른쪽 절반)
        bottom_part = []
        for i in range(2):
            bottom_part.append(board_180[i][w_180:])

        board_final = top_part + bottom_part

        # 6. 물고기 조절 -> 7. 평면화
        fish = flatten(adjust_fish(board_final))


solve()
