# https://www.acmicpc.net/problem/2480

num = list(map(int, input().split()))
num.sort()

if(num[0]==num[1] or num[1]==num[2]):
  if(num[0]==num[2]):
    print(10000+num[0]*1000)
  else:
    print(1000+num[1]*100)
else:
  print(num[2]*100)