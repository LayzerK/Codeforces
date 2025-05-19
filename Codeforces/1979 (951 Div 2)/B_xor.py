import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  """
  observation #1: if the parity of the two numbers is different, then I vaguely feel that the answer will always be 1?
  observation #2: answer always seems to be a power of 2?
  observation #3: first bit where they differ
  
  """
  a,b = multiple_ints()

  for i in range(35):
    val = 1 << i

    if (val & a) ^ (val & b):
      print(val)
      return

for tc in range(int(input())):
  solve()
    