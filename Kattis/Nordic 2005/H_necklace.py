import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())
def is_necklace(start):
  for first in range(1, len(start)):
    rotate = start[first:] + start[:first]
    if rotate < start:
      return False
  return True

def solve():
  s = input().strip()

  start = 0
  ans = []
  while start < len(s):
    end = len(s)
    #print(start, end)
    while end > start:
      cut = s[start:end]
      if(is_necklace(cut)):
        ans.append("(" + cut + ")")
        start = end
        break
      else:
        end -= 1
  #print(ans)
  print("".join(ans))


for tc in range(int(input())):
  solve()
    