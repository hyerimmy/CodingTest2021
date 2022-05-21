### 백준 [11720] 숫자의 합 ###
### https://www.acmicpc.net/problem/11720 ###

import sys
n = int(sys.stdin.readline())
num = sys.stdin.readline()
result = 0

for i in range(0,n):
  result += int(num[i])
print(result)

# 맞았습니다