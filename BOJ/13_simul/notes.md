# 1. bfs의 상하좌우 탐색

```python
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(4):
    nx = cur_x+dx[i]
    ny = cur_y+dy[i]
    arr[nx][ny]
```

# 2. 한방향으로 끝까지 탐색(boj #15683-감시 )

```python
d = (0,1,2,3)
while True:
    nx += dx[d]
    ny += dy[d]
    if arr[nx][ny] == '벽' : break
```

# 3. 배열복사 (boj #15683-감시 )

```python
new_arr=[]

for row in current_arr:
    copied = row[:]   # copied = row 는 주소복사라 절대x
    new_arr.append(copied)

# list comprehension 간단히
new_arr = [row[:] for row in current_arr]
```

여기서 copied=row[:] 임에 주의

```python
office = [[0, 0, 0], 
          [0, 0, 0]]

#(얕은 복사)
copied = [row for row in office]

# 복사본의 맨 첫 칸에 레이저(#)
copied[0][0] = '#'

# 원본 office 출력
print(office) 
# 결과: [['#', 0, 0], [0, 0, 0]] -> 원본까지 오염

"""
따라서 [row[:] for row in current_arr]
"""
```

# 비트연산

### 왼쪽 shift (<<)
`1 << (2 * cctv.size())`

`print(4<<1)` 
1. 4 ->100 이진법 변환
2. 1000 비트연산
3. 8 - 다시 10진법 변환후 출력