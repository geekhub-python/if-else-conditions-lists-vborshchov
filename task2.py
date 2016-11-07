#!/usr/bin/env python3

a = int(input("input A: "))
print("\n")
b = int(input("input B: "))
print("\n")
c = int(input("input C: "))
print("\n")

result = 1
if a == b == c:
  result = 3
elif a == b:
  result += 1
elif b == c:
  result += 1
elif c == a:
  result += 1
else:
  result = 0


print(result)