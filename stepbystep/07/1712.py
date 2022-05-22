# 손익분기점
# https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())

# result = -1
# n=int(a/c-b)
# print(n)

# if c<b:
#   print(result)
# else:
#   while True:
#     n+=1000
#     print(n, "/ a=b*n", a+b*n, "/ c*n", c*n)
#     if((a+b*n)<(c*n)):
#       while ((a+b*n)>=(c*n)):
#         result = n
#     else:
#       print(result)
#       quit()
## 시간초과 왓더헬


if c<=b:
  result=-1
else:
  result = (a//(c-b))+1

print(result)
