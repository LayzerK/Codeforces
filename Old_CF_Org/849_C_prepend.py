import sys
input = sys.stdin.readline


def solve():
  n = int(input())
  left = 0
  right = n - 1

  s = input().strip()

  while left < right and s[left] != s[right]:
    left += 1
    right -= 1

  print(right-left+1)

for tc in range(int(input())):
  solve()