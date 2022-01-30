# https://www.acmicpc.net/problem/1316

n = int(input())
result = n
for i in range(0,n):
  word = input()
  for i in range(0,len(word)):
    if((word.find(word[i]))+word.count(word[i]) <= i):
      #print(word[i]," / -1")
      result -= 1
      break

print(result)
