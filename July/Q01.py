### 이것이 코딩테스트다 p.311###
### Q 01 - 모험가 길드 ###

# 19:52~20:05 (13m)

# 모험가 수 n 입력받기
n = int(input())

# 각 모험가의 공포도 값 입력받기
data = list(map(int, input().split()))
data.sort()

result = 0 # 최종그룹수
count = 0 # 그룹의 현재 멤버 수
full = 0 # 그룹의 충족해야 하는 멤버 수

for i in data:
  count += 1
  if full  < data[i]:
    full = data[i]
  if count == full:
    count = 0
    full = 0
    result += 1

print(result)
