# 이중우선순위큐 - LV 3
# 힙
# 26.04.20
"""
[문풀 WIL]
- 최소힙에서 최댓값은 모든원소 순회(O(N)) 해야 하는 문제가 있음
- 이때는 힙 두개를 만들고, 유령원소를 계속 pop() 하는 식으로 해결가능
- 힙에 튜플(num1,num2,num3,...) 넣으면 기준은 왼쪽부터 (사전순 정렬)

- heap에서 push, pop 하면 자동으로 정렬
- 힙에서 루트말고 다른원소는 건드리면 안됨
##########
- 루트만 유령이 아니면, 자식이 유령이어도 max/min 구하는 것에 아무런 영향x
##########
"""
import heapq


# 빈큐삭제 ->무시
def solution(operations):
    answer = [0, 0]

    arr_min = []
    arr_max = []

    # i 번째 명령의 숫자가 이미 삭제된 숫자인지 판단
    exist = [False] * (1000000)

    # 명령 개수만큼 반복
    for i in range(len(operations)):
        oper, num = operations[i].split()
        num = int(num)  # 문자열->정수

        # 삽입
        if oper == "I":
            # 최소힙
            heapq.heappush(arr_min, (num, i))

            # 최대힙 : 음수로 넣기
            heapq.heappush(arr_max, (-1 * num, i))

            # i번째 명령에서 넣은 숫자존재
            exist[i] = True

        # 삭제
        # 최소힙의 최댓값 ,
        # 최대힙의 최솟값은 실제로 삭제하지 않고 exist로 판단
        elif oper == "D":
            # 예외1) 빈 큐를 삭제할 경우

            # 최댓값 삭제
            if num == 1:
                # 루트가 유령데이터 아닐때까지 계속 pop
                while arr_max and not exist[arr_max[0][1]]:
                    heapq.heappop(arr_max)

                # 빈 큐가 아닐때만
                if arr_max:
                    # 실제 숫자삭제 + 몇번째 숫자인지 기록
                    _, tmp_i = heapq.heappop(arr_max)

                    # 유령숫자로 표기 -> 최소힙에서 봐도 유령임
                    exist[tmp_i] = False

            # 최솟값 삭제
            elif num == -1:
                # 루트가 유령데이터 아닐때까지 계속 pop
                while arr_min and not exist[arr_min[0][1]]:
                    heapq.heappop(arr_min)

                # 빈 큐가 아닐때만
                if arr_min:
                    # 실제 숫자삭제 + 몇번째 숫자인지 기록
                    _, tmp_i = heapq.heappop(arr_min)

                    # 유령숫자로 표기 -> 최소힙에서 봐도 유령임
                    exist[tmp_i] = False

    # 삭제된 숫자인지 최종 검사
    while arr_max and not exist[arr_max[0][1]]:
        heapq.heappop(arr_max)
    while arr_min and not exist[arr_min[0][1]]:
        heapq.heappop(arr_min)

    # 출력
    # 큐가 안비었을때
    if arr_min:
        answer[0] = arr_max[0][0] * (-1)
        answer[1] = arr_min[0][0]
        return answer

    # 큐가 비었을때:
    else:
        return [0, 0]


###출력
r = solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(r)
