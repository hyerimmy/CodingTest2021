### 백준 [2675] 문자열 반복 ###
### https://www.acmicpc.net/problem/2675 ###

import sys

c = int(sys.stdin.readline())
for p in range(0,c):
  n, s = sys.stdin.readline().split()
  for k in range(0,len(s)):
    for i in range(0,int(n)):
      print(s[k],end='')
  print()

# 맞았습니다