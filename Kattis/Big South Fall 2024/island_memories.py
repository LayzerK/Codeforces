import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n,m = multiple_ints()
  arr = []

  for i in range(m):
    k = int(input())
    curr = set(multiple_ints())
    for prior in arr:
      intersection = prior & curr
      #print(intersection)
      if intersection and (len(intersection) != len(prior) and len(intersection) != len(curr)):
        print(0)
        return
    arr.append(curr)
  print(1)

solve()
    