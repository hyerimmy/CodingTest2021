#https://www.acmicpc.net/problem/2525

a, b = map(int, input().split())
c = int(input())

b+=c


if(b>59):
  a+=b//60
  b=b%60

if(a>23):
  a=a%24

print(a, b)