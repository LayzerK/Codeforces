import sys
input = sys.stdin.readline
from math import ceil
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,k = multiple_ints()
  times = []
  
  for line in range(n):
    times.append(int(input()))
  times.sort()
  #binary search on the most number of times the most efficient car must go?
  
  left = 1
  right = 10**14

  def check(x):
    rem = n
    
    for i in range(min(len(times), k)):
      time = times[i]
      trips = x//time
      if trips:
        rem -= ceil(trips/2) * 4 + 1
      if rem <= 0:
        break
    #print(rem, x, "here")
    return rem <= 0    

  while left <= right:
    #print(left, right)
    mid = (left+right)//2
    
    if check(mid):
      right = mid - 1
    else:
      left = mid + 1
    
  #print(check(9000))
  print(left)

solve()
    