# 1. bfs의 dx,dy 상하좌우탐색

```python
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(4):
    nx = cur_x+dx[i]
    ny = cur_y+dy[i]
    arr[nx][ny]
```

# 2. 한방향으로 끝까지 이동하는 탐색(boj #15683-감시 )

```python
d = (0,1,2,3)
while True:
    nx += dx[d]
    ny += dy[d]
    if arr[nx][ny] == '벽' : break
```
