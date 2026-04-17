# N으로 표현
# DP - LV3
# 26.04.16

"""
n과 사칙연산만 사용해서,number을 만들때 n 사용횟수의 최솟값=?
r1.나머지는무시
r2.최솟값이 8보다 크면 -1  return

dp[i]= N을 i번써서 숫자를 만들때, 만들수있는 수의 집합
dp[1]={N}
dp[2]={NN,}
"""


def solution(N, number):
    # 예외처리) N=number일떄
    if N == number:
        return 1

    # dp[8]까지만 필요
    dp = [set() for _ in range(9)]

    # 초기값
    # N,NN,NNN 수는 사칙연산으로 만들수 없으니
    # 초기값으로 세팅
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN, NNN, ...

    # 점화식
    # 집합 dp[2]~dp[8] 구하기
    for i in range(2, 9):
        # dp[i]에 대해 , 왼쪽집합 / 오른쪽집합 고르기
        # 왼쪽: dp[a] / 오른쪽:dp[i-a]
        for a in range(1, i):
            for num1 in dp[a]:
                for num2 in dp[i - a]:
                    # num1, num2의 사칙연산으로 가능한 수
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)

                    # 0나누기 방지
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        # dp[i]를 다구했으면, number이 있는지 검사
        # 바텀업이니 처음 찾는 i가 정답
        if number in dp[i]:
            return i

    # dp[8]안에 표현못하면 -1 리턴
    return -1


#####
# 5로 12를 만들떄 필요한 5의개수의 최솟값
# 12= (55+5)/5  -> 4개
print(solution(5, 12))
print(solution(2, 11))
