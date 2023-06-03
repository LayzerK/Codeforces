import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    
    adj = [[] for vertice in range(n+1)]

    for edge in range(1, n):
        a,b = map(int, input().strip().split())
        adj[a].append((b,edge))
        adj[b].append((a, edge))
    if n%3:
        print(-1)
        return
    size = [0] * (n+1)
    cut = []
    def dfs(curr, par):
        for child, edgenum in adj[curr]:
            if child == par:
                continue
            
            dfs(child, curr)

            size[curr] += size[child]

            #if the size of the child is % 3 then we have to cut

            if size[child] % 3 == 0:
                cut.append(edgenum)
            
        size[curr] += 1
    dfs(1, -1)
    #a cut tree has to have n//3 - 1 cuts
    #print(cut)
    if len(cut) != (n//3) - 1:
        print(-1)
    else:
        print(len(cut))
        print(*cut)

for tc in range(int(input())):
    solve()