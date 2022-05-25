# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())

def is_prime_num(ipn):
  if ipn==1:
    return False
  for pn in range(2,ipn):
    if(ipn%pn==0):
      return False
  return True

for i in range(m, n+1):
  if(is_prime_num(i)):
    print(i)