import sys
input = sys.stdin.readline
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  arr = list(multiple_ints())
  ans = 1
  prior = defaultdict(lambda: -1)
  for i, val in enumerate(arr): 
    bit = 0
    #print(val, "HERE")
    if val == 0 and len(prior) != 0:
        #print("here")
        ans = max(ans, i - min(prior.values()) + 1)
    while (1 << bit) <= val:
      if val & 1 << bit:
        #print(i, "here", prior[bit+1], bit+1)
        ans = max(ans, i - prior[bit+1])
        prior[bit+1] = i
      bit += 1
  if len(prior) != 0:
    ans = max(ans, n - min(prior.values()))
  print(ans)


for tc in range(int(input())):
  solve()
    