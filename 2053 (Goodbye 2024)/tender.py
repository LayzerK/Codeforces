import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n = int(input())
  arr = list(multiple_ints())

  #it suffices to check if there are any elements that work with eachother

  #two elements work with eachother if 2x > y, x + y > x and 2y > x


  for i in range(len(arr)-1):
    x = arr[i]
    y = arr[i+1]
  

    if 2 * x > y and 2 * y > x:
      print("YES")
      return
  print("NO")

for tc in range(int(input())):
  solve()
    