n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = 0

for a in range (0, n):
  for b in range(0, a):
    for c in range(0,b):
      if(num[a]+num[b]+num[c]<=m and num[a]+num[b]+num[c]>result):
        result = num[a]+num[b]+num[c]

print(result)
