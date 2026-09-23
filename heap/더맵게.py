# 더맵게 - LV 2
# 우선순위 큐
# 26.04.20
"""
[문풀 WIL]
- 파이썬 힙큐는 최소힙, 최대힙 만드려면
heapq.heappush(heap, -value) # 값을 음수로 변환하여 삽입
max_val = -heapq.heappop(heap) # 꺼낼 때 다시 양수로 변환

- 최소힙에서 루트가 최솟값이니 나머지 안봐도됨
- 루트확인은 arr[0]


"""
import heapq


# len(scov)>=2
def solution(scoville, K):
    cnt = 0  # 섞은 횟수

    # 최소힙으로 변경
    heapq.heapify(scoville)

    # 예외)이미 전부 K이상인 경우
    if scoville[0] >= K:
        return 0

    # 원소가 1개일때까지 반복
    while len(scoville) >= 2:
        # 1. 가장 맵지않은 음식 + 2번째로 맵지않은 음식 섞기
        # 두번 연속 루트 pop()후  새 원소 추가
        new_food = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)

        heapq.heappush(scoville, new_food)

        cnt += 1

        # 2. 모든 원소가 K 이상인지 체크
        # 최소 힙이므로 루트가 K 이상이면 항상 만족
        if scoville[0] >= K:
            return cnt

    # 모든 원소를 K이상으로 만들수 없으면 -1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))

print(solution([1, 2, 3], 999))
