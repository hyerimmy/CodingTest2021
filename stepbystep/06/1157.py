### 백준[1157] 단어공부###
### https://www.acmicpc.net/problem/1157 ###

import sys
s = list(sys.stdin.readline().rstrip().upper())

from collections import Counter
counter = Counter(s)

max_count = -1
for letter in counter:
  if counter[letter] > max_count:
    max_count = counter[letter]
    max_letter = letter

for letter in counter:
  if counter[letter] == max_count and letter != max_letter:
    print("?")
    quit()

print(max_letter)
