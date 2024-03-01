import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  s = int(input())
  
  ans = []
  
  for frow in range(2,s):
    both = frow*2 - 1
    if s % both == 0 or s%both == frow:
      ans.append((frow, frow-1))
    if s % frow == 0:
      ans.append((frow, frow))
  print(f"{s}:")
  for a,b in ans:
    print(f"{a},{b}")
    
    

solve()