### 백준 1655 가운데를 말해요 ###
### https://www.acmicpc.net/problem/1655 ###

# 02:08 ~ 02:21 (13m)

# n 입력받기
n = int(input())

# 수 입력받기
nlist = []
for i in range(0,n):
  nlist.append((int(input())))
print(nlist)

# 결과값 리스트로 정리
result = []
for i in range(0,n):

'''
# 결과 인덱스 넣을 리스트 정의
result = []

# 반복하며 결과값 리스트에 저장
for i in range(0,n):
  num = int(input()) # 새로운 수 입력받기
  list.append(num)
  list.sort()
  if len(list)%2 == 0: # 길이가 짝수면
    rindex = int(len(list)/2-1)
  else: # 길이가 홀수면
    rindex = int(len(list)/2)
  result.append(list[rindex])

# 결과 리스트 값 출력
for i in range(0,len(result)):
  print(result[i])
  '''