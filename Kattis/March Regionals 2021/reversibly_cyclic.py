import sys
input = sys.stdin.readline
from collections import defaultdict, deque
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  s = input().strip()
  n = len(s)
  ans = True
  subs = defaultdict(set)
  base = 347
  pows = [1] * (n+1)
  MOD = 10**9 + 7

  for i in range(1, n):
      pows[i] = (pows[i-1] * base) % MOD
  
  for i in range(n):
    pat = []
    patHash = 0

    for j in range(i, n):
      pat.append(s[j])
        
      v = ord(pat[-1])
      patHash = (patHash * base + v) % MOD
      subs[len(pat)].add(patHash)
      
  def test(sub):
    patLength = len(sub)
    window = 0
    for i in range(patLength):
        curr = ord(sub[i])
        window = (window * base + curr) % MOD
    #print(window, subs)
   # print(window, subs)
    if window in subs[len(sub)]:
        return True
    for i in range(len(sub)):
       curr = ord(sub[i])
       prior = ord(sub[i])
       window = ((window - prior * pows[patLength-1])* base + prior) % MOD
       #print(window, "here", len(pat))
       if window in subs[len(sub)]:
          return True
    #print(sub)
    return False
  for i in range(len(s)):
     sub = deque()
     for j in range(i, len(s)):
        sub.appendleft(s[j])
        if i == 0 and j == len(s)-1:
           continue
        ans &= test(sub)
        if not ans:
           print(0)
           return
  print(1)
       
    
    
solve()
    