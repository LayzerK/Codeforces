from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    v, e = map(int, input().split())

    adj = defaultdict(list)

    for edge in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    q = deque()
    even = []
    odd = []
    seen = [False] * (v+1)
    seen[1] = True
    q.append((1, 0))

    while q:
        curr, dist = q.popleft()
        #print(dist, "dist", curr)
        if dist % 2:
            odd.append(str(curr))
        else:
            even.append(str(curr))

        for nei in adj[curr]:
            if not seen[nei]:
                q.append((nei, dist+1))
                seen[nei] = True
    #print(odd, even)
    if len(odd) < len(even):
        print(len(odd))
        print(" ".join(odd))
    else:
        print(len(even))
        print(" ".join(even))
