from collections import defaultdict
for tc in range(int(input())):
    n, m = map(int, input().split())
    adj = defaultdict(list)

    for edge in range(m):
        a, b = map(int, input().split())

        adj[a].append(b)
        adj[b].append(a)

    x = 1
    y = 0
    exy = 0
    for v in adj:
        if len(adj[v]) == 1:
            y = len(adj[adj[v][0]]) - 1
            exy = adj[v][0]

    for nei in adj[exy]:
        x = max(x, len(adj[nei]))

    print(x, y)
