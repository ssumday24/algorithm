# 전화번호목록
# 해시-lv2
# 26.04.17
"""
[문풀]
- 문자열 1자리씩 자르는 템플릿
"""


# 다른 번호에 접두사로 포함 -> true
# 서로포함x -> false
def solution(phone_book):

    dic = {}
    # 모든 번호에 대한 딕셔너리
    for elem in phone_book:
        dic[elem] = 1

    # 각 전화번호에 대해
    # 한자리씩 잘라가며 다른번호에 포함되는지 비교
    for number in phone_book:
        temp = ""
        # x= 전화번호의 각 자릿수
        # temp= 1, 11, 119, ....,자기자신
        for x in number:
            temp += x

            # 딕셔너리에 있고 자기자신이 아닐때
            # 접두어 포함
            if temp in dic and temp != number:
                return False

    # 위에 안걸렸으면 true
    answer = True
    return answer
