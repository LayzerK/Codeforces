import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
  n,k = multiple_ints()
  s = input().strip()
  removed = n-k
  #construct a valid sequence of length K from an input N
  if n == k:
    print(s)
    return
  
  #we can just remove valid sequences from s

  stack = []
  matched = set()
  output = []

  for i,char in enumerate(s):
    if char == "(":
      stack.append(i)
    elif len(matched) < removed:
      matched.add(i)
      matched.add(stack.pop())

    if len(matched) == removed:
      break
  
  for i, char in enumerate(s):
    if i not in matched:
      output.append(char)

  print("".join(output))

solve()