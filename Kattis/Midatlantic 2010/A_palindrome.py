import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve(s):
  sz = len(s)


  if s == s[::-1]:
    print(0)
    return
  
  dig = int(s)

  i = 0

  while True:
    dig += 1
    i += 1
    sdig = str(dig)

    sdig = "0" * (sz-len(sdig)) + sdig

    if sdig == sdig[::-1]:
      print(i)
      return
  

while True:
  s = input().strip()
  if s == "0":
    break
  solve(s)