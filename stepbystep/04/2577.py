### 백준 [2577] 숫자의 개수 ###
### https://www.acmicpc.net/problem/2577 ###

# 01:54 ~ 02:01 (7m)

import sys

# a,b,c 입력받기
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

# 곱한 값 계산하기
result = str(a*b*c)

# 각 숫자별 카운팅 수 저장할 리스트
cnt = [0]*10

for i in range(0,len(result)):
  cnt[int(result[i])] += 1

for i in range (0,10):
  print(cnt[i])

# 맞았습니다!