import sys
input = sys.stdin.readline

def solve():
  n, m, d = map(int, input().strip().split())
  locs = [1] + list(map(int, input().strip().split())) + [n]
  prior = 1
  total = 1
  ans = 0

  for i in range(1, m+1):
    curr = locs[i]
    prior = locs[i-1]

    if curr == prior:
      continue

    nxt = locs[i+1]

    sentinel = int(nxt == locs[-1] and curr!=nxt)
    

    priorfree = curr-prior - 1
    nxtfree = nxt-curr - sentinel
    excludewindow = nxt-prior - sentinel

    included = priorfree//d + 1 + nxtfree//d
    excluded = excludewindow//d

    #print(priorfree, nxtfree, excludewindow)
    if included != excluded:
       ans += 1
    total += priorfree//d + 1
  
  print("answer here:")
  if ans == 0:
     print(total, m)
  else:
     print(total-1, ans)

    
    


     #gain from removing the current cookie seller -> we get nxt-prior-1 locations to pick up a free cookie + the seller at nxt (if its not the sentinel)
     #gain from keeping- > we get the cookies in the prior window if possible, cookie here, cookies in the nxt window + the seller at nxt (if its not the sentinel)
    


  



  #no point in removing a cookie seller from the 1st position OR any position 


for tc in range(int(input())):
    solve()
    