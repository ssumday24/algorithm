#11654 : 아스키코드

x= input()

if ((x>='A' and x<='Z')or 
    (x>='a' and x<='z')or 
    (x>='0' and x<='9')
    ):
    print(ord(x))

    
 # ord() : 문자 => 아스키코드()
 # chr() : 아스키코드 => 문자
 # ex) chr(65) = > A 
    
    