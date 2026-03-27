#2628 : 종이자르기

w, h = map(int,input().split()) #가로 세로길이

num = int(input()) #칼로 잘라야하는 점선의 개수

row_cuts=[0,h]  # 사각형 높이는 (0 부터 h) 까지
col_cuts=[0,w]  # 사각형 가로길이는 (0부터 w) 까지


for _ in range(num):
    
    p,q = map(int,input().split())
    
    if p == 0 : #가로로 자르기
        row_cuts.append(q)
        
    elif p ==1 : #세로로 자르기
        col_cuts.append(q)
        
        
# 예제입력처럼  w=10, h= 8 이면
# row_cuts=[0,8,3,2] / col_cults=[0,10,4]
# 일단 정렬필요

row_cuts=sorted(row_cuts)
col_cuts=sorted(col_cuts)

#print(row_cuts)
#print(col_cuts)

# 높이 = abs(0-2 / 2-3 / 3-8)
max_h=0

for i in range(len(row_cuts)-1):
    diff= abs(row_cuts[i]-row_cuts[i+1])
    
    if diff > max_h:
        max_h = diff
        
max_w= 0  
for i in range(len(col_cuts)-1):  
    # 끝에서 두번째 원소의 인덱스까지만 비교
    diff= abs(col_cuts[i]-col_cuts[i+1])
    
    if diff > max_w:
        max_w = diff

print(max_w*max_h)
    
    