from collections import Counter
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    n, m = map(int, input().split())

    seating = list(map(int, input().split()))

    taken = [False] * (m+1)

    lc = 0
    rc = 0
    for loc in seating:
        if loc == -1:
            lc += 1
        elif loc == -2:
            rc += 1
        else:
            taken[loc] = True
    lp = 0
    rp = 0
    choice = 0
    for i in range(1, m+1):
        loc = taken[i]
        if loc is False:
            rp += 1
        else:
            choice += 1
    ans = max(lc, rc) + choice
    for i in range(1, m+1):
        loc = taken[i]
        if loc is False:
            lp += 1
            rp -= 1
        else:
            ans = max(ans, min(lc, lp) + min(rc, rp) + choice)
    print(min(ans, m))
