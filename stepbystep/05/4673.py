### 백준 [4673] 셀프 넘버 ###
### https://www.acmicpc.net/problem/4673 ###

def d(n):
  result = n
  for i in range(0,len(str(n))):
    result += n%10
    n = n//10
  #print(n, result)
  return result

list = []

for i in range (1,10001):
  list.append(d(i))

for i in range(1,10001):
  if not i in list:
    print(i)

# 맞았습니다.