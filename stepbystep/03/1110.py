### 백준 [1110] 더하기 사이클 ###
### https://www.acmicpc.net/problem/1110 ###

# 12:49 ~ 01:09 (10m)

import sys

# 결과값 저장할 변수
r = 0
result = []

# 입력받기
n = int(sys.stdin.readline())
result.append(n)

while 1:
  # 단계1 - 각 자리수 더하기
  r = result[-1] % 10 + result[-1]//10

  # 단계2 - 새로운 수 구하기
  r = result[-1]%10*10 + r%10

  if r not in result:
    result.append(r)
  else:
    break

print(len(result))

# 맞았습니다!!