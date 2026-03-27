#1085:직사각형에서 탈출
x,y,w,h= map(int,input().split())  #리스트 정수를 변수에 매핑


d1=x
d2=y
d3=(w-x)
d4=(h-y)
print(min(d1,d2,d3,d4))
