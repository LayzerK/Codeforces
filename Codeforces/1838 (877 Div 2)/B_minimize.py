import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    oneloc = 0
    twoloc = 0
    nloc = 0

    for i,num in enumerate(arr):
        if num == 1:
            oneloc = i + 1
        elif num == 2:
            twoloc = i + 1
        elif num == n:
            nloc = i + 1
    
    if oneloc <= nloc <= twoloc or twoloc <= nloc <= oneloc:
        print(oneloc, twoloc)
    elif nloc < oneloc and nloc < twoloc:
        print(nloc, min(oneloc, twoloc))
    elif nloc > oneloc and nloc > twoloc:
        print(nloc, max(oneloc, twoloc))


for tc in range(int(input())):
    solve()