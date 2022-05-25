# https://www.acmicpc.net/problem/2839

n = int(input())
result = -1
max = n//5
while (max>=0):
  if((n-5*max)%3==0):
    result = max + (n-5*max)//3
    break
  max-=1

print(result)