#!/usr/bin/env python3
import math

lists = [
  [1, 2, 3, 2, 3],
  [1, 1, 1, 1, 1],
  [1, 2, 3],
  [1, 1, 1],
  [2, 3],
  [2, 2],
  [0, 0],
  [0, 0, 6, 1, 1, 4, 2, 1, 2, 2],
  [0, 1, 43, 10, 13, 33, 15, 8, 18, 21],
  [3, 2, 1, 2, 2, 4, 3, 2, 5, 3, 2]
]

print(lists)

def pair_counter(number_list):
  result = []
  unique = set(number_list)
  for number in unique:
    result.append(number_list.count(number))

  pairs_number = 0
  for x in result:
    if x >= 2:
      pairs_number += math.factorial(x) // (math.factorial(x-2) * 2)

  return pairs_number

for list in lists:
  print(pair_counter(list))