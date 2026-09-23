# 등굣길
# DP - LV3
# 26.04.16 - 20분
"""
1. 1-idxed 설계
- 왼쪽,위쪽 전부 제로 패딩 있으니 1행,1,열 모두 안전

2. 리스트로 웅덩이 순회하면 O(N) 이지만
집합(해시테이블)으로 순회시 O(1)

"""


def solution(M, N, puddles):
    # puddles : 물이 잠긴 지역의 좌표를 담은 2차원 배열
    # 물을 피해서 갈수있는 최단경로의 수=?

    # 1-indexed, (N+1)*(M+1)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # 초기값
    dp[1][1] = 1

    # 웅덩이 집합
    puddle_set = set()
    for y, x in puddles:
        puddle_set.add((x, y))

    # 점화식
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # 시작점은 제외
            if i == 1 and j == 1:
                continue

            # 왼쪽, 위쪽 경로 합산
            # 왼쪽,위쪽 전부 제로 패딩 있으니 1행,1,열 모두 안전
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007

            # 웅덩이 자리인경우, 무조건 0으로 수정
            if (i, j) in puddle_set:
                dp[i][j] = 0

    # print(*dp, sep="\n")

    answer = dp[N][M]
    return answer


# M=4,N=3 리턴:4
res = solution(4, 3, [[2, 2]])
print(res)
