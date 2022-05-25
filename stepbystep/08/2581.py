# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())

result1=0
result2=10000


def is_prime_num(ipn):
  if (ipn==1):
    return False
  for k in range(2,ipn):
    if (ipn%k==0):
      return False
  return True

for i in range(m, n+1):
  if(is_prime_num(i)):
    result1+=i
    if(result2>i):
      result2=i

if(result1==0):
  print("-1")
else:
  print(result1)
  print(result2)