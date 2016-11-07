#!/usr/bin/env python3

n = int(input("input n: "))
print("\n")
m = int(input("input m: "))
print("\n")
k = int(input("input k: "))
print("\n")

if k % m == 0:
  if n >= k / m:
    print("YES")
  else:
    print("NO")
elif k % n == 0:
  if m >= k / n:
    print("YES")
  else:
    print("NO")
else:
  print("NO")
