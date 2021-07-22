### 이것이 코딩테스트다 p.314 ###
### Q 04 - 만들 수 없는 금액 ###

# 12:31 ~ 13:08

# n 입력받기
n = int(input())

# 화폐 단위 입력 받기
c = list(map(int, input().split()))
c.sort()

max = list()

result = 1
for a in range(len(c)):
  max[a] = 0
  for i in range(len(c)):
    if(c[i]<a):
      max[a] = i