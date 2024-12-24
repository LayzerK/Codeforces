import sys
from collections import defaultdict
input = sys.stdin.readline
def multiple_ints():
  return map(int, input().strip().split())

def solve():
  n, req = multiple_ints()
  s = input().strip()

  moo_count = defaultdict(int)
  ans = set()

  for i in range(len(s) - 2):
    a,b,c = s[i], s[i+1], s[i+2]

    if a != b and b == c:
      moo_count[s[i:i+3]] += 1
  
  #simulate changes

  for i in range(len(s)):
    char = s[i]

    containing = []
    lb = max(0, i-2)
    rb = min(len(s) - 1, i + 2)
    for j in range(lb, rb - 1):
      containing.append(s[j:j+3])

    #print(containing)
    for j in range(26):
      if j == ord(char) - ord("a"):
        continue

      new_char = chr(ord("a") + j)
      if i < len(s) - 2:
        #first
        b,c = s[i+1], s[i+2]
        a = new_char

        new_sub = a + b + c
        overlap = int(new_sub in containing)
        if moo_count[new_sub] + 1 - overlap >= req and a != b and b == c:
          ans.add(new_sub)
      

      if i > 0 and i < len(s) - 1:
        a, c = s[i-1], s[i+1]
        b = new_char

        new_sub = a + b + c
        overlap = int(new_sub in containing)
        if moo_count[new_sub] + 1 - overlap >= req and a != b and b == c:
          ans.add(new_sub)


      if i > 1:
        a,b = s[i-2], s[i-1]
        c = new_char

        new_sub = a + b + c
        overlap = int(new_sub in containing)
        if moo_count[new_sub] + 1 - overlap >= req and a != b and b == c:
          ans.add(new_sub)



  for moo, count in moo_count.items():
    if count >= req:
      ans.add(moo)
  ans = list(ans)
  ans.sort()
  print(len(ans))
  for moo in ans:
    print(moo)


solve()