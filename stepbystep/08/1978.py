# https://www.acmicpc.net/problem/1978

n = int(input())
num = list(map(int,input().split()))
result = 0

def is_prime_number(k):
  if k==1:
    return 0

  for i in range(2,k):
    if(k%i==0):
      return 0
  return 1

for nn in num:
  result+=is_prime_number(nn)
  # print(nn, result)
print(result)
     