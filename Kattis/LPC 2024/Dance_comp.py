import sys
from collections import deque
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  dancers, threshold = multiple_ints()

  arr = []
  subs = {}
  for i in range(dancers):
    arr.append(list(input().strip().split()))
  
  copy = set()
  for d in arr:
    dancer = d[0]
    q = deque()
    for i in range(1, len(d)):
      q.append(d[i])


      if len(q) > threshold:
        q.popleft()
      

      if len(q) == threshold:
        hsh = tuple(q)
        if hsh in subs and subs[hsh] != dancer:
          copy.add(dancer)
          copy.add(subs[hsh])
        subs[hsh] = dancer
  print(len(copy))

solve()
    