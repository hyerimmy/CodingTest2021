### 이것이 코딩테스트다 p.321 ###
### Q 07 - 럭키 스트레이트 ###

# 01:09 ~ 01:16 (7m)

# 점수 n 입력받기
n = input()

# 왼쪽 자리 합 구하기
left = 0
for i in range (0,int(len(n)/2)):
  left += int(n[i])

# 오른쪽 자리 합 구하기
right = 0
for i in range (int(len(n)/2),int(len(n))):
  right += int(n[i])

if left == right:
  print("LUCKY")
else:
  print("READY")