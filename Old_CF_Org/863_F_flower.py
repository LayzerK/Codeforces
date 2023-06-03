from math import sqrt
from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start, adj, used):
    sz = 0

    stack = [start]
    used[start] = True
    while stack:
        curr = stack.pop()
        sz += 1

        for nei in adj[curr]:
            if not used[nei]:
                stack.append(nei)
                used[nei] = True
    return sz


for tc in range(int(input())):
    valid = True
    empty = input()
    n, m = map(int, input().split())
    adj = defaultdict(list)
    indegree = defaultdict(int)
    for edge in range(m):
        a, b = map(int, input().split())

        adj[a].append(b)
        adj[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    k = sqrt(n)
    if n != k*k or m != n + k:
        print("no")
        continue
    for v in range(1, n+1):
        if indegree[v] != 2 and indegree[v] != 4:
            print("no")
            #print(v, indegree[v])
            valid = False
            break
    if not valid:
        continue
        # all k flowers will have an indegree of 2 or 4 if they are in the main cycle
    # test for connectivity
    used = [False] * (n+1)

    if dfs(1, adj, used) != n:
        print("no")
        # print("here")
        continue

    # sever the center connections and ensure everything decomposes into a SCC of size K
    used = [False] * (n+1)
    remove = []
    for node, freq in indegree.items():
        if freq == 4:
            for nei in adj[node]:
                if indegree[nei] == 4:
                    remove.append((node, nei))

    for a, b in remove:
        adj[a].remove(b)
    for node in range(1, n+1):
        if not used[node] and dfs(node, adj, used) != k:
            print("no")

            valid = False
            break
    if not valid:
        continue
    print('yes')
