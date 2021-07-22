### 이것이 코딩테스트다 p.312###
### Q 02 - 곱하기 혹은 더하기 ###

# 23:09 ~ 23:19 (10m)

# 문자열 s를 리스트로 입력받기
s = list(map(int, input()))

# 결과값
result = s[0]

for i in range(1,len(s)):
  if result<=1 or s[i]<=1:
    result += s[i]
  else:
    result *= s[i]

print(result)