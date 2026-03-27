# (a^b) mod  m  : c++,java -> overflow 
def func1(a,b,m):
    val = 1
    while (b>0):
        val = val * a
        b -=1
    
    return val % m

res = func1(6,100,5) #6^100 % 5
print(res)

def func2(a,b,m):
    val = 1
    while (b>0):
        val = (val * (a%m) %m)
        b -=1
    
    return val % m

res = func2(6,100,5)
print(res)