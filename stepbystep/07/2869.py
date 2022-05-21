# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

result = 1

# while(v>0):
#   v-=a
#   if(v<=0):
#     break;
#   v+=b
#   result+=1


v-=a
# while(v>0):
#   v=v+b-a
#   # print(str("result"),result,str("v"), v)
#   result+=1

import math
temp = math.ceil(v/(a-b))
result+=temp

print(result)