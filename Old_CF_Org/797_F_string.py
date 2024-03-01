import sys
input = sys.stdin.readline
from collections import defaultdict
from math import lcm
def solve():
    
    n,s = int(input()), input().strip()
    arr = list(map(int, input().strip().split()))

    cycles = []
    visited = [False] * (n+1)
    def cyclelength(start):
      subword = []
      stack = [start]
      while stack:
        curr = stack.pop()
        subword.append(s[curr-1])
        visited[curr] = True
        if arr[curr-1] == start:
          break
        stack.append(arr[curr-1])
      cycles.append("".join(subword))

    def mincost(start):
      cost = 1

      new = start[-1] + start[:len(start)-1]

      while new != start:
          new = new[-1] + new[:len(new)-1]
          cost += 1
      return cost


    for i in range(1, n+1):
       if not visited[i]:
          cyclelength(i)
    
    ans = 1

    for subword in cycles:
       ans = lcm(ans, mincost(subword))
    
    print(ans)

for tc in range(int(input())):
   solve()  