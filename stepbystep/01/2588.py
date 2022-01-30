### 백준 2588 곱셈 ###
### https://www.acmicpc.net/problem/2588 ###

# 23:31 ~ 23:41 (10m)

# 입력받기
n = int(input())
m = input()

# (3) 출력하기
a = n*int(m[2])
print(n*int(m[2]))

# (4) 출력하기
b = n*int(m[1])
print(b)

# (5) 출력하기
c = n*int(m[0])
print(c)

# (6) 출력하기
print(a+b*10+c*100)

# 맞았습니다!