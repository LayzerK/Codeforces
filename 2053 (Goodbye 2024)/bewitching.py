import sys
from collections import defaultdict
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve(n, k):
  starts = []
  steps = []
  terms = []
  factor = []

  fac = 0
  ans = 0
  t = 1
  while n >= k:
    if n % 2 == 1:
      steps.append(n)
      starts.append((n//2 + 1))
      terms.append(t)
      factor.append(fac)
    n//= 2
    t *= 2
    fac += 1

  prior = 0

  for start, step, terms, fac in zip(starts, steps, terms, factor):

    
    total = terms/2 * (2*start + terms * step - step)
    if fac:
      total += prior * (1<<(fac-1))
    ans += int(total)
    prior += terms
  print(ans)

def brute_force(n, k):
  arr = []
  cnts = defaultdict(int)
  vals = defaultdict(list)
  def dfs(l, r):
    size = (r-l+1)
    if size <= k and k != 1:
      return
    if l > r:
      return
    mid = (l+r)//2

    if size % 2 == 1:
      arr.append((mid, size))
      cnts[size] += 1
      vals[size].append(mid)
      dfs(l, mid-1)
      dfs(mid+1, r)
    else:
      dfs(l, mid)
      dfs(mid+1, r)
  dfs(1, n)
  arr.sort()

  print(cnts)
  #print(vals[45])
  starts = []
  steps = []
  terms = []
  factor = []

  fac = 0
  ans = 0
  t = 1
  while n >= k:
    if n % 2 == 1:
      steps.append(n)
      starts.append((n//2 + 1))
      terms.append(t)
      factor.append(fac)
    n//= 2
    t *= 2
    fac += 1
  print(steps)

  prior = 0

  wtf = 0
  for start, step, terms, fac in zip(starts, steps, terms, factor):

    
    total = terms/2 * (2*start + terms * step - step)
    rv = sum(vals[step])
    print("pre", total - rv, prior, fac)
    if fac:
      total += prior * (1<<(fac-1))
    print(total, "real value", sum(vals[step]))
    ans += int(total)
    prior += terms

  print(ans)
  a2 = 0
  for v in vals:
    a2 += sum(vals[v])
  print(a2)

    
  return 2

for tc in range(int(input())):
  n,k = multiple_ints()
  
  solve(n, k)
  #brute_force(n, k)