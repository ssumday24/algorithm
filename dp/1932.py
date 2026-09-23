# BOJ 1932
# 정수 삼각형-S1
# 26.03.16
import sys

input = sys.stdin.readline
"""
[WIL]
- 경로추적 
- 백트래킹-> 2^500 , 시간초과
- dp 시간복잡도 계산: 1+2+...N= N^2

dp[i][j]: i번째row 까지 골랐을떄 합이 최대일때, 선택한 수들의합.
단 마지막에 고른 숫자는 idx:i 행의 arr[i][j]임
근데 생각해보면
arr[i][j]를 선택하려면 윗줄에서는 
arr[i-1][j-1], arr[i-1][j] 둘중 하나에서만 올수있으므로
dp[i][j]=max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]
예외처리) 맨끝값인 j=0, j= i(row)일때 무조건 1경로.


"""
N = int(input())
arr = []  # 크기n인 삼각형 담을 배열

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

# N*N 크기
dp = [[0] * N for _ in range(N)]

# 초기값 설정
dp[0][0] = arr[0][0]

# dp 테이블 채우기
for i in range(1, N):  # 1~(N-1) row 채우기
    # 각 줄 i 마다, 끝 인덱스: i
    for j in range(0, i + 1):

        # 예외) 맨왼쪽일때
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]

        # 예외) 맨오른쪽일때 인덱스 j는 i값을 가짐
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + arr[i][j]

        # 일반 케이스 : 위의 두수중 1개를 선택
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]


# 출력 - print(max(dp[N-1])) 로 1줄가능
maxval = 0  # 최대값 초기화
for elem in dp[N - 1]:
    if elem > maxval:
        maxval = elem
print(maxval)
