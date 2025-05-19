import sys
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():  
  n = int(input())
  s = input().strip()

  for i in range(len(s)-1):
    if ord(s[i]) > ord(s[i+1]):
      print(s[:i] + s[i+1:])
      return
  print(s[:-1])  

solve()