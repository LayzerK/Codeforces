import sys
from math import ceil
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  a,b,c = multiple_ints()

  total = a + b + c
  
  if total % 2:
    print(-1)
    return
  else:
    #pair A with B
    #pair B with C?

    diff = c-b

    with_c = min(a, diff)

    rest = a-with_c

    ans = with_c + rest

    c -= with_c - rest//2
    b -= ceil(rest/2)

    ans += min(b, c)

    print(ans)

  
for tc in range(int(input())):
  solve()
    