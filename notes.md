# 1. bfs의 상하좌우 탐색

```python
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(4):
    nx = cur_x+dx[i]
    ny = cur_y+dy[i]
    arr[nx][ny]
```

# 2. 한방향으로 끝까지 탐색

- #15683-감시

```python
dx=[-1,1,0,0]
dy=[0,0,-1,1]

nx= cur_x
ny= cur_y

while True:
    nx += dx[d]
    ny += dy[d]
    if arr[nx][ny] == '벽' : break
```

# 3. 배열복사

- #15683-감시

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

# 배열회전

```python
# 배열 90도회전 R*C -> C*R
def rotate(stick,R,C):
    new_arr= [[0]*R for _ in range(C)]

    for x in range(R):
        for y in range(C):
            # (x,y) -> (y,-x+R-1)
            if stick[x][y]==1:
                new_arr[y][R-1-x]=1

    return new_arr

#좌표들로 일차방정식 유도가능
```

# 배열에서 pop() 주의 - 03.05

```python
arr = ['A', 'B', 'C']
for i in range(3):
    arr.pop(i)
```

- 인덱스를 돌면서 pop()을 해버리면 절대 안됨
- i=0 : arr=[B,C] 남음
- i=1 : arr=[C] 남음
- i=2 : indexError 발생

# 03.19

- 튜플원소 순회하며 칠하기
  [(0,), (1,), (2,), (3,)]
  예를들어 (1) 처럼 원소가 하나에 쉼표가 없으면 일반 정수로 처리되니
  쉼표 필수
- 파이썬의 기본값은 수학 괄호() 이므로 튜플이아닌 정수로 처리되는것

- 슬라이딩 윈도우 - 스티커붙이기 #18808

    ```python
    for i in range(N - R + 1):
            for j in range(M - C + 1):
    ```
