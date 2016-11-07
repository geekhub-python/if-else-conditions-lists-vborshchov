#!/usr/bin/env python3

year = int(input("input year: "))
print("\n")

if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
  print("YES")
else:
  print("NO")