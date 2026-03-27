#2753 : 윤년

y = int (input())

#윤년 은 4의 배수이면서 100의 배수가 아닐때 or 400의 배수일때

if (( y % 4 == 0 and y% 100 != 0 )or y % 400 ==0):
    print(1)
else:
    print(0)