import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
  sLen, tLen = multiple_ints()

  s = input().strip()
  t = input().strip()

  if "*" not in s:
    if s != t:
        print("NO")
    else:
        print("YES")
    return
  #match the prefix and match the suffix

  for i, char in enumerate(s):
     if char == "*":
        loc = i
        break
  
  prefix = s[:loc]
  suffix = s[loc+1:]

  if len(prefix) + len(suffix) > tLen:
     print("NO")
     return
  
  suffixLen = len(suffix)
  prefixLen = len(prefix)
  #test if non zero or zero
  #zero case

  #print(t[:prefixLen], t[tLen - suffixLen:], "here")
  if prefix + suffix == t:
     print("YES")
  elif t[:prefixLen] == prefix and t[tLen-suffixLen:] == suffix:
     print("YES")
  else:
     print("NO")


solve()