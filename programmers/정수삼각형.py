# 정수 삼각형
# 26.04.16
# DP
# 동일문제: BOJ #1932


# 입력배열 : 0-indexed
def solution(triangle):
    """
    dp[i][j]: 인덱스 i번째 숫 자까지 골랐을때, 합의 최댓값
    단, 마지막줄에 고른숫자는 arr[i][j]
    """
    N = len(triangle)  # 한변의 길이
    dp = [[0] * N for _ in range(N)]  # N*N

    # 초기값 세팅
    dp[0][0] = triangle[0][0]

    # 1행부터 계산
    for i in range(1, N):
        # 열의개수 = i , 따라서 i번 반복
        for j in range(i + 1):
            # 1. 맨왼쪽값: 1가지
            if j == 0:
                dp[i][0] = dp[i - 1][0] + triangle[i][0]

            # 2. 맨오른쪽: 1가지
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

            # 3.그외 일반케이스
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    answer = max(dp[N - 1])  # 마지막 행의 최댓값
    return answer


####
# x = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# print(solution(x))
