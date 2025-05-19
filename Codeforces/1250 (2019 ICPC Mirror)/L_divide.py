import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  a,b,c = multiple_ints()
  total = a+b+c
  def check(big):
    return big * 3 >= total and (a <= big or c <= big) and max(a,c) <= big * 2
  
  left = 1
  right = total
  
  while left <= right:
    mid = (left + right)//2
    if check(mid):
      right = mid - 1
    else:
      left = mid + 1
  #print(check(left))
  print(left)
    

for tc in range(int(input())):
  solve()
    