n = int(input())
result = 99999999
sum = 0

for i in range (0, n+1):
  for k in range(0, len(str(i))):
    sum += i[k]
  sum += i
  if (sum == n and sum < result):
    reslt = sum

print(result)

## 하는중