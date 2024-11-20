import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  req = 2 * n
  drawings = n * 10
  cnts = [0] * 51

  for drawing in range(drawings):
    draw = list(multiple_ints())
    for num in draw:
      cnts[num] += 1
  ans = [i for (i,c) in enumerate(cnts) if c > req]
  if not ans:
    print(-1)
  else:
    print(*ans)

solve()
    