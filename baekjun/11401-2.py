### 백준 11401 이항계수3 ###
### https://www.acmicpc.net/problem/11401 ###

# 입력받기
import sys
n, k = map(int, sys.stdin.readline().split())

# 팩토리얼! 함수 정의
def f(num):
  fac = 1
  for i in range(1,num+1):
    fac *= i
  return fac

# 이항계수(n,k) 계산하기
result = f(n)/(f(k)*f(n-k))

# 나머지 계산
print(int(result%1000000007))

# 시간 초과