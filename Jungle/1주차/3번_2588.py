#2588 곱셈   / : 나누기 // : 몫
a=int(input()) 
b=int(input())

c=a* ( b%10 )  # 385 %10 = 5  
d=( a*(b % 100 // 10 ) ) # 80 =  (385 % 100 // 10)  
e= a*(b // 100)    
f=a*b 

print(c)
print(d)
print(e)
print(f)