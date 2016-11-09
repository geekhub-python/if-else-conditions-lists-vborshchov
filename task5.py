#!/usr/bin/env python3

lists = [
  [-1, 2, 3, -1, -2],
  [1, 2, -3, -4, -5],
  [1, -2, 3, -4, -5],
  [1, -2, 3, -4, 5, 6]
]

print(lists)

def sublings_finder(number_list):
  for i in range(len(number_list)-1):
    current_el = number_list[i]
    next_el = number_list[i+1]
    if current_el != 0 and next_el != 0:
      if current_el * next_el > 0:
        return (current_el, next_el)

for list in lists:
  print(sublings_finder(list))