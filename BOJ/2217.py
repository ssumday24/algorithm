# 백준 #2217. 로프
# 중량이 w이고 , k개의 로프
# 목표 :로프에 대한 정보가 주어졌을때, 들어올릴수 있는 물체의 최대중량
"""
예시) 10, 15 => 출력: 20(w)
모든 로프를 사용할 필요는 없음
"""

N =int(input())
ropes=[int(input()) for _ in range(N)] # 로프들 : 버틸수 있는 최대 중량
ropes.sort(reverse=True) # 내림차순  [100,50,30,10]

max_result=0

for k in range(1,len(ropes)+1): # k 개의 로프 사용
    weight = ropes[k-1] * k
    if weight > max_result:
        max_result = weight

print(max_result)