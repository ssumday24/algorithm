# 3*n 타일링
# 26.04.16
# DP
# 백준 2133.타일채우기-G4 동일문제


def solution(n):
    answer = 0
    dp = [0] * (n + 1)  # idx:1~n 사용

    # 1.테이블정의
    # dp[i]: 가로의 길이가 i일때, 직사각형들로 채우는 경우의 수

    # 2.초기값 세팅,예외처리

    # n=0, n=1 이면 0리턴
    if n < 2:
        return 0

    # 초기값
    dp[0] = 1  # 0이아닌 1로설정해야 2 더해짐
    dp[2] = 3

    # 3.점화식
    """
    dp[i]=dp[i-2]*3 + dp[i-4]*2+ dp[i-6]*2 + ..... dp[0]*2
    
    """
    for i in range(3, n + 1):
        # 홀수면 절대 만들기 불가
        if i % 2 == 1:
            continue

        dp[i] = dp[i - 2] * 3

        # i-4 부터시작
        num = i - 4
        while num >= 0:
            dp[i] += dp[num] * 2
            # 2씩 감소
            num -= 2

            # 문제조건
            dp[i] = dp[i] % 1000000007

    answer = dp[n]

    return answer
