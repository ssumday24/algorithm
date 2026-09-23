# BOJ 1335
# 트럭 - S1
# 26.03.29
"""
큐 시뮬레이션문제면
1. 맨앞쪽부터 처리 -> 맨뒤쪽 처리
    - popleft(방출) -> 조건확인 -> append(진입)
2. 시간 계산문제는, time+=1 맨앞에 배치해서 반복 줄이기

3. 전체크기가 고정된 큐 문제에서는
- 큐에 하나뺴고 하나 넣으니 길이 고정
- 따라서 길이검사 필요x

4. 상태값은 무조건 O(1)로 관리 (ex)다리무게

"""
import sys
from collections import deque

input = sys.stdin.readline

# n: 트럭수 / w: 다리길이 / L: 다리 최대하중
N, W, L = map(int, input().split())

# 각 트럭 무게 저장
truck = deque(map(int, input().split()))

# 다리상태 큐/ 다리길이: W
bridge = deque([0] * W)

# 경과 시간
time = 0

# 다리 총 무게
cur_weight = 0

# 다리가 비면 종료
while bridge:
    # 각 1초마다
    time += 1

    # 하나씩 당기기
    # 다리원소개수 -1
    front = bridge.popleft()

    # 맨앞 나간만큼 무게감소
    cur_weight -= front

    # 더 올라와야할 트럭이 남았으면
    if truck:
        # 올려야 할 큐의 맨앞 트럭
        cur_truck = truck[0]

        # 무게초과 ->못넣음
        if cur_weight + cur_truck > L:
            # 앞의 트럭들과 1칸씩 차이가 나야하니 제로패딩
            bridge.append(0)

        # 트럭 넣기 가능함
        else:
            # 큐에 하나뺴고 하나 넣으니 길이는 고정,
            # 따라서 길이검사 필요x
            cur_truck = truck.popleft()
            bridge.append(cur_truck)
            cur_weight += cur_truck

    # 트럭 더 없으면
    else:
        continue

# 출력: 모든 트럭이 건넜을때 시간?
print(time)
