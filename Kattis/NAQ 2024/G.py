import sys
from collections import defaultdict
from math import log
from math import e
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  gears = []

  paths = defaultdict(list)
  mx = 0
  for gear in range(n):
    size, count = multiple_ints()
    gears.append((size, count))
    paths[size].append(count)
    mx = max(mx, len(paths[size]))

  ans = 0
  for size in paths:
    paths[size].sort(reverse = True)
  

  rem = list(paths.keys())
  speed = 1

  cnt = 0
  cap = 10**9
  for size in paths:
    p = paths[size]
    if len(p) == 1:
      continue
    seqA = 1
    seqB = 1

    for i in range(len(p)//2):
      seqA *= p[i]/p[len(p) - i - 1]
    for i in range(len(p)-1):
      seqB *= p[i]/p[i+1]
    
    if len(p) == mx and len(p)%2:
      seqA = 1
    speed *= max(seqA, seqB)
    if speed >= cap:
      speed = log(speed, e)
      cnt += 1
  for i in range(cnt):
    speed = pow(e, speed)
  print(log(speed, e))

solve()