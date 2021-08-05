### 이것이 코딩테스트다 p.316~7###
### Q 06 - 무지의 먹방 라이브 ###

# 12:58 ~ 13:09 (11m)

# food_times 리스트 입력받기
food_times = list(map(int, input().split()))

# k 입력받기
k = int(input())

time = 0

while time < k+1:
  for i in range(len(food_times)):
    if food_times[i] > 0:
      food_times[i] -= 1
      result = i+1
      time += 1

print(result)