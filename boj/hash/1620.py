# 포켓몬 이다솜_1620
# 26.03.31
"""
해시 문제집

- 문자열/숫자 분류-> .isgdigit()
- value -> key 찾는건 O(N)이므로 딕셔너리 하나더


reversed_dict = {v: k for k, v in poke_dict.items()}
로 key,value 뒤집기 가능
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dict1 = {}  # 이름:숫자
dict2 = {}  # 도감번호:이름

# N개 포켓몬 입력
for num in range(1, N + 1):
    # 도감번호 1~N
    name = input().rstrip()
    dict1[name] = num
    dict2[num] = name

# m개 문제
for _ in range(M):
    query = input().rstrip()
    # 문자열/숫자 분류-> .isgdigit()

    # value -> key찾기 는 O(N) 이니
    # 딕셔너리 하나 더 만들어야함
    if query.isdigit():
        query = int(query)
        print(dict2[query])

    # key -> value
    else:
        print(dict1[query])
