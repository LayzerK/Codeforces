import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  arr = list(multiple_ints())
  
  arr.sort()
  
  ans =  arr[-1] - arr[0] + arr[-2] - arr[1]
  
  print(ans * 2)

for tc in range(int(input())):
  solve()
    