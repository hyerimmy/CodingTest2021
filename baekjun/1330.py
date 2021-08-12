### 백준 1330 두 수 비교하기 ###
### https://www.acmicpc.net/problem/1330 ###

# 16:26 ~ 16:27 (1m)

# 입력받기
a, b = map(int, input().split())

# 비교하여 출력하기
if a<b:
  print('<')
elif a>b:
  print('>')
else:
  print('==')

# 맞았습니다!!