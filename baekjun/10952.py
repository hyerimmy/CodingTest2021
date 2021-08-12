### [10952] A+B-5 ###
### https://www.acmicpc.net/problem/10952 ###

# 12:36 ~ 12:42 (6m)

import sys


a,b = map(int, sys.stdin.readline().split()) # 입력받기

while(a!=0 and b!=0):
  print(a+b) # 합 출력하기
  a,b = map(int, sys.stdin.readline().split()) # 입력받기

# 맞았습니다!!