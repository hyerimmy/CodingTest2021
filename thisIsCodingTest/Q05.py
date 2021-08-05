### 이것이 코딩테스트다 p.315###
### Q 05 - 볼링공 고르기 ###

# 12:17 ~ 12:50 (33m)

# m, n 입력받기
n, m = map(int, input().split())

# 무게 입력 받기
k = list(map(int, input().split()))

# 무게 별 공 개수 리스트로 정리
ball = [0] * m
for i in range(n):
  w = k[i]
  ball[w-1] += 1

result = 0 # 경우의 수

for a in range(0,m):
  for b in range(a+1,m):
    result += ball[a]*ball[b]

print(result)