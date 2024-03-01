import sys
input = sys.stdin.readline

vertices,e = map(int, input().strip().split())

colors = [0] * (vertices+1)
edges = []
adj = [[] for x in range(vertices+1)]
for edge in range(e):
    a,b = map(int, input().strip().split())
    edges.append((a,b))

    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (vertices+1)
visited[1]= True
valid = True
stack = [1]
while stack:
    curr = stack.pop()

    for nei in adj[curr]:
        if visited[nei] and colors[nei] == colors[curr]:
            valid = False
        elif not visited[nei]:
            colors[nei] = colors[curr] ^ 1
            stack.append(nei)
            visited[nei] = True

if not valid:
    print("NO")
else:
    ans = []
    for i, pair in enumerate(edges):
        a,b = pair

        ans.append(str(colors[a]))
    #print(colors)
    print("YES")
    print("".join(ans))
    
    