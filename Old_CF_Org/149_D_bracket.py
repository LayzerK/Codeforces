import sys
input = sys.stdin.readline


def solve():
  n = int(input())
  s = input().strip()

  mapping = {")":"(", "(":")"}
  


  cnts = {}
  cnts["("] = 0
  cnts[")"] = 0
  ans = []

  
  for char in s:
    #print(cnts)
    if char == "(":
      if cnts[mapping[char]]:
        cnts[mapping[char]] -= 1
        ans.append(2)
      else:
        cnts[char] += 1
        ans.append(1)
    elif char == ")":
      if cnts[mapping[char]]:
        cnts[mapping[char]] -= 1
        ans.append(1)
      else:
        cnts[char] += 1
        ans.append(2)

  if sum(cnts.values()) != 0:
    print(-1)
    return
  l = len(set(ans))
  if l == 1:
    for i in range(len(s)):
      ans[i] = 1
  print(l)
  print(*ans)
    
for tc in range(int(input())):
    solve()
