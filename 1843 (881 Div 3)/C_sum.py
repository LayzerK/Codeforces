import sys
input = sys.stdin.readline

memo = {}

def solve():
    n = int(input())
    og = n
    if n in memo:
        print(memo[n])
        return

    ans = 0
    while n:
        ans += n
        n//=2
    memo[og] = ans
    print(ans)


for tc in range(int(input())):
    solve()