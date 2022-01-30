### 백준 10871 X보다 작은 수  ###
### https://www.acmicpc.net/problem/10871 ###

# 14:54 ~ 14:59
# 12:15 ~ 12:24 (14m)

import sys

# n, x 입력받기
n, x = map(int,sys.stdin.readline().split())

# 숫자 n개 입력받기
num = list(map(int,sys.stdin.readline().split()))

# 해당 값 출력하기
for i in range (0, n):
  if num[i] < x:
    print(num[i], end=' ')

# 맞았습니다!!