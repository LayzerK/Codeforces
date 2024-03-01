import sys
input = sys.stdin.readline

"""
observation:

If a component isn't "closed" then you can just tie it to another

how to determine if a component is closed?


6
2 3 1 5 6 4

5
3 5 4 1 2

these two have closed components    

"""
from collections import defaultdict

def solve():
    adj = defaultdict(list)
    n = int(input())

    unclosed = 0
    closed = 0
    visited = set()
    arr = list(map(int, input().strip().split()))
    for i,nei in enumerate(arr):
        if nei not in adj[i+1]:
            adj[i+1].append(nei)
        
        if i+1 not in adj[nei]:
            adj[nei].append(i+1)
    
    for x in range(1, n):
        if x not in visited:
            joinable = False

            stack = [x]
            visited.add(x)
            while stack:
                curr = stack.pop()

                if len(adj[curr]) != 2:
                    joinable = True 
                
                for nei in adj[curr]:
                    if nei != curr and nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            if joinable:
                unclosed += 1
            else:
                closed += 1
    #print(unclosed)
    mini = closed + min(1, unclosed)
    maxi = closed + unclosed

    print(mini, maxi)
                

    

    


for tc in range(int(input())):
    solve()