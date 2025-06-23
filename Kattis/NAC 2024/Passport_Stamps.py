import sys
input = sys.stdin.readline
from math import ceil
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n,free = multiple_ints()
  
  total = 0
  arr = []
  for i in range(n):
    arr.append(int(input()))

  for i, curr in enumerate(arr):
    #if I want to fail index I, then I want to use a maximal amount of spacing w/ each space being at most curr - 1
    
    #I have i segments of spacing I can use and prior filler
   
    rem = free//(i+1) if free%(i+1) == 0 else free//(i+1) + 1
    if rem < (curr):
      print(i)
      return
    free -= curr
    
  
  print(n)

solve()