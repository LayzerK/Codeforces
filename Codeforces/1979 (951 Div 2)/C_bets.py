import sys
from math import lcm, gcd
from functools import reduce
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  arr = list(multiple_ints())
  arr_lcm  = reduce(lcm, arr)
  total = sum(arr_lcm//x for x in arr)

  if total >= arr_lcm:
    print(-1)
  else:
    seq = [arr_lcm//x for x in arr]
    print(*seq)

for tc in range(int(input())):
  solve()
    