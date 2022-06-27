# https://www.acmicpc.net/problem/11653

n = int(input())
prime_list = list()

def is_prime_num(ipn):
  if ipn==1:
    return False
  for i in range(2,ipn):
    if ipn%i==0:
      return False
  return True

for k in range(2,n):
  if(is_prime_num(k)):
    prime_list.append(k)
    print(k)

# print(prime_list)

while(is_prime_num(n)==False):
  for p in range(2,n):
    if(is_prime_num(k)):
      if n%p==0:
        n=n//p
        print(p)
        break
print(n)