def func4(tmp):
    brute = tmp
    
    #자리수가 3인경우만
    for i in range(3): 
        res = (brute%4)
        print(f"{res}",end='')
        brute //=4 
    print()

#4진법-> 일의자리부터 거꾸로 출력
func4(39)
print("======")

print(4<<1)