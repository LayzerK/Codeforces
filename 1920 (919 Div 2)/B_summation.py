import sys
input = sys.stdin.readline
from itertools import accumulate
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,alice_lim,bob_lim = multiple_ints()
  
  arr = list(multiple_ints())
  
  arr.sort(reverse = True)
  arr.append(0)
  prefix = list(accumulate(arr))
  
  ans = -(10**20)

  for removed in range(alice_lim+1):
    

    neg_endpt = min(n, removed + bob_lim - 1)
    removed_vals = 0 if removed == 0 else prefix[removed - 1]
    
    negated_vals = prefix[neg_endpt] - removed_vals
    
    rest = prefix[n] - prefix[neg_endpt]
    
    ans = max(ans, rest-negated_vals)
  print(ans)


for tc in range(int(input())):
  solve()
    