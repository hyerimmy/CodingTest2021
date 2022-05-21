#https://www.acmicpc.net/problem/5622

word = input()
result = 0

for i in range(0,len(word)):
  if(ord(word[i])<68):
    result += 3
  elif(ord(word[i])<71):
    result += 4
  elif(ord(word[i])<74):
    result += 5
  elif(ord(word[i])<77):
    result += 6
  elif(ord(word[i])<80):
    result += 7
  elif(ord(word[i])<84):
    result += 8
  elif(ord(word[i])<87):
    result += 9
  else:
    result += 10

print(result)