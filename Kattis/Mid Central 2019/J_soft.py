import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  s = input().strip()
  p = input().strip()
  
  if s == p:
    print("Yes")
    return
  elif s[1:] == p and s[0].isdigit():
    print("Yes")
  elif s[:len(s) - 1] == p and s[-1].isdigit():
    print("Yes")
  elif len(s) == len(p) and all((s[i].isnumeric and s[i] == p[i]) or (((s[i].isupper() and p[i].islower()) or (s[i].islower and p[i].isupper()))  and s[i].lower() == p[i].lower())for i in range(len(s))):
    print("Yes")
  else:
    print("No")
  

solve()
    