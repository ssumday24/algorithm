# BOJ 15664
# N 과 M (10) - S2
# 26.03.18
import sys

input = sys.stdin.readline
"""
[WIL]
생각 순서 
1. 한원소를 여러번 고를수없으니 vis 필요 
2. 비내림차순 => 시작인덱스 (i+1)~
=> 그럼 그 이전은 안보니까 vis 배열 필요없어짐 

3. [1,7,9,9]의 9처럼 여러개인 숫자는 정렬후에 무조건 붙어있음
=> before 변수 만들어서 활용 
    
# 같은 자릿수에, 같은 수가 다시 온다면 무조건 중복이니 걸러 내야함    
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 담을 배열
result = []

# 정렬
arr.sort()


def func(depth, start):
    # M개의 수를 고르면 종료
    if depth == M:
        print(*result)
        return

    before = 0  # 이 깊이 전용 기억

    for i in range(start, N):

        # 같은자릿수에 이전값이 올떄 걸러내기
        # 초기화값이 0 이므로 arr[0]>before 
        if arr[i] == before:
            continue

        # 바로다음 반복문에 넘길 before 갱신
        before = arr[i]

        result.append(arr[i])

        # 다음 깊이에서는 start: i+1~
        func(depth + 1, i + 1)

        result.pop()


# 깊이0, start idx:0 시작
func(0, 0)
