# 2025.11.02 - 2회차 : 10분 
import sys

# readline 은 개행문자 \n 까지 포함하니 strip 써주기 
S = sys.stdin.readline().strip() 
cnt = ord('z')-ord('a') +1 # 알파벳개수 26개
arr= [0 for _ in range(cnt)]



for word in S:
    arr[ord(word)-ord('a')]+=1


