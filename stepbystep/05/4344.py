### 백준 [4344] 평균은 넘겠지 ###
### https://www.acmicpc.net/problem/4344 ###

import sys

# c 입력받기
c = int(sys.stdin.readline())

# 변수 생성
avg = 0

# 케이스 입력받기
for i in range(0,c):
  case = list(map(int, sys.stdin.readline().split()))
  result = 0
  avg = (sum(case)-case[0])/case[0]
  for n in range(1,case[0]+1):
    if(case[n]>avg):
      result += 1
      #print(case[n], result)
  result = format((result/case[0])*100,"0.3f")
  print(str(result)+'%')