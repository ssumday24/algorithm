# 10808 : 알파벳_개수

word = input()
result = [0 for _ in range(26)] # 알파벳 개수 

for x in word:
    result[ord(x) - ord('a')]+=1  # ord() : 문자를 아스키코드로 변환 

for i in result:
    print(i,end=" ") # 줄바꿈 없이 
