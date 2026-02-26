# BOJ 15652
# N과M (4) - S3
# 26.02.26
"""
- 1~N중 M개를 고른 수열
- 같은수 여러번 가능
- 비 내림차순 : a1 <= a2 <= a3 ...
- BOJ 15650과 비교 
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M= map(int,input().split())
arr=[]
vis=[False] * (N+1) # idx : 1~N 

def func(depth):
    
    if     



###
func(0)