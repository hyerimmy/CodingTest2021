#https://www.acmicpc.net/problem/10250

import math

t = int(input())
result = list()

for i in range(0,t):
  h, w, n = map(int,input().split())
  y = n%h
  x = math.ceil(n/h)
  if y==0:
    y=h
  result.append(str(y)+str(x).zfill(2))


for r in result:
  print(r)