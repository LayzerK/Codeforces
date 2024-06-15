import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  arr = list(multiple_ints())
  ans = max(arr[0], arr[1]) - 1

  for i in range(1, len(arr)-1):
    LG = max(arr[i], arr[i-1])
    RG = max(arr[i], arr[i+1])

    ans = min(ans, LG-1, RG-1)

  print(ans)

for tc in range(int(input())):
  solve()
    