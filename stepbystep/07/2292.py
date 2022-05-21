#벌집
#https://www.acmicpc.net/problem/2292

n = int(input())
result = 0
i=1

if(n>1):
  n=n-1
  while n>0:
    result+=1
    n-=i*6
    i+=1
    # print("i : "+str(i)+" / n : "+str(n)+" / result : "+str(result))
result+=1

print(result)