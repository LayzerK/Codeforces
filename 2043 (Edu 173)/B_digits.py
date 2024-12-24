import sys
input = sys.stdin.readline
from math import factorial
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n,d = multiple_ints()
  ans = [1]

  #3 case

  if n >= 3 or d == 3 or d == 9 or d == 6:
    ans.append(3)

  if d == 5:
    ans.append(5)
  
  if n >= 3 or d == 7:
    #if n! is a multiple of 6?? -> all n! >= 3
    ans.append(7)
  if n >= 6 or d == 9 or ((d == 3 or d == 6) and n >= 3):
    ans.append(9)
  
  print(*ans)
  
def brute_force(n,d):

  ans = [1]

  fac = factorial(n)

  num = int(str(d) * fac)

  ans = [1]

  if num % 3 == 0:
    ans.append(3)
  if num % 5 == 0:
    ans.append(5)
  if num % 7 == 0:
    ans.append(7)
  if num % 9 == 0:
    ans.append(9)
  return ans
for tc in range(int(input())):
  solve()