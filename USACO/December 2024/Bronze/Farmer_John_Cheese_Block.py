import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n, q = multiple_ints()

  xy = defaultdict(lambda: n)
  xz = defaultdict(lambda: n)
  yz = defaultdict(lambda: n)


  ans = 0
  for i in range(q):
    x,y,z = list(multiple_ints())

    xy_pair = (x,y)
    xz_pair = (x,z)
    yz_pair = (y,z)

    xy[xy_pair] -= 1
    ans += xy[xy_pair] == 0

    xz[xz_pair] -= 1
    ans += xz[xz_pair] == 0

    yz[yz_pair] -= 1
    ans += yz[yz_pair] == 0

    print(ans)




    


solve()