# 회사에 있는 사람_7785
# 26.03.31
"""
-해시 문제집

1. 리스트 대신 해시 필요이유: N<= 10^6
리스트에서 원소를 찾고 지우는 작업은 O(N)이니 N개 입력에 대해
O(N^2)-> 시간초과

2. 반면 해시기반 set/dict 는 add/remove/find O(1)에 가능

3.Set : 존재여부가 중요 / 중복제거 목적일때
- set은 Key만 저장

4.Dict : key,value 한 쌍으로 저장

5.집합 set()/딕셔너리{}는순서가 없어서 sort()함수 불가
-> 정렬후 리스트로 반환해주는 sorted() 사용
"""

import sys

input = sys.stdin.readline

N = int(input())
company = set()

for _ in range(N):
    name, log = input().split()

    if log == "enter":
        company.add(name)
    else:
        company.remove(name)

# 사전순의 역순으로 정렬
company = sorted(company, reverse=True)

# 결과
print(*company)
