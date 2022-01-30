### 백준 [1546] 평균 ###
### https://www.acmicpc.net/problem/1546 ###

# 02:10 ~ 02:18 (8m)

import sys

# 입력
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
#print(score)

# 최댓값 M 구하기
tscore = score
tscore.sort()
m = tscore[-1]
#print(m)

# 점수 새로 계산
for i in range(0,n):
  score[i] = score[i]/m*100

print(sum(score)/len(score))


# 맞았습니다!!