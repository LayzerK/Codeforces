import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())

  countries = []
  neis = []

  cmap = {}
  imap = {}
  for i in range(n*2):
    country = input().strip()
    nei = list(input().strip().split())
    countries.append(country)
    neis.append(nei)
  
  for i,c in enumerate(countries):
    cmap[c] = i
    imap[i] = c
  
  dp = {}
  def dfs(used, left, right):
    if (used, left, right) in dp:
      return dp[(used, left, right)]
    
    if used.bit_count() == n:
      return True
    
    i = used.bit_count()

    for bit in range(n):
      c = imap[bit]

      if (1 << bit) & used:
        continue
      
      
      if c not in neis[left] or imap[left] not in neis[bit]:
        continue
      
      if i == (n-1) and (c not in neis[right] or imap[right] not in neis[bit]):
        continue
      
      nmask = used | (1<<bit)
      
      a = dfs(nmask, bit, right)

      if a:
        #print("HEREERERE", left, right, bit)
        #print(neis[left])
        return True
    dp[(used, left, right)] = False
    return False
  
  for i in range(n):
    for j in range(n):
      if i == j or imap[i] not in neis[j] or imap[j] not in neis[i]:
        continue
      #print("HASA")
      mask = (1<<i) | (1<<j)
      a = dfs(mask, i, j)
      if a:
        #print(i, j, "here")
        print("true")
        return
  print("false")

solve()