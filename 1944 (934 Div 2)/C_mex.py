import sys
from collections import Counter
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = multiple_ints()
  arr = list(multiple_ints())
  arr.sort()
  biggest = -1
  cnts = Counter(arr)
  risk = False
  for num in sorted(cnts.keys()):
    if num > biggest + 1: 
      print(biggest + 1)
      return
    elif cnts[num] == 1 and risk:
      print(num)
      return
    elif cnts[num] == 1:
      risk = True

    biggest = num
  print(arr[-1] + 1)
for tc in range(int(input())):
  solve()
    