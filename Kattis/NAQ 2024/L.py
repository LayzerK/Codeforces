import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  rLen, cLen = multiple_ints()

  grid = []
  for row in range(rLen):
    grid.append(list(input().strip()))

for tc in range(int(input())):
  solve()
    