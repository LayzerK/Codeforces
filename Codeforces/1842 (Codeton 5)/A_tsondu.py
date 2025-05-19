import sys
input = sys.stdin.readline

def solve():
    n,m = map(int, input().strip().split())

    tson = list(map(int, input().strip().split()))
    tenz = list(map(int, input().strip().split()))

    tsum = sum(tson)
    zsum = sum(tenz)

    if tsum == zsum:
        print("Draw")
    elif tsum > zsum:
        print("Tsondu")
    else:
        print("Tenzing")

for tc in range(int(input())):
    solve()