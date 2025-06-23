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
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  cap = n * 2
  dp = []
  dp_prime_condense = [defaultdict(lambda: cap + 1) for i in range(n)]

  def factorize(num):
    factors = []
    for p in primes:
      if num == 1:
        break
      elif num % p == 0:
        factors.append(p)
        while num % p == 0:
          num //= p
    if num > 100:
      return []
    if num > 1:
      factors.append(p)
    
    return factors
  

  precomp = {}
  valid = []
  for i in range(2, cap+1):
    f = factorize(i)
    if f:
      precomp[i] = f
      valid.append(i)
  
  for i in range(n):
    dp.append({})
    for v in valid:
      if vals[i] == v:
        dp[i][v] = 0
      else:
        dp[i][v] = v
  #print(dp[0], "HERE ASA SAS")
  #dp where dp[i][j] is the cost to make node i gcd harmonic with all of its children given that node i has value j

  #ans will never exceed n * 2, even in degenerate prime cases

  #can optimize by doing coordinate compression and only including valid precomp values? May be slower due to dict lookup thouugh
  for i in range(n):
    v = int(input())
    vals[i] = v
    dp[i][v] = 0
    dp[i][0] = cap + 1
    dp[i][1] = cap + 1
  for i in range(n-1):
    a,b = multiple_ints()
    a -= 1
    b -= 1
    adj[b].append(a)
    adj[a].append(b)
  
  def dfs(curr, par):
    #print("HERE", curr, par)
    for child in adj[curr]:
      if child == par:
        continue
      dfs(child, curr)

      for val in valid:
        #if we went to set curr to val, we need to transition from any value in child that is GCD harmonic with val
        #this is just any value that shares a prime factor
        #condense all prime factors into one
        #we want to choose the prime factor w/ minimum cost
        child_cost = cap + 1
        for factor in precomp[val]:
          child_cost = min(child_cost, dp_prime_condense[child][factor])
        #print(child_cost, curr, child, val)
        dp[curr][val] += child_cost
      
      #print(dp[curr], curr, "HERE")
      #condense all values in DP
    for val in valid:
      for factor in precomp[val]:
        dp_prime_condense[curr][factor] = min(dp_prime_condense[curr][factor], dp[curr][val])
    #print("FINISHED", dp_prime_condense[curr])
    #print(dp[curr], "HERE", curr)
  dfs(0, -1)
  

  print(min(dp[0].values()))
  #print(dp)

solve()