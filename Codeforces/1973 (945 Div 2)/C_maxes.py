import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  #max number = (n-2)//2
  #can we always reach that max number?

  #say we have A,B,C,D,E,F
  #we can have maxes on B/D or C/E
  #when would we want to choose one or the other?

  #if I am considering B, let D1 be B-A and D2 be B-C
  #we care about filling in positive deltas first since those are the impactful ones
  #for positive deltas, fill in the adjacent ones with the lowest possible?
  
  n = int(input())
  p = list(multiple_ints())
  deltas = []
  arr = [0] * n

  for i in range(n):
    if i % 2 == 1 and i != n-1:
      continue
    l = 100000 if i == 0 else p[i-1] - p[i]
    r = 100000 if (i >= n-2) else p[i+1] - p[i]

    deltas.append((min(l,r), i))

  deltas.sort()
  rem = [i for i in range(len(deltas)+1,  n+1)]
  for i, (val, j) in enumerate(deltas):
    arr[j] = i + 1
  fill = []
  for i in range(1, n-1):
    if i % 2:
      fill.append((arr[i-1] + arr[i+1], i))
    
  fill.sort(reverse=True)

  for val, i in fill:
    arr[i] = rem.pop()
  
  print(*arr)








for tc in range(int(input())):
  solve()
    