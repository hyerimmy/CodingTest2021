### 백준 [10818] 최소,최대 ###
### https://www.acmicpc.net/problem/10818 ###

# 01:36 ~ 01:40 (4m)

import sys

# 입력받기
n = int(sys.stdin.readline())

# 리스트로 입력받기
num = list(map(int, sys.stdin.readline().split()))

num.sort()
print(num[0], num[-1])

# 맞았습니다