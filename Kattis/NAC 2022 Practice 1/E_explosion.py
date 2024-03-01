import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,m,d = multiple_ints()

  yours = list(multiple_ints())
  opps = list(multiple_ints())
  
  y_health = [0] * 7
  o_health = [0] * 7
  for x in yours:
    y_health[x] += 1
  for x in opps:
    o_health[x] += 1
  
  if d >= sum(yours) + sum(opps):
    print(1)
    return
  if d < sum(opps):
    print(0)
    return
  
  cache = {}
  def dfs(you, opp, rem):
    
    tple = (tuple(you), tuple(opp), rem)
    if tple in cache:
      return cache[tple]
    #print(you, opp, rem)
    if opp[0] == m:
      cache[tple] = 1
      return 1
    
    req = sum(i * x for i,x in enumerate(opp))

    if rem == 0 or req > rem:
      cache[tple] = 0
      return 0
    
    
    
    valid = 0
    total = 0
    for i,x in enumerate(you):
      if i and x:
        you[i] -= 1
        you[i-1] += 1
        valid += dfs(you,opp, rem-1) * x
        total += x
        you[i] += 1
        you[i-1] -= 1
    for i,x in enumerate(opp):
      if i and x:
        opp[i] -= 1
        opp[i-1] += 1
        valid += dfs(you, opp, rem-1) * x
        total += x
        opp[i] += 1
        opp[i-1] -= 1
    #print(valid, total)
    return valid/total
  
  print(dfs(y_health, o_health, d))

      
    

solve()
