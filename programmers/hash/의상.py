# 의상
# 해시-lv2
# 26.04.17
"""
[노트]
- 딕셔너리에서 for x in dic 에서 x에는 key가 담김
- 배열의 indexError처럼,딕셔너리에서는 없는 key 부르면 KeyError.

[조건]
clothes=[[옷이름,옷종류]]

r1. 옷 1개이상은 입어야함
- 전체 - 모두 안입는 1가지경우
- 그럼 각 부위별로 몇종류 있는지만 알면됨
"""


def solution(clothes):
    answer = 1  # 가짓수마다 곱해야하니 초기값 1
    check = {}  # 부위별 개수 담을 딕셔너리

    for name, kind in clothes:
        # 처음 나온 부위일때
        if kind not in check:
            check[kind] = 1

        # 기존 부위면 +1
        else:
            check[kind] += 1

    for x in check:
        answer *= check[x] + 1

    # print(d)
    # print(check)

    return answer - 1  #  모두 안입는 1가지경우 제외


#
x = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
y = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(x))
print(solution(y))
