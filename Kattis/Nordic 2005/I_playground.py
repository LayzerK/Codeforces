import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())
def multiple_floats():
  return map(float, input().strip().split())


while True:
  amount = int(input())

  if amount == 0:
    break
  
  shapes = list(multiple_floats())
  shapes.sort()

  curr = 0
  v = False
  for shape in shapes:
    if shape <= curr:
      print("YES")
      v = True
      break
    curr += shape
  if v == False:
    print("NO")

