# 베스트앨범 - LV 3
# 해시
# 26.04.19
"""
[문풀 WIL]
- 람다정렬 복습
- 정렬기준이 여러개일때 reversed 못쓰니 "음수" 곱해서 내림차순 정렬
- 딕셔너리 하나만 쓰지말고, 총합을 관리하는 딕셔너리를 하나더 만들기
- 딕셔너리를 value 기준으로 내림차순 정렬하는법?
    - arr.items() 는 (key,value) 뽑아주지만 껍데기만 리스트처럼 보일뿐  리스트가 아님.
    - sort() 는 in-place 정렬로, 반드시 리스트만 정렬가능
    - 따라서 sorted() 사용해야함

"""


def solution(genres, plays):
    answer = []
    dic = {}  # 장르별 (번호,재생횟수) 저장
    play_sum = {}  # 장르별 총 재생횟수 저장

    # 장르별 딕셔너리 만들기
    # gen[고유번호]=재생횟수
    # 음악 개수만큼 반복
    for i in range(len(genres)):
        gen = genres[i]
        play = plays[i]

        # 1.없는 장르면 리스트 만들기
        if gen not in dic:
            dic[gen] = []  # 튜플 담아둘 리스트

        # 1.순서쌍 (음악번호,재생횟수) 저장
        dic[gen].append((i, play))

        # 2. 장르별 총합 저장
        # 없는 장르면 만들기
        if gen not in play_sum:
            play_sum[gen] = 0

        play_sum[gen] += play

    # 재생횟수 "내림"차순 정렬 - x[1]
    # 재생횟수가 같으면 고유 번호 오름차순 정렬 - x[0]
    for gen in dic:
        # 내림차순 -> 음수곱하기
        dic[gen].sort(key=lambda x: (-x[1], x[0]))

    # 장르별 총합 내림차순 정렬
    temp = sorted(play_sum.items(), key=lambda x: x[1], reverse=True)

   
    # 최종 계산
    for gen, tot in temp:
        # 각 장르마다 최대 2개씩 넣기
        cnt = 0

        for idx, play_cnt in dic[gen]:
            # 2개 초과면 다음 장르로 넘어가기
            if cnt == 2:
                break

            answer.append(idx)
            cnt += 1

    return answer


###
x=solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

print(x)