import sys
input = sys.stdin.readline
from math import gcd
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  arr = []
  mx = 1
  for i in range(n):
    arr.append(int(input()))
    mx = max(mx, arr[-1])
  
  arr.append(-1)

  ans = 0
  
  for goal in range(1, mx+1):
    curr = arr[0]
    for i in range(n):
      curr = gcd(curr, arr[i])
      #print(curr, goal)
      if curr % goal != 0:
        curr = arr[i+1]
      elif goal == curr:
        ans += 1
        break
  print(ans)

solve()
    