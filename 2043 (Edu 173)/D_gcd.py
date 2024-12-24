import sys
input = sys.stdin.readline
from math import floor, ceil, gcd
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  lb, rb, G = multiple_ints()

  adjustedLB = lb//G
  if lb % G != 0:
    adjustedLB += 1

  adjustedRB = rb//G


  #A = G * n and B = G * m -> ensures GCD of at least G. To ensure GCD no GREATER than G, M and N must be coprime?

  #find farthest apart pair of coprime integers in the range A,B

  #from wikipedia it seems most numbers are coprime is actually like 60%??? just sample the first like, 10000 pairs


  maxDist = adjustedRB - adjustedLB
  for dist in range(maxDist, -1, -1):
    maxN = adjustedRB - dist
    for n in range(adjustedLB, maxN + 1):
      m = n + dist
      if gcd(n, m) == 1:
        A = G * n
        B = G * m
        print(A, B)
        return
  print(-1, -1)
for tc in range(int(input())):
  solve()
    