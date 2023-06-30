import sys
input = sys.stdin.readline
from collections import defaultdict
def solve():
    n = int(input())
    adj = defaultdict(list)
    for edge in range(n-1):
        a,b = map(int, input().strip().split())
        adj[a].append(b)
        adj[b].append(a)
    
    cnt = [0] * (n+1)
    
    def dfs(curr, par):
        
        if len(adj[curr]) == 1 and adj[curr][0] == par:
            cnt[curr] = 1
            return
        for nei in adj[curr]:
            dfs(nei, curr)
            cnt[curr] += cnt[nei]
    dfs(1, -1)
    for q in range(int(input())):
        a,b = map(int, input().strip().split())

        print(cnt[a] * cnt[b])

for tc in range(int(input())):
    solve()