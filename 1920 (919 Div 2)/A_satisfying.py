import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  
  lo = -1
  hi = 10**20
  banned = []
  
  for constraint in range(n):
    a,x = multiple_ints()
    
    if a == 1:
      lo = max(lo, x)
    elif a == 2:
      hi = min(hi, x)
    else:
      banned.append(x)
    
  total = hi-lo + 1
  if total <= 0:
    print(0)
    return
  for x in banned:
    if lo <= x <= hi:
      total -= 1
  print(total)

for tc in range(int(input())):
  solve()
    