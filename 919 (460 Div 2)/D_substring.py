import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n,m = multiple_ints()
    s = input().strip()
    
    adj =  [[] for node in range(n+1)]
    res = 1
    dp = [[0 for i in range(26)] for node in range(n+1)]
    indegree = [0 for node in range(n+1)]

    for edge in range(m):
        start, end = multiple_ints()

        indegree[end] += 1
        adj[start].append(end)
    
    
    q = deque()
    visited = 0
    for node in range(1, n+1):
        if indegree[node] == 0:
            q.append(node)
    
    while q:
        curr = q.popleft()
        char_indice = ord(s[curr-1]) - ord('a')
        dp[curr][char_indice] += 1
        res = max(res, max(dp[curr]))
        visited += 1

        for nei in adj[curr]:
            for i, val in enumerate(dp[curr]):
                dp[nei][i] = max(dp[nei][i], val)
            
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)
        
    
    if visited == n:
        print(res)
    else:
        print(-1)



    
solve()