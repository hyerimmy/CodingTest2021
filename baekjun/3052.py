### 백준 [3052] 나머지 ###
### https://www.acmicpc.net/problem/3052 ###

# 02:03 ~ 02:06 (3m)

import sys
result = []

# 입력받기
for i in range(0,10):
  n = int(sys.stdin.readline())
  if n%42 not in result:
    result.append(n%42)

print(len(result))

# 맞았습니다!!