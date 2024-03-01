import sys
input = sys.stdin.readline
#greedily create the longest cycle possible, count everything else
from collections import deque
from heapq import heapify, heappop, heappush
def solve():
    n = int(input())
    adj = list(map(int, input().strip().split()))

    visited = [False] * (n+1) 
    
    cycles = []
    def cyclelength(start):
        #print(start, "here")
        stack = [start]
        ln = 0
        while stack:
          curr = stack.pop()
          ln += 1
          visited[curr] = True
          if adj[curr-1] == start:
              return ln
          stack.append(adj[curr-1])
    for start in range(1, n+1):
        if not visited[start]:
            cycles.append(-cyclelength(start))
    ans = 0
    heapify(cycles)
    if len(cycles) >= 2:
        a = -heappop(cycles)
        b = -heappop(cycles)

        ans += (a+b)**2

        for element in cycles:
            ans += element**2
    else:
        ans += cycles[0] ** 2
    print(ans)

        


solve()