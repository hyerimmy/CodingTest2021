n = int(input())
for i in range(0,n):
  i = list(map(int, input().split()))
result = [0]*n

for a in range(0,n+1):
  for b in range(a+1,n+1):
    print(str(a)[0])
    if str(a)[0]>str(b)[0] and str(a)[1]>str(b)[1]:
      result[a] += 1

print(result)

#### 아이고~~