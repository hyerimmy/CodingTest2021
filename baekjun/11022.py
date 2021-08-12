### 백준 11022 A+B-8  ###
### https://www.acmicpc.net/problem/11022 ###

# 14:43 ~ 14:44 (1m)

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 출력하기
for i in range (0,n):
  a, b = map(int,sys.stdin.readline().split())
  print('Case #'+str(i+1)+': '+str(a)+' + '+str(b)+' = '+str(a+b))

  # 맞았습니다.