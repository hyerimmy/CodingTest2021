### 백준 10430 나머지 ###
### https://www.acmicpc.net/problem/10430 ###

# 23:07 ~ 23:10 (3m)

# 입력받기
A,B,C = map(int, input().split())

# 출력하기
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#	맞았습니다!!