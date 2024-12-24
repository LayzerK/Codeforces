import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())

  ans = 1

  while n > 3:
    n //= 4
    ans *= 2
  print(ans)

for tc in range(int(input())):
  solve()
    