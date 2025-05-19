import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().strip().split()))

    used = False

    ans = 1
    mn = min(arr)
    for n in arr:
        if n == mn and not used:
            ans *= (n+1)
            used = True
        else:
            ans *= n
    print(ans)

for tc in range(int(input())):
    solve()