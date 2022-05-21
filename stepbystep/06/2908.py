# https://www.acmicpc.net/problem/2908

a, b = input().split()
result = 0

for i in range(2,-1, -1):
  if(a[i] > b[i]):
    result = a
    break
  elif(a[i] < b[i]):
    result = b
    break

print(result[::-1])