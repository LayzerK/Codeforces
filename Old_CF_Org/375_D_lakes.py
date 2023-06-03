import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque
import heapq
rLen, cLen, k = map(int, input().strip().split())
 
grid = [[] for r in range(rLen)]
 
for row in range(rLen):
    for col in input().strip():
        grid[row].append(col)
seen = set()
components = {}
invalid = {}
directions = [(0,1), (0,-1), (1,0), (-1,0)]
 
def comp(row, col):
    
    q = deque()
 
    q.append((row, col))
   
    while q:
        r, c = q.popleft()
        if r == 0 or r == rLen - 1 or c == 0 or c == cLen - 1:
            #print("here")
            invalid[(row, col)] = True
        components[(row, col)].append((r, c))
        seen.add((r,c))
 
        for dr, dc in directions:
            NR = r + dr
            NC = c + dc
 
            if 0 <= NR < rLen and 0 <= NC < cLen and grid[NR][NC] == "." and (NR, NC) not in seen:
                q.append((NR, NC))
 
 
    
 
 
for r in range(rLen):
    for c in range(cLen):
        if (r,c) not in seen and grid[r][c] == ".":
            components[(r,c)] = []
            comp(r,c)
sizes = []
#print(invalid)
for component, size in components.items():
    #print(component)
    if component not in invalid:
      heapq.heappush(sizes, (len(size), component))
 
req = len(components) - k - len(invalid)
ans = 0
for x in range(req):
    sz, loc = heapq.heappop(sizes)
    r,c = loc
    ans += sz
 
    for row, col in components[(r,c)]:
        grid[row][col] = "*"
print(ans)
for ln in grid:
    print("".join(ln))
#print(grid)
print(invalid)