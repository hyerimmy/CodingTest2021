# https://www.acmicpc.net/problem/2941

input = str(input())
result = len(input)

if "c=" in input:
  result -= 1*input.count("c=")
  #print("c=")

if "c-" in input:
  result -= 1*input.count("c-")
  #print("c-")


if "d-" in input:
  result -= 1*input.count("d-")
  #print("d-")

if "lj" in input:
  result -= 1*input.count("lj")
  #print("lj")

if "nj" in input:
  result -= 1*input.count("nj")
  #print("nj")

if "s=" in input:
  result -= 1*input.count("s=")
  #print("s=")

if "z=" in input:
  result -= 1*input.count("z=")
  #print("z=",1*input.count("z="))

if "dz=" in input:
  result -= 1*input.count("dz=")
  #print("dz=")

print(result)