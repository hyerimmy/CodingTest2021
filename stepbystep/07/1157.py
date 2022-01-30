### 백준[1157] 단어공부###
### https://www.acmicpc.net/problem/1157 ###

import sys
s = list(sys.stdin.readline().upper())
print(s)

# count list 생성
c = [0]*len(s)

import collections
count = collections.Counter(s)
print(count)