# https://www.acmicpc.net/problem/10870

# Fn = Fn-1 + Fn-2 (n ≥ 2)
def fibo(n):
  if(n>=2):
    return (fibo(n-1)+fibo(n-2))
  else:
    return n

n = int(input())
print(fibo(n))