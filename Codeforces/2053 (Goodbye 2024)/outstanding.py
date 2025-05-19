import sys
from collections import defaultdict
from itertools import accumulate
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())

  bounds = []
  sweep = [0] * (2 * n + 10)
  cnts = [0] * (2 * n + 10)
  for i in range(n):
    lb, rb = multiple_ints()
    if lb == rb:
      sweep[lb] = 1
      cnts[lb] += 1
    bounds.append((lb, rb))


  sweep = list(accumulate(sweep))
  ans = []
  for lb, rb in bounds:
    cnt = sweep[rb] - sweep[lb-1]
    size = rb - lb + 1
    if lb == rb and cnts[lb] == 1:
      ans.append("1")

    elif cnt >= size:
      ans.append("0")
    else:
      ans.append("1")
  #print("MY ANSWER")
  print("".join(ans))

for tc in range(int(input())):
  solve()
    