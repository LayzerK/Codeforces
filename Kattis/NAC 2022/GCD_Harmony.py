import sys
input = sys.stdin.readline
from math import sqrt, gcd, inf
from collections import defaultdict
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  vals = [0 for i in range(n)]
  adj = [[] for i in range(n)] 
  cap = 100
  for i in range(n):
    v = int(input())
    vals[i] = v
  for i in range(n-1):
    a,b = multiple_ints()
    a -= 1
    b -= 1
    adj[b].append(a)
    adj[a].append(b)
  

  works = defaultdict(list)

  for i in range(2, 101):
    for j in range(2, 101):
      if gcd(i, j) > 1:
        works[i].append(j)

  memo = {}

  dp = []

  def dfs(curr, par):
    if (curr, par, p_val) in memo:
      return memo[(curr, par, p_val)]
    
    #we assume by induction that everything p_val and above gcd harmonizes, therefore we have to change to something that harmonizes with p_val
    if par == -1:
      poss = list(range(2, 101))
    else:
      poss = works[p_val]
    ans = inf
    if len(adj[curr]) == 1 and adj[curr][0] == par:
      return 0 if vals[curr] in poss else poss[0]
    for c_val in poss:
      cost = c_val if c_val != vals[curr] else 0
      for nei in adj[curr]:
        if nei == par:
          continue
        nei_cost = dfs(nei, curr, c_val)
        cost += nei_cost
      ans = min(ans, cost)
    return ans
  
  ans =  dfs(0, -1, -1)

  print(ans)

  #when is it not optimal to change a node to 2
  #imagine an entire tree of like 79s with one leaf 2 -> if the tree is big enough then it makes sense to change to 79 instead of making all the 79s to 2
  #since v is 1 thru 100, can we try every 'family' of numbers?
  #i.e. all the multiples of primes?
  # this doesn't work -> just do a dp where we try all values? N * V where V is 100

solve()