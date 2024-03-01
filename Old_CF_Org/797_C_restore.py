import sys
input = sys.stdin.readline
from collections import deque


def solve():
    n = int(input())
    arrival = list(map(int, input().strip().split()))
    end = list(map(int, input().strip().split()))
    ans = [0 for x in range(n)]

    curr = 0
    q = deque()
    for i,n in enumerate(arrival):
        q.append((n,i))

    while q:
        atime, i = q.popleft()

        curr = max(atime, curr)

        ans[i] = end[i] - curr
        curr = end[i] 
    print(*ans)
for tc in range(int(input())):
    solve()