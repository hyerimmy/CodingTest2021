### 백준 2439 별 찍기 - 2  ###
### https://www.acmicpc.net/problem/2439 ###

# 14:50 ~ 14:53 (3m)

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 별 출력하기
for i in range (1,n+1):
  for a in range(n-i,0,-1):
    print(' ',end='')
  for b in range(0,i):
    print('*',end='')
  print('')

# 맞았습니다!!