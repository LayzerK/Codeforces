import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  imap = {}
  wnodes = {}
  output = []
  for i in range(n):
     comp = input().strip()
     imap[comp] = i
  rank = [1 for x in range(n)]
  par = [x for x in range(n)]
  
  
  def find(node):
      if par[node] != node:
          par[node] = find(par[node])
      return par[node]
  
  def union(n1, n2):
      p1 = find(n1)
      p2 = find(n2)
      
      if rank[p1] > rank[p2]:
          par[p2] = p1
      elif rank[p2] > rank[p1]:
          par[p1] = p2
      
      else:
          par[p2] = p1
          rank[p1] += 1
  
  while True:
    start = list(input().strip().split())
    if len(start) == 1:
      break
    
    if start[0] == "COMPETITION":
      size = int(start[1])

      winner = input().strip()
      
      for loser in range(1, size):
        union(imap[winner], imap[input().strip()])
      wnodes[find(imap[winner])] = winner
    else:
       person = start[1]
       a = wnodes[find(imap[person])]
       output.append(a)
       print(a)

solve()