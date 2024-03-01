import sys
from math import floor,ceil
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  vehicles = []
  for v in range(n):
    pos, vel = multiple_ints()
    vehicles.append((pos, vel))

  
  
  
  eps = 10**-7
  
  left = 0
  right = 10**10
  
  def check(time):
    lb = 10**20
    rb = -(10**20)
    for pos, vel in vehicles:
      new_pos = vel * time + pos
      lb = min(lb, new_pos)
      rb = max(rb, new_pos)
    return rb-lb
      
  while eps <= right-left:
    mid = (left+right)/2
    
    
    if check(mid) <= check(mid+eps):
      right = mid - eps
    else:
      left = mid + eps
  print(check(mid))
  
    

solve()
    