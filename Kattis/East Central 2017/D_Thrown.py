import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,k = multiple_ints()
  pos = [0] * (k+1)
  arr = list(input().strip().split())
  
  throw = 0
  i = 0
  while i < len(arr):
    if arr[i] == 'undo':
      shift = int(arr[i+1])
      throw = max(0, throw-shift)
      i += 2
    else:
      curr = pos[throw]
      dist = int(arr[i])
      new = (curr + dist)%n
      
      throw += 1
      i += 1
      
      pos[throw] = new
  print(pos[throw])

solve()