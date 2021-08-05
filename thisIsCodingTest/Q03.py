### 이것이 코딩테스트다 p.313###
### Q 03 - 문자열 뒤집기 ###

# 23:30 ~ 23:41 (11m)

# 문자열 입력받기
s = input()

num = s[0]
set = 1

for i in range(1,len(s)):
  if(num != s[i]):
    set +=1
    num = s[i]

print(set//2)