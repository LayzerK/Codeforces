import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,k = multiple_ints()
  if k >= n-1:
    print(1)
  else:
    print(n)

for tc in range(int(input())):
  solve()
    