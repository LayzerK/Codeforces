import sys
input = sys.stdin.readline


def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    nodupes = []

    for x in arr:
        if nodupes and nodupes[-1] == x:
            continue
        nodupes.append(x)
    ans = len(nodupes)
    for mid in range(1, len(nodupes)-1):
        ans -= int((nodupes[mid-1] < nodupes[mid] < nodupes[mid+1]) or (nodupes[mid-1]> nodupes[mid] > nodupes[mid+1]))
    print(ans)
for tc in range(int(input())):
    solve()
