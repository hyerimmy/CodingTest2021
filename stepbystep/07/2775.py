#https://www.acmicpc.net/problem/2775

def num(k,n):
  if k==0:
    return n
  else:
    result=0
    for i in range(1,n+1):
      result+=num(k-1,i)
    return result

t = int(input())
result=list()

for i in range(0,t):
  k = int(input())
  n = int(input())
  result.append(num(k,n))

for r in result:
  print(r)

  ## 시간초과