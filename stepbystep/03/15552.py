### 백준 15552 빠른 A+B  ###
### https://www.acmicpc.net/problem/15552 ###

# 14:18 ~ 14:21 (3m)

# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

import sys

# n 입력받기
n = int(sys.stdin.readline())

# 구구단 출력하기
for i in range (0,n):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)

# 맞았습니다.