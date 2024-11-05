import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  ans = 0
  for i in range(n):
    d = int(input())
    ans += d % 2
  print(ans)

solve()
    