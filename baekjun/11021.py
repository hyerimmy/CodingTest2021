### 백준 11021 A+B-7  ###
### https://www.acmicpc.net/problem/11021 ###

# 14:30 ~ 14:33 (3m)

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 출력하기
for i in range (0,n):
  a, b = map(int,sys.stdin.readline().split())
  print('Case #'+str(i+1)+': '+str(a+b))

# 맞았습니다!!