import sys


def f(i):
    s = 0
    for x in range(9):
        if i & (1 << x):
            s += 1
    return s


input = sys.stdin.readline
MOD = 10**9 + 7
for tc in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # according to constraints n is less than 63. Since btiwise & can never make a number go up, the bitwise & is also capped at 63 set bits

    # let dp[i][j] be the number of ways to use the first I elements such that the & value is J
    # the issue is how can I track how bitwise AND transitions between state

    prior = [0 for x in range(64)]
    for num in arr:
        dp = [0 for x in range(64)]
        dp[num] = 1

        for p in range(64):
            new = p & num
            dp[p] = (dp[p] + prior[p]) % MOD
            dp[new] = (dp[new] + prior[p]) % MOD
        prior = dp

    ans = 0
    for i, num in enumerate(dp):
        if f(i) == k:
            ans += num
    print(ans % MOD)
