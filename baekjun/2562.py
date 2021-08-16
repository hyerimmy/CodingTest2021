### 백준 [2562] 최댓값###
### https://www.acmicpc.net/problem/2562 ###

# 01:41 ~ 01:53 (12m)

import sys

num = [0]*9
index = 0

# 입력받기
for i in range(0,9):
  num[i] = int(sys.stdin.readline())
  if num[i] > num[index]:
    index = i

print(num[index])
print(index+1)

# 맞았습니다