# BOJ 12865
# 평범한배낭  - G5
# 26.03.13
"""
[WIL]
- 첫 배낭문제(KnapSack) 알고리즘

1.하위값->상위값 활용가능?
2.이전선택에 따라 현재선택지가 줄어드는가?->O->2차원
3.dp[i][j]= i번째 물건까지 고려했을때, 가방한도가 j일때 얻는 최대가치

(N+1)*(K+1), 1-indexed로 설계

시간복잡도: N*K = 최대 100*100,000= 10^7
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

# i:1~N,
for i in range(1, N + 1):
    # (무게,가치)
    W, V = map(int, input().split())

    # dp테이블 채우기 ,  j:1~K
    for j in range(1, K + 1):

        # j-W <0 이되면 어떻게처리?
        # i번째 물건은 절대 못넣음
        # 즉, 과거의 가방상태 그대로 물려받아야함
        if j - W < 0:
            dp[i][j] = dp[i - 1][j]

        else:
            # i번째 물건을 넣지x 와 넣었을때 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)


# 출력
# N번째 물건까지 담았을때, 가방한도=K 일때 가치의 최댓값
print(dp[N][K])
