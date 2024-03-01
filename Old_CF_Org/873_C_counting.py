import sys
input = sys.stdin.readline


def solve():

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 10**9 + 7
    asort = sorted(a, reverse=True)
    bsort = sorted(b, reverse=True)
    ans = 1
    right = 0
    #print(asort, bsort)
    for i, num in enumerate(bsort):
        while right < len(a) and asort[right] > num:
            right += 1
        #print(right, right-i,)
        ans *= max(0, (right-i))
        ans = ans % MOD
    print(ans)
    # number of ways is just spare elements greater * next spa
    # re elements greater * so on by the product rule


for tc in range(int(input())):
    solve()
