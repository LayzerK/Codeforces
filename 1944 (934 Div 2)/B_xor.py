import sys
from collections import Counter
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,k = multiple_ints()
  arr = list(multiple_ints())
  left = arr[:n]
  right = arr[n:]

  #there will either be an even # of some value in the left or right half, or 1 of each. Just do the 0 pairs + the same am ount of odd numbers

  Lcnt = Counter(left)
  Rrnt = Counter(left)

  left_evens = []
  right_evens = []
  odds = []

  for num in range(1, n+1):
    if Lcnt[num] == 1:
      odds.append(num)
    elif Lcnt[num] == 2:
      left_evens.append(num)
    else:
      right_evens.append(num)
  
  fill_in = k*2 - len(left_evens)*2
  left_ans = []
  right_ans = []
  for i in range(min(k, len(left_evens))):
    left_ans.append(left_evens[i])
    left_ans.append(left_evens[i])
    right_ans.append(right_evens[i])
    right_ans.append(right_evens[i])
  for i in range(0, fill_in, 1):
    left_ans.append(odds[i])
    right_ans.append(odds[i])
  
  print(*left_ans)
  print(*right_ans)



for tc in range(int(input())):
  solve()
    