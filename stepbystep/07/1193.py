#분수찾기
#https://www.acmicpc.net/problem/1193

# 1/1 - 1/2 - 2/1 - 3/1 - 2/2 - 1/3 - ...
# 분모 : 1 / 2 1 / 1 2 3 / ...
# 분자 : 1 / 1 2 / 3 2 1 / ...

x = int(input())
xi = x
max=0
up=0
down=0
first=0

for i in range(1,x+1):
  if(x-i)<=0:
    max=i
    # print("max"+str(max))
    break
  x-=i


for i in range(1,max):
  first+=i
first=first+1
# print("first"+str(first))
down=max-(xi-first)
# print(xi-first)
up=max+1-down

if(max%2!=0):
  temp = up
  up = down
  down = temp

print(str(up)+"/"+str(down))