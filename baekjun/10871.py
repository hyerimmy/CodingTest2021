### 백준 10871 X보다 작은 수  ###
### https://www.acmicpc.net/problem/10871 ###

# 14:54 ~ 14: (m)

import sys

# n, x 입력받기
n, x = map(int,sys.stdin.readline().split())

# 결과 리스트 생성
result = []

# 입력받기
for i in range (0, n):
  a = int(sys.stdin.readline())
  if a < x:
    result.append(a)

print(a)

# 푸는중