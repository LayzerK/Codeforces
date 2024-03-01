import sys
input = sys.stdin.readline


def solve():
    
    n,c = map(int, input().strip().split())

    costs = map(int, input().strip().split())

    adj = []

    for i,cost in enumerate(costs):
        adj.append(i+1+cost)
    adj.sort()

    taken = 0

    while taken < n and c - adj[taken] >= 0:
        c -= adj[taken]
        taken += 1
    print(taken)

for tc in range(int(input())):
    solve()