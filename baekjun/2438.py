### 백준 2438 별 찍기 - 1  ###
### https://www.acmicpc.net/problem/2438 ###

# 14:45 ~ 14:49 (4m)

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 별 출력하기
for i in range (1,n+1):
  for i in range(0,i):
    print('*',end='')
  print('')

#print(1, end='') # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
#print(2, end='')
#print(3)

# 맞았습니다!!