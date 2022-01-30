### 백준 2753 윤년 ###
### https://www.acmicpc.net/problem/2753 ###

# 16:34 ~ 16:37 (3m)

# 입력받기
y = int(input())

# 윤년인지 확인해 출력
if y%4==0 and y%100!=0 :
  print(1)
elif y%400==0:
  print(1)
else:
  print(0)

# 맞았습니다!