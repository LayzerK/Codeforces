import sys
input = sys.stdin.readline
from collections import defaultdict
n,m = map(int, input().strip().split())


rank = [1 for x in range(n+1)]
par = [x for x in range(n+1)]
indegree = [0] * (n+1)


def find(node):
    if par[node] != node:
        par[node] = find(par[node])
    return par[node]

def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)
    
    if rank[p1] > rank[p2]:
        par[p2] = p1
    elif rank[p2] > rank[p1]:
        par[p1] = p2
    
    else:
        par[p2] = p1
        rank[p1] += 1


unneeded =[0 for x in range(n+1)]

for edge in range(m):
    a,b = map(int, input().strip().split())

    indegree[b] += 1
    indegree[a] += 1

    union(a,b)

components = defaultdict(list)
ans = 0
for i in range(1, n+1):
    components[find(i)].append(i)

for i, comp in components.items():
    valid = True
    for node in comp:
        if indegree[node] != 2:
            valid = False
    ans += int(valid)
print(ans)
