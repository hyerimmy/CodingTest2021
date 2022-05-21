# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

result = 1

while(v>0):
  v-=a
  if(v<=0):
    break;
  v+=b
  result+=1

print(result)