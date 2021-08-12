### 백준 2884 알람 시계 ###
### https://www.acmicpc.net/problem/2884 ###

# 16:42 ~16:46 (4m)

# 입력받기
h,m = map(int,input().split())

# 계산하기
if m>=45:
  m -= 45
else:
  if h == 0:
    h = 23
  else:
    h -= 1
  m = m+60-45

print(h, m)

# 맞았습니다!