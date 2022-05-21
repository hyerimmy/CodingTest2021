### 백준 [8959] OX퀴즈 ###
### https://www.acmicpc.net/problem/8959 ###

# 02:20 ~ 02:24 (4m)

import sys

n = int(sys.stdin.readline())

for i in range(0,n):
  s = sys.stdin.readline()
  cnt = 0
  score = 0
  for i in range(0,len(s)):
    if s[i] == 'O':
      score += 1+cnt
      cnt += 1
    else:
      cnt = 0
  print(score)

  # 맞았습니다!!