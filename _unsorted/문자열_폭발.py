#9935 - week02 Test 3번
def check(string,bomb):

    stack=[]

    #STRING 와 STACK 은 별개
    for i in string:
        stack.append(i)

    #bomb는 문자열이니 리스트로 변환필요
        
        if stack[-len(bomb):]==list(bomb):  
            for _ in range(len(bomb)):
                stack.pop() 

    
    # 스택이 비었을때
    if not stack : 
        print("FRULA")
        return
    else:
        print("".join(stack))
     

string = input().strip()
bomb =input().strip() # 개행문자 제거

# 스택의 꼭대기는 stack[-1]

check(string,bomb)
                