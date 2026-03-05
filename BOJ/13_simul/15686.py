# BOJ 15686
# 치킨배달-G5
# 26.03.05
"""
[WIL]

치킨 거리 : dist(집,가장 가까운 치킨집)
[도시의 치킨 거리] : sum(모든 집의 치킨거리)
도시의 치킨집 : 최대 M개
=> M개를 고르기 + [도시의 치킨 거리] 최소로
"""
import sys

input = sys.stdin.readline

# 치킨거리 계산: 가장 가까운 치킨집
def calc_dist(home,arr):
    # home:튜플
    home_x,home_y =home 
    
    # 초기값 :999999
    min_dist= 999999

    for arr_x,arr_y in arr:
        if abs(home_x-arr_x)+abs(home_y-arr_y) <min_dist:
            min_dist = abs(home_x-arr_x)+abs(home_y-arr_y)

    return min_dist


N,M=map(int,input().split())
#도시정보 N*N
board=[list(map(int,input().split())) for _ in range(N)] 
city_num = 0 # 도시개수 <= M

#치킨집,가정집 좌표(x,y) 저장
arr_home=[]
arr_chick=[]

for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            arr_home.append((i,j))
    
        elif board[i][j]==2: 
            city_num +=1
            # 튜플로 좌표저장 
            arr_chick.append((i,j))
        
# 폐업 필요X
if city_num <=M :
    result=0
    for home in arr_home: 
        # 각집마다 치킨거리 계산 
        result += calc_dist(home,arr_chick)

#폐업 필요 , 
else:
    while city_num >M:
        #TODO : 폐업로직