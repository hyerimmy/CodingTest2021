### 백준 14681 사분면 고르기 ###
### https://www.acmicpc.net/problem/14681 ###

# 16:38 ~ 16:41 (3m)

# 입력받기
x = int(input())
y = int(input())

# 사분면 확인해 출력
if x>0:
  if y>0:
    print(1)
  else:
    print(4)
else:
  if y>0:
    print(2)
  else:
    print(3)


# 맞았습니다!