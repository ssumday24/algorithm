def dfs(start, current, total, depth):
    global min_cost

    # 가지치기
    if total >= min_cost:
        return

    # 모든 도시 방문 완료
    if depth == N - 1:
        if Matrix[current][start] != 0:  # 다시 시작점으로 갈 수 있는지 확인
            min_cost = min(min_cost, total + Matrix[current][start])
        return

    for i in range(N):
        if not visited[i] and Matrix[current][i] != 0:
            visited[i] = True
            dfs(start, i, total + Matrix[current][i], depth + 1)
            visited[i] = False  # 백트래킹

##################################################################################

N=int(input())
Matrix = [list(map(int,input().split())) for _ in range(N)]

min_cost= float("inf") # 초기화용

visited = [False]*N
visited[0]=True
dfs(0,0,0,0)

print(min_cost)