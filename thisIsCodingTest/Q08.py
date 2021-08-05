### 이것이 코딩테스트다 p.322 ###
### Q 08 - 문자열 재정렬 ###

# 01:23 ~ 01:43 (20m)

# 문자열 S 입력받기
s = input()

# 숫자 리스트 생성
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 숫자 합 저장할 변수
sum = 0

# 문자열 따로 모을 리스트
al = list()

for i in range(0,len(s)):
  if s[i] in num:
    sum += int(s[i])
  else:
    al.append(s[i])

al.sort()

for i in al:
  print(i, end="")
print(sum)