#https://www.acmicpc.net/problem/2750

n = int(input())

num = list()
for i in range(0,n):
  num.append(int(input()))
num.sort()

for i in num:
  print(i)