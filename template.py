import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,k = multiple_ints()
  s = list(input().strip())

  moved = 0
  
  for i in range(len(s)):
    if not k:
      break
    if s[i] == "1":
      continue
    dist = min(i - moved, k)
    s[i], s[i-dist] = s[i-dist], s[i]
    moved += 1

    k -= dist
  print("".join(s))

for tc in range(int(input())):
  solve()
    