import sys
from collections import defaultdict
input = sys.stdin.readline


def solve():
    n = int(input())

    edgemap = {}
    adj = defaultdict(list)

    for edge in range(n-1):
        a, b = map(int, input().split())
        edgemap[(a, b)] = edge
        edgemap[(b, a)] = edge
        adj[a].append(b)
        adj[b].append(a)

    output = [0] * (n-1)
    for node in adj:
        if len(adj[node]) >= 3:
            print(-1)
            return

    stack = [(1, -1, -1)]
    while stack:
        used = False
        curr, par, parweight = stack.pop()
        for child in adj[curr]:
            if par != child:
                if par == -1:
                    if not used:
                        output[edgemap[(child, curr)]] = "2"
                        stack.append((child, curr, 2))
                    else:
                        output[edgemap[(child, curr)]] = "17"
                        stack.append((child, curr, 17))
                    used = True
                elif parweight == 2:
                    output[edgemap[(child, curr)]] = "17"
                    stack.append((child, curr, 17))
                else:
                    output[edgemap[(child, curr)]] = "2"
                    stack.append((child, curr, 2))

    print(" ".join(output))


for tc in range(int(input())):
    solve()
