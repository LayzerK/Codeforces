import sys
from collections import defaultdict
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())


class Node:
  def __init__(self):
    self.left = None
    self.right = None
    
def solve():  
  n,k = multiple_ints()

  if 2 > (1 << k):
    print("impossible")
    return
  adj = defaultdict(list)

  

for tc in range(int(input())):
  solve()
    