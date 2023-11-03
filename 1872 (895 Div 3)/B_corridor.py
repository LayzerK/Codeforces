import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())

def solve():
    n = int(input())
    arr = [0 for trap in range(n)]

    for i in range(n):
        loc, time = multiple_ints()
        arr[i] = (loc, time)
    arr.sort()

    ans = 10000

    for loc, time in arr:
        ans = min(ans, loc+(time-1)//2)
    print(ans)

for tc in range(int(input())):
    solve()
    