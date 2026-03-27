# BOJ 16953 A->B - S2
# 26.03.24
import sys

input = sys.stdin.readline
from collections import deque

"""
1. 정방향 BFS  
- 최악 O(B) = 10^9
- 경로가 겹치지 않는 이유를 생각해보면 K=짝수일때 무조건 *2를 통해 온것이고, K=홀수일때 무조건 (K-1)/10 에서 출발한것. 따라서 VIS배열 필요X

2. 역방향 그리디 
- O(log(B))
- 이방법으로 풀기

"""
A, B = map(int, input().split())

q = deque()

# 시작점: A , 연산횟수0
q.append((A, 0))

while q:
    cur_num, cnt = q.popleft()

    # print(f"{cur_num}, {cnt}")

    if cur_num == B:
        # 연산횟수+1 출력 (문제조건)
        print(cnt + 1)
        sys.exit()

    for i in [cur_num * 2, cur_num * 10 + 1]:

        # B를 넘어가면 절대 도달불가
        if i > B:
            continue

        # 연산횟수 계산후 큐에 넣기
        q.append((i, cnt + 1))


# B 도달 못해서 종료 못했을경우
print(-1)
