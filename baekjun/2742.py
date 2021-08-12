### 백준 2742 기찍N  ###
### https://www.acmicpc.net/problem/2742 ###

# 14:25 ~ 14:28 (3m)

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 출력하기
for i in range (n, 0, -1):
  print(i)

# for i in range(10, 0) 은 작동하지 않음
# for i in range(10, 0, -1)으로 작성해야 함.

# 맞았습니다!!