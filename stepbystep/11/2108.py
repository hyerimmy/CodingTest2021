#https://www.acmicpc.net/problem/2108

n = int(input())

num = list()
for i in range(0,n):
  num.append(int(input()))
num.sort()

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
print(round(sum(num)/len(num)))

# 둘째 줄에는 중앙값을 출력한다.
print(num[round(len(num)/2)])

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
from collections import Counter
cnt = Counter(num)

if(len(cnt.most_common(2))>1 and 
   cnt.most_common(2)[0][1]==cnt.most_common(2)[1][1]):
  print(cnt.most_common(2)[1][0])
else:
  print(cnt.most_common(2)[0][0])

# 넷째 줄에는 범위를 출력한다.
print(num[-1]-num[0])