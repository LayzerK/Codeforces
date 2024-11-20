from collections import defaultdict
def multiple_ints():
    return map(int, input().strip().split())

n, m, req = multiple_ints()

n += 1


edges = [0 for i in range(n)]

par = [i for i in range(n)]
rank = [1 for i in range(n)]

children = defaultdict(list)

unreturned = defaultdict(set)

def find(node):
    if par[node] != node:
        par[node] = find(par[node])
    return par[node]

def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if p1 == p2:
        return
    
    if rank[p1] > rank[p2]:
        par[p2] = p1
    elif rank[p2] > rank[p1]:
        par[p1] = p2
    else:
        par[p2] = p1
        rank[p1] += 1

seen = set()

for pair in range(m):
    a,b = multiple_ints()
    if (b,a) not in seen:
        unreturned[b].add(a)
        unreturned[a].add(b)
    else:
        unreturned[a].remove(b)
        unreturned[b].remove(a)
        union(a,b)
        edges[a] += 1
        edges[b] += 1

    seen.add((a,b))


for i in range(1, n):
    p = find(i)
    children[p].append(i)


ans = 0

for root, childs in children.items():
    size = len(childs)
    if size == req:
        valid = True
        for child in childs:
            if edges[child] != size - 1 or len(unreturned[child]) != 0:
                valid = False
                break
        if valid:
            ans += 1

print(ans)