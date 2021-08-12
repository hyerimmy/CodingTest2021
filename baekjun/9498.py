### 백준 9498 시험 성적 ###
### https://www.acmicpc.net/problem/9498 ###

# 16:29 ~ 16:31 (2m)

# 입력받기
s = int(input())

# 시험 성적 출력
if 100>=s>=90:
  print('A')
elif 90>s>=80:
  print('B')
elif 80>s>=70:
  print('C')
elif 70>s>=60:
  print('D')
else:
  print('F')

# 맞았습니다!