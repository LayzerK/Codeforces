import sys
input = sys.stdin.readline


def solve():
    n = int(input())

    used = set()

    s = input().strip()

    used.add(s[:2])

    for nxt in range(1, n-1):
        used.add(s[nxt:nxt+2])
    #print(used)
    print(len(used))
    


for tc in range(int(input())):
    solve()