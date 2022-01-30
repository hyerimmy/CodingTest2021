### 백준 [10809] 알파벳찾기 ###
### https://www.acmicpc.net/problem/10809 ###

import sys
alp = [-1]*26
word = sys.stdin.readline().rstrip()

for i in range(0,len(word)):
  #print(ord(word[i]))
  if alp[ord(word[i])-97] == -1:
    alp[ord(word[i])-97]=i

for i in range(0,26):
  print(alp[i],end=' ')

  # 맞