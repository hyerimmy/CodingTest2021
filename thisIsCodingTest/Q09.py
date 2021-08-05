### 이것이 코딩테스트다 p.323~4 ###
### Q 09 - 문자열 압축 ###

# 01:11 ~ 01:40 (29m)
# 19:54 ~ 20:03 (9m)

# 문자열 입력받기
s = input()

start = 0

# 자르는 단위를 2부터 적용
for limit in range(2, len(s)):
  # 단위를 잘라 pack 리스트로 생성
  pack = []*limit
  for i in range(0,limit):
    pack[i] = s[start]
    start += 1
  # 단위 다음 문자부터 겹치는지 확인
  for i in range(0, limit):
    if pack[i] != s[start+limit+i]:
      start += 1
      break
    
# 풀지 못함.