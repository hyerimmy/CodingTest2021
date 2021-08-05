### 백준 12865 평범한 배낭 ###
### https://www.acmicpc.net/problem/12865 ###

# 01:30 ~ 02:04

# 물건 수와 최대 무게 입력 받기
n, k = map(int, input().split())

# 각 물건의 무게와 가치 입력 받기
w = [0]*n
k = [0]*n
for i in range(0,n+1):
  wt, kt = map(int, input().split())
  w[i] = wt
  k[i] = kt

# 무게 정렬해서 새로운 리스트 생성
wsort = w.sort()


print(w, k)

# 코드 작성 중