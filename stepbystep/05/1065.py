### 백준 1065 한수  ###
### https://www.acmicpc.net/problem/1065 ###

import sys

def hansu(a):
  a = str(a)
  if len(a) < 2:
    #print(a,'True1')
    return True
  differ = int(a[1])-int(a[0])
  for i in range(0,len(a)-1):
    if(differ != int(a[i+1])-int(a[i])):
      #print(a,'False2')
      return False
  #print(a,'True3')
  return True

n = int(sys.stdin.readline())
result = 0

for i in range(1,n+1):
  if hansu(i):
    result += 1

print(result)

# 맞았